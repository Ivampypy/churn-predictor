from fastapi import FastAPI,HTTPException
from api.base_model import ClientData
from models.model import ChurnMLP
import src.utils.config as conf
import torch
import json


app = FastAPI()


model = None
cat_classes = None
scaler = None


@app.on_event("startup")
def load_artif():
    global model, cat_classes, scaler
    print("Loading of the model...")
    with open(conf.cat_cl, "r") as f:
        cat_classes = json.load(f)
    with open(conf.scal_json, "r") as f:
        scaler = json.load(f)
    model = ChurnMLP(num_lay_sz=4, cat_classes=cat_classes)
    model.load_state_dict(torch.load(conf.weights_pt, weights_only=True))
    model.eval()
    print("Loading of the model is successfully finished!")


@app.get("/health")
def get_st() -> dict:
    return {"status": "ok"}


@app.post("/predict")
def predict_churn(data: ClientData) -> dict :
    client_data=data.dict()
    X_cat,X_num=list(),list()
    for key,value in client_data.items():
        if key in cat_classes:
            if value not in cat_classes[key]:
                raise HTTPException(status_code=400, detail=f"Неверное значение '{value}' для поля '{key}'")
            id_val=cat_classes[key].index(value)

            X_cat.append(id_val)
        else:
            idx=scaler['cols'].index(key)
            n_val=(value-scaler['mean'][idx])/scaler['scale'][idx]
            X_num.append(n_val)

    X_cat=torch.tensor(X_cat,dtype=torch.long).unsqueeze(0)
    X_num=torch.tensor(X_num,dtype=torch.float).unsqueeze(0)

    logits=model(X_num,X_cat)
    prob=torch.sigmoid(logits).item()

    return {'probability': prob, 'will_churn': prob>0.35}
    

    
