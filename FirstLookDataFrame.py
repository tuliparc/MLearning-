# importing DataFrames Lib - Pandas
import pandas as pd
# Decision Tree Model
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

