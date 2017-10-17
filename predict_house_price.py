
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

def get_data(file_name):
 data = pd.read_csv(file_name)  #here ,use pandas to read cvs file.
 X_parameter = []
 Y_parameter = []
 for single_square_feet ,single_price_value in zip(data['square_feet'],data['price']):#遍历数据，
       X_parameter.append([float(single_square_feet)])#存储在相应的list列表中
       Y_parameter.append(float(single_price_value))
 return X_parameter,Y_parameter
# print(get_data('input.csv'))


def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)  # train model
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(X_parameters,Y_parameters):
     # Create linear regression object
     regr = linear_model.LinearRegression()
     regr.fit(X_parameters, Y_parameters)
     plt.scatter(X_parameters,Y_parameters,color='blue')
     plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
     print(regr.score(X_parameters, Y_parameters))
     # plt.xticks(())
     # plt.yticks(())
     plt.show()


X_parameters,Y_parameters = get_data('input.csv')
print(linear_model_main(X_parameters,Y_parameters,700))
show_linear_line(X_parameters,Y_parameters)