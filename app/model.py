import numpy as np
from PIL import Image
import lightgbm as lgbm
from tensorflow.keras.applications import ResNet50, imagenet_utils
from tensorflow.keras.applications.imagenet_utils import (decode_predictions,
                                                          preprocess_input)
from tensorflow.keras.preprocessing.image import img_to_array
import pickle
def load_model():
    '''loading the trained model'''
    pickle_in = open('LGBMClassifier.pkl', 'rb') 
    clf = pickle.load(pickle_in)
    return clf
    
    
def predict(content, model):
    # We keep the 2 classes with the highest confidence score
    results = decode_predictions(model.predict(content), 2)[0]
    response = [
        {"class": result[1], "score": float(round(result[2], 3))} for result in results
    ]