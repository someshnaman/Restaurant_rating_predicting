from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score


class Model_finder:
    """
    this Class we'are going to use for finding the best model

    """

    def __init__(self, file_object, logger_object, x, y):
        self.logger = logger_object
        self.file_object = file_object
        self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(x, y, random_state=354)

    def get_best_model(self):
        self.logger.log(self.file_object, "Starting out for finding out best parameters for Random Forest")
        try:
            # Creating a Model wrt Random Forest
            self.rand_forrest = RandomForestRegressor(n_estimators=500, random_state=329)
            self.rand_forrest.fit(self.train_x, self.train_y)
            self.logger.log(self.file_object, "Random forest model has been successfully created")
            # finding out the accuracy
            pred_y_rf = self.rand_forrest.predict(self.test_x)
            print(f'lenghth of Test X{len(self.test_x)}')
            print(f'lenghth of Test X{len(self.test_x)}')
            self.r2_score_of_random_forest = r2_score(self.test_y, pred_y_rf)
            self.logger.log(self.file_object,
                            f"R2 value wrt random forest turn out to be {self.r2_score_of_random_forest} ")

            # Creating a model wrt Extra tree regressor
            self.extra_tree = ExtraTreesRegressor(n_estimators=500, random_state=329)
            self.extra_tree.fit(self.train_x, self.train_y)
            self.logger.log(self.file_object, "Extaa tree model has been successfully created")

            # finding out the R2 score wrt Extra tree regressor

            pred_y_et = self.extra_tree.predict(self.test_x)
            self.r2_score_of_extra_tree = r2_score(self.test_y, pred_y_et)
            self.logger.log(self.file_object,
                            f"R2 value wrt Extraa tree turn out to be {self.r2_score_of_extra_tree} ")
            if self.r2_score_of_extra_tree > self.r2_score_of_random_forest:
                self.logger.log(self.file_object, "Best model is Extra Tree")
                return 'Extra tree', self.extra_tree
            else:
                self.logger.log(self.file_object, "Best model is Random Forest")
                return "Random Forest", self.rand_forrest
        except Exception as e:
            self.logger.log(self.file_object,
                            "Something went wrong and model selection can't be successfully Executed"
                            "the error msg is:  " + str(e))
