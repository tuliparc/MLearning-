# importing DataFrames Lib - Pandas
import pandas as pd
# Decision Tree Model
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

# Definindo Target(y) e Features(X)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Import the train_test_split function 
from sklearn.model_selection import train_test_split
# Spliting DataSet( X e y ) into training (train_) and Validating(val_) Sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Specify Model
name_model = DecisionTreeRegressor(random_state=1)   #(random_state=num_inteiro)
# Fit Model
name_model.fit(train_X, train_y)

# Predict with all validation observations
val_predictions = name_model.predict(val_X)  #para parte do DataFrame, val_X.head() por exemplo. 
#print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

# print the top few validation predictions
print(iowa_model.predict(val_X.head()))
# print the top few actual prices from validation data
print(val_y.head().tolist())

print(mean_absolute_error(val_y, val_predictions))

# Make validation predictions and calculate mean absolute error
val_predictions = name_model.predict(val_X)
#print(mean_absolute_error(val_y, val_predictions))
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

#===== iteração 1 =============
candidate_max_leaf_nodes = [5, 25, 50, 100, 500, 600]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
best_leaf_nodes_value = 0
min_mae = 100000
for max_leaf_nodes in candidate_max_leaf_nodes:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
    if my_mae < min_mae: 
        best_leaf_nodes_value = max_leaf_nodes 
        min_mae = my_mae
# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = best_leaf_nodes_value

#===== iteração 2 =============
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)

R
