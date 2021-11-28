import os
import pickle
from application_logging.app_logger import App_logger
from data_preprocessing.preprocessing import Preprocessing
import numpy as np


class prediction:
    def __init__(self):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.logger = App_logger()

    def predictionFromModel(self, dict_of_user_values):
        try:
            # First of all we've to encode our data
            self.logger.log(self.file_object, "Starting converting the user data for model")
            data_conversion = Preprocessing(self.file_object, self.logger)
            data_to_send_to_model = data_conversion.convertingCatagoricalForPrediction(dict_of_user_values)

            self.logger.log(self.file_object, "Data preprocessing is done for prediction")

            # Now we're loading model from model directory
            for file in os.listdir('./models'):
                if '.sav' in file:
                    path_of_model = './models/' + file
                    with open(path_of_model, 'rb') as f:
                        model = pickle.load(f)
                        predicted_data = np.round(model.predict(np.array([data_to_send_to_model])), 1)

                    self.logger.log(self.file_object, f"Prediction is done from given data the rating for "
                                                      f"given Restaurant is {predicted_data} ")
                    self.file_object.close()
                    return predicted_data
        except Exception as e:
            self.logger.log(self.file_object, "Something went wrong in prediction Please check" + str(e))
            self.file_object.close()
            raise Exception()



