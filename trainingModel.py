from application_logging.app_logger import App_logger
from data_ingestion.data_getter import Data_Getter
from data_preprocessing.preprocessing import Preprocessing
from best_model_finder.tuner import Model_finder
from file_methods.file_operations import File_methods


class trainModel:
    """
    this model will be used for training of the model
    """

    def __init__(self):
        self.logger = App_logger()
        self.file_object = open("Training_Logs/ModelTrainingLog.txt", 'a+')

    def trainingModel(self):
        self.logger.log(self.file_object, "Starting the Model training")
        try:
            # First we will start with data ingesting
            data_getter = Data_Getter(self.file_object, self.logger)
            data = data_getter.get_data()
            self.logger.log(self.file_object, "Data has successfully imported to training module")
            """ doing the data preprocessing. 
            All the pre processing steps are based on the EDA done previously
            """
            """
            1. Duplicate
            2. Remove columns: 	"serial","rate","listed_in(type)","listed_in(city)"
            3. Null removal
            4. Convert cost column to number
            5. Categorical to Numerical
            """
            # Starting with the data preprocessing part
            data_preprocessing = Preprocessing(self.file_object, self.logger)
            data = data_preprocessing.removeUnnecessaryColumns(data, ['url', 'address', 'name', 'phone', 'dish_liked',
                                                                      'reviews_list', 'listed_in(type)'])
            self.logger.log(self.file_object, "Unnecessory columns from the data has been successfully removed")

            # Heading toward removing duplicate values
            data = data_preprocessing.removeDuplicates(data)
            self.logger.log(self.file_object, "Duplicates have  been successfully removed")

            # removing null values from the data
            data = data_preprocessing.removeNullValues(data)
            self.logger.log(self.file_object, "null values have  been successfully removed from the data")

            # renaming the column name
            data = data_preprocessing.renameColumns(data, {'approx_cost(for two people)': 'cost',
                                                           'listed_in(city)': 'city'})
            self.logger.log(self.file_object, "renaming of column is successfully done")

            # formatting cost column
            data = data_preprocessing.convertingCostToFloat(data)
            self.logger.log(self.file_object, "Conversion of cost column into float datatype is done")

            # formatting rating column
            data = data_preprocessing.formattingRatingColumn(data)
            self.logger.log(self.file_object, "formatting for rating column is done")

            # converting categorical into numerical
            data = data_preprocessing.convertingCatagoricalToNumerical(data)
            self.logger.log(self.file_object, "Conversion  of categorical is successfully done")

            # separating feature and label
            x, y = data_preprocessing.separateFeatureAndLabel(data)
            self.logger.log(self.file_object, "Conversion  of categorical is successfully done")

            """
            Now we'll start with the Model training part
            """
            model_finder = Model_finder(self.file_object, self.logger, x, y)
            best_model_name, best_model = model_finder.get_best_model()
            self.logger.log(self.file_object, f"best Model is {best_model_name}")

            # now we'll save the model though pickle
            file_method_object = File_methods(self.file_object, self.logger)
            save_model = file_method_object.save_model(best_model, best_model_name)
            self.logger.log(self.file_object, f"{best_model_name} Model has been successfully saved")
            self.file_object.close()
        except Exception as e:
            self.logger.log(self.file_object, "Training Unsuccessful The error is " + str(e))
            self.file_object.close()
            raise Exception()
