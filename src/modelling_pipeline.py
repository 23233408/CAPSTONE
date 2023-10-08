# load libraries and modules
import pandas as pd
import numpy as np, warnings
from pathlib import Path
import os
from importlib import reload

# visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# data processing
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_validate, cross_val_score, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from sklearn.feature_selection import SelectFromModel

# model comparison
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier

# Evaluation metrics
from sklearn.metrics import cohen_kappa_score,classification_report 
from sklearn.metrics import mean_squared_error, confusion_matrix, roc_auc_score, precision_score, recall_score, f1_score, auc, make_scorer
from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve, balanced_accuracy_score, PrecisionRecallDisplay
import shap

class ModelPipeline:

  # Init the parameters
  ROOT_DIR = Path('')
  


  ROOT_DIR = Path('../..')
    
  def __init__(self, ROOT_DIR):
    self.ROOT_DIR = ROOT_DIR

  def get_dfs(ROOT_DIR, tops, date):
      dfs_dict = {}
      for top in tops:
          dfs_dict[f"top{top}"] = get_model_input_dfs(ROOT_DIR, f'top{top}', date)
      return dfs_dict


  def get_full_dfs(ROOT_DIR, tops, date):
      dfs_dict = {}
      for top in tops:
          dfs_dict[f"top{top}"] = get_model_full_dfs(ROOT_DIR, f'top{top}', date)
      return dfs_dict


  def get_model_input_dfs(ROOT_DIR, top, version, timepoints=['t0', 't1', 't2', 't3', 't4']):
      
      """
      Function to read the model input dataframes based on provided prefixes and date string.
      
      Parameters:
      - ROOT_DIR: The root directory path.
      - prefix: The prefix (e.g. 'top20', 'top30', etc.)
      - date_str: The date string in the filename (e.g. '20231005').
      - timepoints: A list of timepoints (default is ['t0', 't1', 't2', 't3', 't4']).
      
      Returns:
      - A dictionary with keys as timepoints and values as the corresponding dataframes.
      """
      
      dfs = {}
      for tp in timepoints:
          path = ROOT_DIR / 'data' / 'Model input data' / f"{tp}_{top}_{version}.csv"
          dfs[tp] = get_model_input_df(path)
      
      return dfs


  def get_model_full_dfs(ROOT_DIR, top, version, timepoints=['t0', 't1', 't2', 't3', 't4']):
      
      """
      Function to read the model input dataframes based on provided prefixes and date string.
      
      Parameters:
      - ROOT_DIR: The root directory path.
      - prefix: The prefix (e.g. 'top20', 'top30', etc.)
      - date_str: The date string in the filename (e.g. '20231005').
      - timepoints: A list of timepoints (default is ['t0', 't1', 't2', 't3', 't4']).
      
      Returns:
      - A dictionary with keys as timepoints and values as the corresponding dataframes.
      """
      
      dfs = {}
      for tp in timepoints:
          path = ROOT_DIR / 'data' / 'Model input data' / f"{tp}_{top}_{version}.csv"
          dfs[tp] = get_model_input_df(path)
      
      return dfs


  def get_model_input_df(model_input_path):
    """_summary_
    
    Args:
        model_input_path (_type_): Processed csv file path.
    """
    model_input_df = pd.read_csv(model_input_path)
    model_input_df = model_input_df.drop(columns=["SUBJECT_ID", "HADM_ID"])
    return model_input_df


  def count_missing_values(time_df):
    """
    Get count of missing values.
    
    Args:
        time_df (_type_): Processed csv file path.
    """
    for time_point, df in time_df.items():
        df_without_target = df.drop(columns=['IS_SEPSIS'])
        total_values = df_without_target.size
        count_999 = (df_without_target == -999).sum().sum()
        missing_proportions = count_999 / total_values *100
        print(f"Number of missing values in {time_point}: {count_999} ({missing_proportions:.2f}%)")


  def count_missing_SOFA(time_df):
      for time_point, df in time_df.items():
          total_SOFA = df.shape[0]
          count_SOFA_999 = (df['SOFA'] == -999).sum().sum()
          missing_SOFA_proportions = count_SOFA_999 / total_SOFA *100
          print(f"Number of missing SOFA in {time_point}: {count_SOFA_999} ({missing_SOFA_proportions:.2f}%)")


  def split_data(df_train):
      """
      Split data into training and test sets.
      Standardise numerical features.
      
      Compare performances of different models.
      Perform hyperparameter tuning on best model.
      Validate the optimal model's performance on the test set.
      Generate predictions for unknown data using the optimal model.
      
      Parameters:
      - df_train: Processed data for model training
      - test_size: 
      
      Returns:
      - X train, X test, y train, y test 
      """
          
      # Target and Predictors
      X = df_train.drop('IS_SEPSIS', axis='columns')
      y = df_train['IS_SEPSIS']
      
      # Split into train and test sets
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
      
      # Fit the scaler and transform the X train and test sets
      # Standardising (not normalising!)
      scaler = StandardScaler()

      X_train = scaler.fit_transform(X_train)
      X_test = scaler.transform(X_test)
      
      return X_train, X_test, y_train, y_test


  def get_class_weights(y_train):
    """
        Compute class weights for balancing the classes in the target variable.

    Args:
        y_train (_type_)

    Returns:
        class_weights (dict)
    """
    # Get sepsis label proportions
    label_counts = y_train.value_counts()
    label_proportions = label_counts / len(y_train)*100
      
    # Compute class weights
    class_weights = {0: 1 / (label_proportions[0] / 100), 1: 1 / (label_proportions[1] / 100)}

    # Round the class weights to the desired precision (optional)
    class_weights = {key: round(weight, 4) for key, weight in class_weights.items()}
    
    return class_weights


  # 2. Modeling Fitting



  def static_models(candidate_models, class_weights, X_train, y_train, X_test, y_test, time):
      '''
      Fit static models.
      
      Returns:
          pd.DataFrame: A DataFrame containing model names and their average cross-validation scores.
      
      '''
      
      model_names = list(candidate_models.keys())
      
      performance_df = pd.DataFrame(columns=['Model', 'Balanced_Acc_Train', 'Balanced_Acc_Test', 'Precision_Train', 'Precision_Test', 'Recall_Train', 'Recall_Test', 'F1_Train', 'F1_Test'])

      for model_name, model in candidate_models.items():

          y_pred_train, y_pred_test = fit_models(model, model_name, class_weights, X_train, y_train, X_test)

          performance_scores = get_performance_scores(model, model_name, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test)

          formatted_model_name = f"{model_name}_{time}"
          new_row = pd.DataFrame([[formatted_model_name] + performance_scores], columns=performance_df.columns)

          performance_df = pd.concat([performance_df, new_row], ignore_index=True)

          predicted_probabilities = model.predict_proba(X_test)

      return performance_df


  def cv_analysis(X_train, y_train, candidate_models, class_weights):
      """
      Perform cross-validation analysis on a set of candidate models and return their mean scores.

      Args:
          X_train (pd.DataFrame): Scaled feature matrix for training.
          y_train (pd.Series): Target labels for training.
          candidate_models (Dict[str, Any]): A dictionary of static ML model names and their respective instantiated models.
          class_weights (Dict[int, float]): A dictionary of class weights for handling sepsis class imbalance.
          
      Returns:
          pd.DataFrame: A DataFrame containing model names and their average cross-validation scores.
      """
      
      model_names = []
      model_average_scores = [] 
    
    # Calculate mean scores using cross validation
      for model_name, model in candidate_models.items():
          scores = cross_val_score(model, X_train, y_train)
          model_names.append(model_name)
          model_average_scores.append(scores.mean())
          
      # Store mean scores for each model
      df_model = pd.DataFrame({
          'model': model_names,
          'average_score': model_average_scores
      })
      
      return(df_model)

  def fit_models(model, model_name, class_weights, X_train, y_train, X_test):
    """_summary_
    Model training function (inside models_fitting)
    
    Args:
        model (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    if model_name == 'Gradient_Boost':
      model.fit(X_train, y_train, sample_weight=[class_weights[label] for label in y_train])
    else:
      model.fit(X_train, y_train)

    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    return y_pred_train, y_pred_test



  def get_performance_scores(model, model_name, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test):
    """
    Get performance measures on (i) ballanced accuracy (ii) precision, (iii) recall and (iv) F1 score.
    
    Called by models_fitting()
    
    Args:
        model (_type_): _description_
        X_train (_type_): Scaled X_train
        X_test (_type_): Scaled X_train
        y_train (_type_): _description_
        y_test (_type_): _description_
    
    Returns:
    """

    # Computing balanced accuracy
    balanced_acc_train = balanced_accuracy_score(y_train, y_pred_train)
    balanced_acc_test = balanced_accuracy_score(y_test, y_pred_test)

    # Computing precision and recall
    precision_train = precision_score(y_train, y_pred_train)
    precision_test = precision_score(y_test, y_pred_test)
    recall_train = recall_score(y_train, y_pred_train)
    recall_test = recall_score(y_test, y_pred_test)

    # Computing F1 score
    f1_train = f1_score(y_train, y_pred_train)
    f1_test = f1_score(y_test, y_pred_test)

    # Format scores
    performance_scores = [balanced_acc_train, balanced_acc_test, precision_train, precision_test, recall_train, recall_test, f1_train, f1_test]
    
    
    # formatted_performance_scores = []
    # for i in range(len(performance_scores)):
    #   s = '({i:.4f})'.format(performance_scores[i])
    #   formatted_performance_scores.append(s)
    
    # return formatted_performance_scores
    return performance_scores


  def plot_results(candidate_models, class_weights, X_train, X_test, y_train, y_test):
    """
    Get model plots.
    
    Args:
        candidate_models (dict): _description_
        X_train (_type_): Scaled X_train
        X_test (_type_): Scaled X_train
        y_train (_type_): Scaled Y_test
        y_test (_type_): Scaled Y_test
    
    Returns:
    """

    for model_name, model in candidate_models.items():

      y_pred_train, y_pred_test = fit_models(model, model_name, class_weights, X_train, y_train, X_test)
      predicted_probabilities = model.predict_proba(X_test)

      plot_confusion_matrix(model, model_name, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test)
      plot_precision_recall(model, model_name, X_test, y_test)
      plot_roc_curve(predicted_probabilities, model_name, y_test, label = None)


  def plot_combined_roc_curves(candidate_models, X_test, y_test, title='ROC Curves'):
      """
      Plot the ROC curve for the candidate models.
      

      """

      # Initialise the plot
      plt.figure(figsize=(6, 6))
      
      # Iterate over classifiers and plot ROC curve for each
      for model_name, model in candidate_models.items():
          # Predict the probabilities of the positive class
          y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else model.decision_function(X_test)
          
          # Compute ROC curve and AUC
          fpr, tpr, _ = roc_curve(y_test, y_prob)
          roc_auc = auc(fpr, tpr)
          
          # Plot ROC curve
          plt.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc:.2f})')
      
      # Plot the random classifier
      plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Random Classifier (AUC = 0.50)')
      
      # Customize the plot
      plt.xlabel('False Positive Rate')
      plt.ylabel('True Positive Rate')
      plt.title(title)
      plt.legend(loc='lower right')
      
      # Show the plot
      plt.show()


  def plot_confusion_matrix(model, model_name, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test):
    '''
    Called by plot_results()
    '''
    
    # Computating the confusion matrix
    cm_train = confusion_matrix(y_train, y_pred_train)
    cm_test = confusion_matrix(y_test, y_pred_test)    

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,4))
    
    x_labels = ["Predicted\nNon-Sepsis", "Predicted\nSepsis"]
    y_labels = ["Actual Non-Sepsis", "Actual Sepsis"]
    sns.heatmap(cm_train, annot=True, fmt='d', xticklabels=x_labels, yticklabels=y_labels, ax=axes[0])
    sns.heatmap(cm_test, annot=True, fmt='d', xticklabels=x_labels, yticklabels=y_labels, ax=axes[1])
    
    axes[0].set_title("CM in training set", fontsize = 10)
    axes[1].set_title("CM in test set", fontsize = 10)
    axes[0].tick_params(labelsize=9)
    axes[1].tick_params(labelsize=9)
    plt.tight_layout()
    
    print(model_name)
    print(" ---------------------------------------- ")
    plt.show()


  def plot_precision_recall(model, model_name, X_test, y_test):
    # Plot precision recall
    display = PrecisionRecallDisplay.from_estimator(
      model, X_test, y_test, name=model_name, plot_chance_level=True
    )
    display.ax_.legend(loc='upper right')
    _ = display.ax_.set_title("2-class Precision-Recall curve")

    fig = display.figure_
    plt.show()


  def plot_roc_curve(predicted_probabilities, model_name, y_test, label = None):
    """_summary_
    returns AUC score, ROC curve, precision recall

    Args:
        fpr_test (array): _description_
        tpr_test (array): _description_
        model_name (str): Model name
        label (_type_, optional): _description_. Defaults to None.
    """
    # Plotting ROC curve
    fpr, tpr, thresholds_roc_test = roc_curve(y_test, predicted_probabilities[:, 1], pos_label=1)

    # Compute AUC score
    auc_test = auc(fpr, tpr)
    print(f"{model_name} AUC : {auc_test:.4f}")
    
    # Plot ROC curve
    plt.plot(fpr, tpr, linewidth=2, label = label, color='orange')
    plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
    plt.axis([0, 1, 0, 1])                                    
    plt.xlabel('False Positive Rate (Fall-Out)', fontsize=11) 
    plt.ylabel('True Positive Rate (Recall)', fontsize=11)
    plt.grid(False)  
    
    plt.title("ROC Curve: " + model_name)
    plt.figure(figsize=(6, 6))
    plt.show()

  #  fig = plt.gcf()
  #  plt.close(fig)

  #  return fig

  # %% [markdown]
  # # 3. Tuning Hyperparameters

  # %%
  def tune_hyperparameters(X_train, y_train, class_weights, candidate_models):
      """    
      Tune hyperparameters for multiple classifiers using GridSearchCV.

      Args:
          X_train (pd.DataFrame or np.array): Feature matrix for training.
          y_train (pd.Series or np.array): Target labels for training.
          class_weights (dict): Class weights for handling class imbalance.
          candidate_models:

      Returns:
          dict: Best parameters for each classifier.
      """  

      # define hyperparameter grid
      param_grid = {
          'Logistic_Regression': {'C': [0.1, 1, 10],
                                  'penalty': ['l2', None]
                              },
          'Random_Forest': {'n_estimators': [50, 100, 150], 
                        'max_depth': [None, 10, 20], 
                          'min_samples_split': [2, 25, 50, 100, 250],
                        'min_samples_leaf': [2, 25, 50, 100, 250]
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
          
          #todo: gridSearchCV or RandomizedSearchCV using refit=True?
          grid_search = GridSearchCV(estimator=model, param_grid=param_grid[model_name], scoring='balanced_accuracy', cv=3)
          
          if model_name == 'Gradient_Boost':
              grid_search.fit(X_train, y_train, sample_weight=[class_weights[label] for label in y_train])
          else:
              grid_search.fit(X_train, y_train)
          
          
          # Store the best parameters for the current model
          best_params[model_name] = grid_search.best_params_
          best_models[model_name] = grid_search.best_estimator_
                  
          # Get best score
          best_score = grid_search.best_score_
          print(f"Best score for {model_name}: {best_score}")
          print(grid_search.best_params_)
          

          # hypertuned_model = final_model.fit(X_train, y_train)
          
      return best_params
          #return(hypertuned_model)  

  # %%
  def train_models(X_train, X_test, y_train, y_test):
      
      # Get model performances
      model_performance_df = static_models(candidate_models, class_weights, X_train, y_train, X_test, y_test)
      
      # sort by model performance 
      sorted_model_performance_df = model_performance_df.sort_values(by=['average score'],ascending=False) 
      
      # find best performing model
      best_model_name = sorted_model_performance_df.head(1)['model'].to_string().split(" ")[4]
      print("\n\n The best Performing model :", best_model_name)
      
      # tune hyperparameters of best performing model
      tuned_model = tune_hyperparameters(X_train_scaled, y_train, best_model_name)
          
      # Model performance for test data generated using train test split
      
      # To print classification report and cohen_kappa_score    
      # performance_report = validate_test_groundtruth(tuned_model,X_test_scaled,y_test) 

  # %% [markdown]
  # # 4. Final Models

  # %%
  def validate_test_groundtruth(final_model, X_test_scaled, y_test):
      """
      Model Performance validation against test data

      Args:
          final_model (_type_): _description_
          X_test_scaled (_type_): _description_
          y_test (_type_): _description_
      """
          
      y_predicted = final_model.predict(X_test_scaled)

      print("\n\nFor test data generated using train test split \n")
      print(classification_report(y_test, y_predicted))


      print(f"Cohen_kappa_score: {cohen_kappa_score(y_test, y_predicted)} ")


