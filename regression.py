
import numpy
import matplotlib.pyplot as plt
from tqdm import tqdm

class Regression:
	def __init__(self, data_preparation_object, learning_rate, number_of_epochs):
		self.dataset_train_df = data_preparation_object.dataset_train_df
		self.dataset_test_df = data_preparation_object.dataset_test_df

		self.mean_dataset = data_preparation_object.mean_dataset
		self.std_dataset = data_preparation_object.std_dataset

		self.learning_rate = learning_rate
		self.number_of_epochs = number_of_epochs

		self.a = 0
		self.b = 0
		self.fit()


	def predict(self, x_value):
		return self.a * x_value + self.b

	def fit(self):
		x_train = self.dataset_train_df["temporal_index"]
		y_train = self.dataset_train_df["Sales"]

		x_test = self.dataset_test_df["temporal_index"]
		y_test = self.dataset_test_df["Sales"]

		train_length = len(self.dataset_train_df)
		for epoch in tqdm(range(self.number_of_epochs)):
			self.a -= 2*self.learning_rate/train_length * numpy.sum(x_train *(self.a*x_train + self.b - y_train))
			self.b -= 2*self.learning_rate/train_length * numpy.sum(self.a * x_train + self.b - y_train)

		y_train_predicted = self.predict(x_train)
		y_test_predicted = self.predict(x_test)

		plt.figure(figsize=(15, 6))
		plt.plot(x_train, y_train, "bo")
		plt.plot(x_train, y_train_predicted, "b")

		plt.plot(x_test, y_test, "ro")
		plt.plot(x_test, y_test_predicted, "r")
		plt.show()
