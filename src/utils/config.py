import pathlib as pth

current_dir= pth.Path(__file__).resolve().parent


project_root = current_dir.parent.parent
raw_data=project_root/'data'/'raw'/'WA_Fn-UseC_-Telco-Customer-Churn.csv'

preprocessed_train_data=project_root/'data'/'preprocessed'/'train.pt'
preprocessed_test_data=project_root/'data'/'preprocessed'/'test.pt'

cat_cl=project_root/'loaded_models'/'categorical_classes.json'
scal_json=project_root/'json_artifacts'/'scaler.json'
