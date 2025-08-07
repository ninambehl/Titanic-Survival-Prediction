import pickle as pkl
import joblib as jb

def predict(data):
    loaded_model = jb.load("./titan_data.pkl")
    predictions = loaded_model.predict(data)
    return predictions