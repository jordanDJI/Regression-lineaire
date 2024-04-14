import data_preparation
import regression

path_to_csv = "../vente_maillots_de_bain.csv"
x_column_name, y_column_name = "Years", "Sales"
percentage_split = 0.8


# fitting settings
learning_rate = 10**(-5)
number_of_epochs = 100_000

data_preparation_object = data_preparation.DataPreparation(path_to_csv, x_column_name, y_column_name, percentage_split)
regression_object = regression.Regression(data_preparation_object, learning_rate, number_of_epochs)