# %load q02_Max_important_feature/build.py
# Default imports
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data

# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')


# Write your code here
def Max_important_feature(data_set,target_variable='SalePrice',n=4):
    col=len(data_set.columns)-1
    return data_set.iloc[:,:col].apply(lambda x: x.corr(data_set.loc[:,target_variable])).abs().sort_values(ascending = False).head(n).index
    
Max_important_feature(data_set,'SalePrice',4)


