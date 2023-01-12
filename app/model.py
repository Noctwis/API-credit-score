import numpy as np
#from PIL import Image
import lightgbm as lgbm
import pickle
def load_model():
    '''loading the trained model'''
    pickle_in = open('LGBMClassifier.pkl', 'rb') 
    clf = pickle.load(pickle_in)
    return clf
    
   
def predict(content, id, model):
    X=content.iloc[:, :-1]

    score = clf.predict_proba(X[X.index == int(id)])[:,1]
    return score