# load libraries and modules - Amy
import pandas as pd
import numpy as np, warnings
from pathlib import Path
import os
from importlib import reload
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_validate, cross_val_score, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from sklearn.feature_selection import SelectFromModel


from sklearn.model_selection import train_test_split, cross_val_score,RandomizedSearchCV

from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight

# model comparison
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
#from xgboost import XGBClassifier
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.linear_model import SGDClassifier

# evaluation metrics
from sklearn.metrics import cohen_kappa_score,classification_report 
import shap


# compare model performance
def compare_models(X_train_scaled, y_train, candidate_models, class_weight_dict):

    # store model names
    model_names = []           
    model_average_scores = [] 
    # store the mean score of n-fold cross validation for each model

   
   # calculate mean scores using cross validation
    for model_name, model in candidate_models.items():
        scores = cross_val_score(model, X_train_scaled, y_train)
        model_names.append(model_name)
        model_average_scores.append(scores.mean())
        print(f'Scoring completed for {model_name}')
        
    # store mean scores for each model
    df_model = pd.DataFrame()
    df_model['model'] = model_names
    df_model['average_score'] = model_average_scores
        
    print(df_model)
    print(" ---------------------------------------- ")
        
    return(df_model)

def tune_hyperparameters(X_train_scaled, y_train, best_model_name):
    
    #todo: query the candidate_models var instead of using if else...
    
    
    param_grid = {
    'Logistic_Regression': {'C': [0.1, 1, 10],
                            'penalty': ['l1', 'l2']
                            },
    'Random_Forest': {'n_estimators': [50, 100, 150], 
                      'max_depth': [None, 10, 20], 
                      'min_leaf': list(range(2, 8)),
                      'min_samples_split': list(range(2,25)),
                      'min_samples_leaf': list(range(2,25))
                      },
    'Gradient_Boosting': {'n_estimators': [50, 100, 150, 200], 
                          'learning_rate': [0.01, 0.1, 0.2, 0.5], 
                          'loss': ['log_loss', 'exponential'], 
                          'criterion': ['friedman_mse', 'squared_error'],
                          'max_features': ['sqrt', 'log2']
                          }
    }
    
    # Create an empty dictionary to store the best parameters for each model
    best_params = {}

    # Loop through the candidate_models dictionary to perform GridSearchCV for each model
    for model_name, model in candidate_models.items():
        
        #todo:
        # gridSearchCV 
        # or
        # RandomizedSearchCV - refit=True
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid[model_name], cv=5)
        grid_search.fit(X, y)
        
        # Store the best parameters for the current model
        best_params[model_name] = grid_search.best_params_
        
        print(f"The best parameters for {model_name} are {grid_search.best_params_}")

        # gradient boosing has sample weights, not class weights
        # sample weight
        
        # have to calculate sample/class weight seperately for test and seperately for training
        
        
        gridcv.fit(X_train_scaled, y_train)
        print('Optimising complete')
        
        df_optimiser = pd.DataFrame(gridcv.cv_results_).dropna()
        hyper_df = df_optimiser[['param_loss', 'param_learning_rate', 'param_n_estimators', 'param_criterion', 'param_max_features', 'mean_test_score']]
        print(hyper_df) 
        print(" \n\n  ----------------------------------------  \n\n")
        
        # get best score
        best_score = gridcv.best_score_
        print(f"Best score for {best_model_name}: {best_score}")
        
        # Init dictionary of best params
        best_params = gridcv.best_params_   
        
        #todo: how to make this configurable? all models will use diff params...
        final_model = GradientBoostingClassifier(criterion=best_params['criterion'], 
                                            learning_rate=best_params['learning_rate'], loss=best_params['loss'], 
                                            max_features=best_params['max_features'], n_estimators=best_params['n_estimators'])
        

        hypertuned_model = final_model.fit(X_train_scaled, y_train)
        
        # return model object
        return(hypertuned_model)  

# %%
# Model Performance validation against test data

def validate_test_groundtruth(final_model,X_test_scaled,y_test):
    
    y_predicted = final_model.predict(X_test_scaled)

    print("\n\nFor test data generated using train test split \n")
    print(classification_report(y_test, y_predicted))

    print(" \n\n  ----------------------------------------  \n\n")

    print(f"cohen_kappa_score: {cohen_kappa_score(y_test,y_predicted)} ")

# %%
def load_expression(df_processed, test_size):
    """
    Preprocesses the dataframe by encoding the 'Sepsis' column and dropping unnecessary columns.
    Splits the data into training and test sets.
    Computes class weights for balancing the classes in the target variable.
    Normalises numerical features using MinMaxScaler.
    Compare performances of different models.
    Perform hyperparameter tuning on best model. 
    Validate the optimal model's performance on the test set.
    Generate predictions for unknown data using the optimal model.
    
    Parameters:
    - df_processed:
    - test_size: 
    
    
    Returns:
    - DataFrame 
    """
        
    optimal_model = {}  
    class_weight_dict = {} # Dictionary to store class weights
    
    df_train = df_processed 
         
    # Target and Predictors
    X = df_train.drop('IS_SEPSIS', axis='columns')
    y = df_train['IS_SEPSIS']
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=test_size, 
                                                        stratify=y, 
                                                        random_state=42)
    
    # Compute class weights
    class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
    
    # Dictionary containning class weights of target class labels
    for index, weight in enumerate(class_weights):
        class_weight_dict[index] = weight        
    
    
    # Normalise numeric columns, since features have different ranges 
    # In order to minimise data leakage during model testing the scalar is first fitted to train data and then 
    # used it to transform the test data      

    # Fit the scaler and transform the DataFrame
    df_standardised = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    
    # Standardising, not normalising
    scaler = StandardScaler()
    scaler_fit = scaler.fit(X_train) 
    X_train_scaled = scaler_fit.transform(X_train)  
    X_test_scaled = scaler_fit.transform(X_test)  
    

    # get model performances
    model_performance_df = compare_models(X_train_scaled, y_train, class_weight_dict)  
    
    # sort by model performance 
    sorted_model_performance_df = model_performance_df.sort_values(by=['average score'],ascending=False) 
    
    
    # find best performing model
    best_model_name = sorted_model_performance_df.head(1)['model'].to_string().split(" ")[4]
    print("\n\n The best Performing model :", best_model_name)
    
    # tune hyperparameters
    tuned_model = tune_hyperparameters(X_train_scaled, y_train, best_model_name)
        
    # Model performance for test data generated using train test split
    
    # To print classification report and cohen_kappa_score    
    performance_report = validate_test_groundtruth(optimal_model,X_test_scaled,y_test) 
    
    # Generating the dataframe with predicted values
    generate_test_df = validate_test_unknown(optimal_model,scaler_fit)

# %%
# init the parameters
test_size = 0.2

candidate_models = {
    'Logistic_Regression': LogisticRegression(max_iter=10000000000, class_weight=class_weight_dict),
    'Random_Forest': RandomForestClassifier(class_weight=class_weight_dict),
    'Gradient_Boosting': GradientBoostingClassifier()
    
    # todo: are these valid?
    # 'SGD_Classifier': SGDClassifier(class_weight=class_weight_dict),
    # 'XGB': XGBClassifier(),
    # 'KNeighbors': KNeighborsClassifier(),
    # 'Adaboost':AdaBoostClassifier()
    }

load_expression(df_processed, test_size, candidate_models)


