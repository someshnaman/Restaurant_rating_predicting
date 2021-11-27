import pandas as pd

from application_logging.app_logger import App_logger


class Data_Getter:
    """
    This class will be used for getting the data for training

    """

    def __init__(self, file_object, logger_object):
        self.logger = logger_object
        self.file_location = './training_data/zomato.csv'
        self.file_object = file_object

    def get_data(self):
        """
        This method will read the csv file.

        :return: data
        """
        self.logger.log(self.file_object, "Initialising the get_data method")
        try:
            data = pd.read_csv(self.file_location)
            self.logger.log(self.file_object, "Successfully completed the reading the data")
            print('done')
            return data
        except Exception as e:
            self.logger.log(self.file_object,
                            "Some error has occurred in Get_data class. The error message is " + str(e))
            self.logger.log(self.file_object, "Data loading Unsuccessful")
            raise Exception()





