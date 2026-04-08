import numpy as np
import tensorflow
from keras.models import load_model
from keras.preprocessing import image
import os






class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename




   
    def predict(self):
        # load model
        model = load_model(r"E:\projects\DL_kidney_tumor_pred\kidney_tumor_prediction_project\artifacts\training\model.keras")
        # insted of upper line paste this below lines 
        # model_path = os.path.join("model",, "model.keras")
        # model = load_model(model_path)


        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)


        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]


