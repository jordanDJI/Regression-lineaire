import pandas
import matplotlib.pyplot as plt 
import numpy

class DataPreparation:
	def __init__(self, path_to_csv, x_column_name, y_column_name, percentage_split):
		self.dataset_df = pandas.read_csv(path_to_csv)
		self.x_column_name = x_column_name
		self.y_column_name = y_column_name
		self.percentage_split = percentage_split
		self.dataset_df[x_column_name] = pandas.to_datetime(self.dataset_df[x_column_name])
		self.prepare_data()


	def prepare_data(self):
		self.dataset_df["temporal_index"] = numpy.arange(0, len(self.dataset_df))
		self.correct_outliers_values()
		self.standard_normalize_data()
		self.split_data()


	def correct_outliers_values(self):
		"""
		This function is empty and user must work on it if necessary.
		The purpose of this function is to correct some outlier values.
		"""
		pass


	def standard_normalize_data(self):
		self.mean_dataset = self.dataset_df[self.y_column_name].mean()
		self.std_dataset = self.dataset_df[self.y_column_name].std()
		self.dataset_df[self.y_column_name] = (self.dataset_df[self.y_column_name] - self.mean_dataset) / self.std_dataset


	def split_data(self):
		index_split = int(self.percentage_split * len(self.dataset_df))
		self.dataset_train_df = self.dataset_df.iloc[ : index_split]
		self.dataset_test_df = self.dataset_df.iloc[index_split : ]
	

	def show_dataset(self):
		plt.figure(figsize=(15, 6))
		plt.plot(self.dataset_df[self.x_column_name], self.dataset_df[self.y_column_name])
		plt.show()