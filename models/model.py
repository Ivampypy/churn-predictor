import torch 
import torch.nn as N

class ChurnMLP(N.Module):

    def __init__(self, num_lay_sz: int ,cat_classes: dict, emb_dim: int = 8):
        super().__init__()

        self.embeddings=N.ModuleList([
            N.Embedding(len(cat_classes[col]),embedding_dim=emb_dim) for col in cat_classes.keys()
        ])

        input_layer_size=num_lay_sz+len(cat_classes)*emb_dim

        self.mlp=N.Sequential(
            N.Linear(input_layer_size,64),
            N.ReLU(),
            N.Dropout(0.2),

            N.Linear(64,32),
            N.ReLU(),
            N.Dropout(0.15),

            N.Linear(32,1)
        )

    def forward(self,x_num,x_cat):

        embs=[]

        for i, emb in enumerate(self.embeddings):
            embs.append(emb(x_cat[:,i]))

        preact_layer=torch.cat([x_num]+embs,dim=1)

        logits=self.mlp(preact_layer)

        return logits.squeeze(-1)

        