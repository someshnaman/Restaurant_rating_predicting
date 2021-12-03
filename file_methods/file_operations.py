import joblib
import os


class File_methods:
    """
    This class will be responsible for all the methods related to model dumping,
    loading etc.
    """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger = logger_object
        self.model_directory = './models/'

    def save_model(self,model, file_name):
        """
        this method will help in saving the model ito svg format

        :return: saved model
        """
        self.logger.log(self.file_object, "Initialising the save_model method")
        try:
            path = os.path.join(self.model_directory, file_name)
            with open(path+'.sav', 'wb') as f:
                joblib.dump(model,f)
            self.logger.log(self.file_object, "Successfully saved the model")
            return 'Success'
        except Exception as e:
            self.logger.log(self.file_object, "There is some problem in saving the model"+str(e))

    def load_model(self, file_name_with_path):
        """
        this method is used for predicting from the model
        :param file_name_absolute_path
        :return:
        """
        try:
            with open(file_name_with_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            self.logger.log(self.file_object, "There is some problem in loading the model"+str(e))









