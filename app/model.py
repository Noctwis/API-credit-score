import numpy as np
#from PIL import Image
import lightgbm as lgbm
import pickle
def load_model():
    '''loading the trained model'''
    pickle_in = open('LGBMClassifier.pkl', 'rb') 
    clf = pickle.load(pickle_in)
    return clf

def load_data():
    z = ZipFile("data/default_risk.zip")
    data = pd.read_csv(z.open('default_risk.csv'), index_col='SK_ID_CURR', encoding ='utf-8')

    z = ZipFile("data/X_sample.zip")
    sample = pd.read_csv(z.open('X_sample.csv'), index_col='SK_ID_CURR', encoding ='utf-8')
       
    description = pd.read_csv("data/features_description.csv", 
                              usecols=['Row', 'Description'], index_col=0, encoding= 'unicode_escape')

    target = data.iloc[:, -1:]

    return data, sample, target, description    
    
def prepare_cli(content):
    dicte = json.loads(content)
    df2 = pd.DataFrame.from_dict(dicte)
    return df2
    
   
def predict(sample, id, clf):
    X=sample.iloc[:, :-1]

    score = clf.predict_proba(X[X.index == int(id)])[:,1]
    return score