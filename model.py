import joblib
import xgboost
from xgboost import XGBClassifier
import os
import numpy as np




curr_path = os.path.dirname(os.path.realpath(__file__)) +  r'/p2tmlc.json'

model_xgb = XGBClassifier()
model_xgb.load_model(curr_path)






def predict(attributes: np.array):
    
    pred = model_xgb.predict(attributes)

    print("Probabilty predicted")

    return pred[0]
