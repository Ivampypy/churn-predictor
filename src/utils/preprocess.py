import pandas as pd
from pathlib import Path
from src.utils.config import raw_data
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import torch
import sys 

class Preprocess:
    def __init__(self, path: Path = raw_data):
        self.path = path
        self.data = None
        self.scaler = StandardScaler()
        self.encoding_classes = {}

    def read_raw(self, path: Path = raw_data):

        if not path.exists():
            raise FileExistsError("File does not exist!")

        self.data = pd.read_csv(path, sep=",")

    def drop_column(self):
        self.read_raw()
        self.data = self.data.drop(columns="customerID")

    def enc_norm_cl(self):
        X = self.data.drop(columns="Churn")

        self.data["TotalCharges"] = pd.to_numeric(
            self.data["TotalCharges"], errors="coerce"
        ).fillna(0.0)
        cols_to_norm = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]
        cols_to_enc = [col for col in X.columns if col not in cols_to_norm]

        for col in cols_to_enc:
            enc = LabelEncoder()
            self.data[col] = enc.fit_transform(self.data[col])
            self.encoding_classes[col] = enc.classes_

        self.data[cols_to_norm] = self.scaler.fit_transform(self.data[cols_to_norm])

    def data_split(self):
        target = (self.data["Churn"] == "Yes").astype(int)
        X = self.data.drop(columns="Churn")

        trd, testd, trtarg, testtarg = train_test_split(
            X, target, stratify=target, test_size=0.2, random_state=864
        )
        return [trd, testd, trtarg, testtarg]

    def save_to_disk(self):
        list_chs = self.data_split()
        trd, testd, trtarg, testtarg = (
            list_chs[0],
            list_chs[1],
            list_chs[2],
            list_chs[3],
        )

        cols_to_norm = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]
        Cols_to_enc = [col for col in trd.columns if col not in cols_to_norm]

        X_num_tr = torch.tensor(trd[cols_to_norm].values, dtype=torch.float32)
        X_cat_tr = torch.tensor(trd[Cols_to_enc].values, dtype=torch.long)

        X_num_ts = torch.tensor(testd[cols_to_norm].values, dtype=torch.float32)
        X_cat_ts = torch.tensor(testd[Cols_to_enc].values, dtype=torch.long)

        torch.save(
            {
                "X_num": X_num_tr,
                "X_cat": X_cat_tr,
                "target": torch.tensor(trtarg.values).float(),
            },
            "data/preprocessed/train.pt",
        )
        torch.save(
            {
                "X_num": X_num_ts,
                "X_cat": X_cat_ts,
                "target": torch.tensor(testtarg.values).float(),
            },
            "data/preprocessed/test.pt",
        )

    def __call__(self):
        self.read_raw()
        self.drop_column()
        self.enc_norm_cl()
        self.save_to_disk()


if __name__ == "__main__":
    prep = Preprocess()
    prep()
