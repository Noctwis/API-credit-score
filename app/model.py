import numpy as np
#from PIL import Image
import lightgbm as lgbm
import pickle
import json
import pandas as pd

def load_model():
    '''loading the trained model'''
    pickle_in = open('LGBMClassifier.pkl', 'rb') 
    clf = pickle.load(pickle_in)
    return clf
   
    
def prepare_cli(content):
    #dicte = json.loads(content)
    df2 = pd.read_json(content)
    return df2
    
   
def predict(sample, id, clf):
    X=sample.iloc[:, :-1]

    score = clf.predict_proba(X)[0][1] * 100
    return score