
import datetime
import pickle
import json
import base64
import warnings
warnings.filterwarnings("ignore")
from . import image_converter
import keras
keras.backend.clear_session()
def predict_plant_disease(imgpth):
    try:
        with open(imgpth, "rb") as f:
            encoded = base64.b64encode(f.read())
         
        image_data = encoded.decode("utf-8")
        image_array, err_msg = image_converter.convert_image(image_data)
        if err_msg == None :
            model_file = "./models/cnn_model.pkl"
            saved_classifier_model = pickle.load(open(model_file,'rb'))
            prediction = saved_classifier_model.predict(image_array)
            label_binarizer = pickle.load(open("./models/label_transform.pkl",'rb'))
            return_data = f"{label_binarizer.inverse_transform(prediction)[0]}"
        
    except Exception as e:
        return_data =  str(e)
       
    return return_data
# Create your views here.