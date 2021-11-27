import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pickle
import os
from file_methods.file_operations import File_methods


class Preprocessing:
    """
    This class is going to used completely for data preprocessing part.
    """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger = logger_object

    def removeUnnecessaryColumns(self, data, columns):
        """
        This method will take list of columns which are supposed to be removed
        :param columns:
        :return: a Dataframe with the desired number of columns
        """
        self.logger.log(self.file_object, "Initialising the removeUnnecessaryColumns method")
        self.data = data
        self.columns = columns
        try:
            self.useful_data = self.data.drop(columns=self.columns)
            self.logger.log(self.file_object, "The given number of columns has been successfully removed")
            return self.useful_data
        except Exception as e:
            self.logger.log(self.file_object, "Some error has occurred in removing Unnecessary columns."
                                              "The error message is " + str(e))
            raise Exception()

    def removeDuplicates(self, data):
        """
        This method will be used for removing duplicate values in data

        """
        self.logger.log(self.file_object, "Starting removing duplicates from the data")
        try:
            count = data.duplicated().sum()
            if count > 0:
                data.drop_duplicates(inplace=True)
            self.logger.log(self.file_object, "Duplicate values has been removed")
            return data
        except Exception as e:
            self.logger.log(self.file_object, "Some error has occurred in removing duplicates. The error is: " + str(e))

    def removeNullValues(self, data):
        """
        We will use this method to remove the data which had null values

        :param data:
        :return:
        """
        self.logger.log(self.file_object, "removing null values method has been called ")
        try:
            data.dropna(how='any', inplace=True)
            self.logger.log(self.file_object, "removing null values From data has been completed")
            return data
        except Exception as e:
            self.logger.log(self.file_object,
                            "Some error has occurred in removing null value data.Error message " + str(e))

    def renameColumns(self, data, dict_of_columns_to_be_updated):
        """
        This function will be used for renaming the columns.
        :param data:
        :param dict_of_columns_to_be_updated:
        :return:
        """

        self.logger.log(self.file_object, "renaming the columns from the data")
        try:
            data = data.rename(columns=dict_of_columns_to_be_updated)
            self.logger.log(self.file_object, "removing null values method has been called renaming of columns has "
                                              "been completed")
            return data
        except Exception as e:
            self.logger.log(self.file_object, "Some error has happened in renaming the columns" + str(e))

    def convertingCostToFloat(self, data):
        try:
            data['cost'] = data['cost'].apply(lambda x: x.replace(",", ""))
            data['cost'] = data['cost'].astype('float')
            return data
        except Exception as e:
            self.logger.log(self.file_object, "Some error has happened in converting cost" + str(e))
            raise Exception()

    def formattingRatingColumn(self, data):
        data = data.loc[data.rate != '-']
        data = data.loc[data.rate != 'NEW']
        data.rate = data['rate'].apply(lambda x: x.replace("/5", ""))
        return data

    def convertingCatagoricalToNumerical(self, data):
        try:
            data.online_order = data.online_order.replace(("Yes", "No"), (1, 0))
            data.book_table.replace(("Yes", "No"), (1, 0), inplace=True)
            for column in data.columns[~data.columns.isin(['book_table', 'online_order', 'cost', 'votes', 'rate'])]:
                encoder = LabelEncoder()
                data[column] = encoder.fit_transform(data[column])
                path_to_save_file = open('./encoder' + '/' + column + '.sav', 'wb')
                pickle.dump(encoder, path_to_save_file)
                path_to_save_file.close()
            return data
        except Exception as e:
            self.logger.log(self.file_object, "Some error has happened in converting categorical to numerical" + str(e))
            raise Exception()

    def separateFeatureAndLabel(self, data):
        self.X = data.drop(columns=["rate"])
        self.Y = data.rate
        return self.X, self.Y

    def standardScalingData(self, X):
        scalar = StandardScaler()
        X_scaled = scalar.fit_transform(X)
        return X_scaled

    def convertingCatagoricalForPrediction(self, dict_of_user_data):
        try:
            result_dict = {}
            for key in dict_of_user_data.keys():
                dir_of_encoder = './encoder/'

                if os.path.isfile(dir_of_encoder + key + '.sav'):
                    with open(dir_of_encoder + key + '.sav', 'rb') as f:
                        encoder = pickle.load(f)

                        if dict_of_user_data[key] in encoder.classes_:
                            result_dict[key] = encoder.transform([dict_of_user_data[key]])[0]

                        else:
                            new_encoder = LabelEncoder()
                            result_dict[key] = new_encoder.fit_transform([dict_of_user_data[key]])[0]

                elif key == 'votes' or key == 'cost':
                    result_dict[key] = dict_of_user_data[key]
                else:
                    encoder = LabelEncoder()
                    result_dict[key] = encoder.fit_transform([dict_of_user_data[key]])[0]

            data_to_send_to_model = [result_dict['online_order'], result_dict['book_table'],
                                     result_dict['votes'],
                                     result_dict['location'], result_dict['rest_type'],
                                     result_dict['cuisines'], result_dict['cost'],
                                     result_dict['menu_item'], result_dict['city']]
            return data_to_send_to_model
        except Exception as e:
            raise Exception()
