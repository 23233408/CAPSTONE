import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import mean_squared_error, confusion_matrix, roc_auc_score, precision_score, recall_score, f1_score, auc, make_scorer
from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve, balanced_accuracy_score
import scipy.stats as stats

def get_class_weights(y_train_df):
  label_counts = y_train_df.value_counts()
  label_proportions = label_counts / len(y_train_df)*100
  # Calculate class weights
  class_weights = {0: 1 / (label_proportions[0] / 100), 1: 1 / (label_proportions[1] / 100)}

  # Round the class weights to the desired precision (optional)
  class_weights = {key: round(weight, 4) for key, weight in class_weights.items()}
  return class_weights

def compute_sample_weights(y):
  class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)
  sample_weights = class_weights[y]
  return sample_weights

# Plotting ROC curve to determine the threshold
def __plot_roc_curve(fpr, tpr, label = None):
  plt.plot(fpr, tpr, linewidth=2, label = label)
  plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
  plt.axis([0, 1, 0, 1])
  plt.xlabel('False Positive Rate (Fall-Out)', fontsize=11)
  plt.ylabel('True Positive Rate (Recall)', fontsize=11)

def plot_auc_roc_curve(model, x_test, y_test):
  # Predict the test set using the best random forest regressor
  y_pred = model.predict(x_test)

  # Plotting ROC curve
  fpr_rf_test, tpr_rf_test, thresholds_roc_rf_test = roc_curve(np.argmax(y_test, axis=1), y_pred[:, 1], pos_label=1)
  # fpr_rf_test, tpr_rf_test, thresholds_roc_rf_test = roc_curve(y_test, y_pred, pos_label=1)
  auc_t0_rf = auc(fpr_rf_test, tpr_rf_test)
  print("AUC = {:.4f}".format(auc_t0_rf))

  # plt.figure(figsize=(6, 6))
  __plot_roc_curve(fpr_rf_test, tpr_rf_test)
  plt.title("ROC Curve - LSTM")
  plt.grid(False)
  plt.show()

def plot_combined_roc_curves(models, x_train, y_train, x_test, y_test):
  y_train = np.argmax(y_train, axis=1)
  y_test = np.argmax(y_test, axis=1)
  plt.figure(figsize=(6, 6))
  row_list = []
  # Predict the test set using the best random forest regressor
  for i, (model_name, model) in enumerate(models.items()):
    preds_train = model.predict(x_train)
    preds_test = model.predict(x_test)
    # Plotting ROC curve
    fpr, tpr, thresholds_roc_rf_test = roc_curve(y_test, preds_test[:, 1], pos_label=1)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, linewidth=2, label = f'{model_name} (AUC = {roc_auc:.3f})')

    # Computing f1 and acc
    f1_train = f1_score(y_train, np.argmax(preds_train, axis=1))
    f1_test = f1_score(y_test, np.argmax(preds_test, axis=1))
    acc_train = balanced_accuracy_score(y_train, np.argmax(preds_train, axis=1))
    acc_test = balanced_accuracy_score(y_test, np.argmax(preds_test, axis=1))
    # Computing precision and recall
    precision_train = precision_score(y_train, np.argmax(preds_train, axis=1))
    precision_test = precision_score(y_test, np.argmax(preds_test, axis=1))
    recall_train = recall_score(y_train, np.argmax(preds_train, axis=1))
    recall_test = recall_score(y_test, np.argmax(preds_test, axis=1))
    
    new_row = [model_name, round(acc_train, 3), round(acc_test, 3),
                round(precision_train, 3), round(precision_test, 3),
                round(recall_train, 3), round(recall_test, 3),
                round(f1_train, 3), round(f1_test, 3),
                round(roc_auc, 3)]
    row_list.append(new_row)
  
  plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
  plt.axis([0, 1, 0, 1])
  plt.xlabel('False Positive Rate', fontsize=11)
  plt.ylabel('True Positive Rate', fontsize=11)
  plt.legend(loc='lower right')
  plt.title("ROC Curve")
  plt.grid(False)
  plt.show()
  table = pd.DataFrame(row_list, columns= ['Model', 'Balanced acc Train', 'Balanced acc Test',
                                         'Precision Train', 'Precision Test',
                                         'Recall Train', 'Recall Test',
                                         'F1 Train', 'F1 Test', 'AUC'])
  return table

def plot_combined_roc_curves_t(models, split_data_dict, top_features, time_windows):
  plt.figure(figsize=(6, 6))
  row_list = []
  # Predict the test set using the best random forest regressor
  for top in top_features:
    for time in time_windows:
      model = models[top][time]
      x_train = split_data_dict[(top, time)]['x_train']
      y_train = split_data_dict[(top, time)]['y_train']
      x_test = split_data_dict[(top, time)]['x_test']
      y_test = split_data_dict[(top, time)]['y_test']
      
      y_train = np.argmax(y_train, axis=1)
      y_test = np.argmax(y_test, axis=1)

      preds_train = model.predict(x_train)
      preds_test = model.predict(x_test)
      # Plotting ROC curve
      fpr, tpr, thresholds_roc_rf_test = roc_curve(y_test, preds_test[:, 1], pos_label=1)
      roc_auc = auc(fpr, tpr)
      plt.plot(fpr, tpr, linewidth=2, label = f'{time} (AUC = {roc_auc:.3f})')

      # Computing f1 and acc
      f1_train = f1_score(y_train, np.argmax(preds_train, axis=1))
      f1_test = f1_score(y_test, np.argmax(preds_test, axis=1))
      acc_train = balanced_accuracy_score(y_train, np.argmax(preds_train, axis=1))
      acc_test = balanced_accuracy_score(y_test, np.argmax(preds_test, axis=1))
      # Computing precision and recall
      precision_train = precision_score(y_train, np.argmax(preds_train, axis=1))
      precision_test = precision_score(y_test, np.argmax(preds_test, axis=1))
      recall_train = recall_score(y_train, np.argmax(preds_train, axis=1))
      recall_test = recall_score(y_test, np.argmax(preds_test, axis=1))
      
      new_row = [time, round(acc_train, 3), round(acc_test, 3),
                  round(precision_train, 3), round(precision_test, 3),
                  round(recall_train, 3), round(recall_test, 3),
                  round(f1_train, 3), round(f1_test, 3),
                  round(roc_auc, 3)]
      row_list.append(new_row)
  
  plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
  plt.axis([0, 1, 0, 1])
  plt.xlabel('False Positive Rate', fontsize=11)
  plt.ylabel('True Positive Rate', fontsize=11)
  plt.legend(loc='lower right')
  plt.title("ROC Curve")
  plt.grid(False)
  plt.show()
  table = pd.DataFrame(row_list, columns= ['Model', 'Balanced acc Train', 'Balanced acc Test',
                                         'Precision Train', 'Precision Test',
                                         'Recall Train', 'Recall Test',
                                         'F1 Train', 'F1 Test', 'AUC'])
  test_table = __get_test_performance(table)
  return table, test_table

def __get_test_performance(table):
  table = table[['Model', 'Balanced acc Test',
                                         'Precision Test',
                                         'Recall Test',
                                         'F1 Test', 'AUC']]
  table = table.T
  table.columns = table.iloc[0]
  table = table[1:]
  return table

def print_results(M, X_train, Y_train, X_test, Y_test):
  Y_train = np.argmax(Y_train, axis=1)
  Y_test = np.argmax(Y_test, axis=1)

  preds_train = M.predict(X_train)
  preds_train = np.argmax(preds_train, axis=1)
  conf_mat_train = confusion_matrix(Y_train, preds_train)
  # conf_mat = conf_mat.astype('float') / conf_mat.sum(axis=1)[:, np.newaxis]

  preds_test = M.predict(X_test)
  preds_test = np.argmax(preds_test, axis=1)
  conf_mat_test = confusion_matrix(Y_test, preds_test)
  # conf_mat = conf_mat.astype('float') / conf_mat.sum(axis=1)[:, np.newaxis]

  print("***[RESULT]*** ACT  Confusion Matrix")
  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,4))

  x_labels = ["Predicted\nNon-Sepsis", "Predicted\nSepsis"]
  y_labels = ["Actual Non-Sepsis", "Actual Sepsis"]
  sns.heatmap(conf_mat_train, fmt='d', annot=True, xticklabels=x_labels, yticklabels=y_labels, ax=axes[0])
  sns.heatmap(conf_mat_test, fmt='d', annot=True, xticklabels=x_labels, yticklabels=y_labels, ax=axes[1])

  axes[0].set_title("CM in training set", fontsize = 10)
  axes[1].set_title("CM in test set", fontsize = 10)
  axes[0].tick_params(labelsize=9)
  axes[1].tick_params(labelsize=9)
  plt.tight_layout()
  plt.show()

  f1_train = f1_score(Y_train, preds_train)
  f1_test = f1_score(Y_test, preds_test)
  acc_train = balanced_accuracy_score(Y_train, preds_train)
  acc_test = balanced_accuracy_score(Y_test, preds_test)
  # Computing precision and recall
  precision_train = precision_score(Y_train, preds_train)
  precision_test = precision_score(Y_test, preds_test)
  recall_train = recall_score(Y_train, preds_train)
  recall_test = recall_score(Y_test, preds_test)
  # table = pd.DataFrame({'F1-Score':[f1_train, f1_test], 'Balanced Acc':[acc_train, acc_test],
  #                      'Precision':[precision_train, precision_test], 'Recall':[recall_train, recall_test]},
  #                      index=['Train', 'Test'])

  table = pd.DataFrame({'Train':[acc_train, precision_train, recall_train, f1_train], 'Test':[acc_test, precision_test, recall_test, f1_test]},
                        index=['Balanced Acc', 'Precision', 'Recall', 'F1-Score'])
  print(table)

def calculate_mean_conf(m_hist, measure):
  # Calculate mean and confidence intervals for training loss
  train_losses = [hist.history[measure] for hist in m_hist]
  max_len = max(len(loss) for loss in train_losses)

  # Pad the sublists with NaN values to match the maximum length
  train_losses = [loss + [np.nan] * (max_len - len(loss)) for loss in train_losses]
  mean_train_loss = np.nanmean(train_losses, axis=0)

  std_train_loss = np.nanstd(train_losses, axis=0)
  confidence_interval = 0.95  # Adjust this value as needed

  # Calculate margin of error
  margin_of_error = stats.t.ppf((1 + confidence_interval) / 2, max_len - 1) * (std_train_loss / np.sqrt(max_len))

  # Calculate confidence intervals
  lower_bound_train_loss = mean_train_loss - margin_of_error
  upper_bound_train_loss = mean_train_loss + margin_of_error

  # Similarly, calculate mean and confidence intervals for validation loss
  val_losses = [hist.history[f'val_{measure}'] for hist in m_hist]

  # Pad the sublists with NaN values to match the maximum length
  val_losses = [loss + [np.nan] * (max_len - len(loss)) for loss in val_losses]
  mean_val_loss = np.nanmean(val_losses, axis=0)
  std_val_loss = np.nanstd(val_losses, axis=0)
  margin_of_error_val = stats.t.ppf((1 + confidence_interval) / 2, max_len - 1) * (std_val_loss / np.sqrt(max_len))
  lower_bound_val_loss = mean_val_loss - margin_of_error_val
  upper_bound_val_loss = mean_val_loss + margin_of_error_val

  # Create plots
  # plt.figure(figsize=(10, 5))

  # Training loss
  # plt.subplot(1, 2, 1)
  plt.plot(mean_train_loss, label=f'mean train {measure}', color='blue')
  # plt.fill_between(range(max_len), lower_bound_train_loss, upper_bound_train_loss, color='lightblue', alpha=0.5)
  # plt.title(f'Model {measure}')
  # plt.xlabel('epochs')
  # plt.ylabel(measure)

  # Validation loss
  # plt.subplot(1, 2, 2)
  plt.plot(mean_val_loss, label=f'mean val {measure}', color='red')
  plt.fill_between(range(max_len), lower_bound_val_loss, upper_bound_val_loss, color='lightcoral', alpha=0.5)
  plt.title(f'Model {measure}')
  plt.xlabel('epochs')
  plt.ylabel(measure)
  plt.legend(loc='lower right')
  plt.show()

def __cal_mean(max_len, m_hist, measure):
  # Calculate mean and confidence intervals for training loss
  hist_list = [hist.history[measure] for hist in m_hist]

  # Pad the sublists with NaN values to match the maximum length
  hist_list = [one_list + [np.nan] * (max_len - len(one_list)) for one_list in hist_list]
  mean_measure = np.nanmean(hist_list, axis=0)

  std_measure = np.nanstd(hist_list, axis=0)
  confidence_interval = 0.95  # Adjust this value as needed

  # Calculate margin of error
  margin_of_error = stats.t.ppf((1 + confidence_interval) / 2, max_len - 1) * (std_measure / np.sqrt(max_len))

  # Calculate confidence intervals
  lower_bound_measure = mean_measure - margin_of_error
  upper_bound_measure = mean_measure + margin_of_error
  
  return mean_measure, lower_bound_measure, upper_bound_measure

def cal_model_mean(m_hist, kfold, measure_list):
  result = []
  max_len = max(len(one_list.history[measure_list[0]]) for one_list in m_hist)
  model_no = int(len(m_hist) / kfold)
  for i in range(0, model_no):
    model_result = []
    hist_list = m_hist[i*model_no : i*model_no+model_no]
    for measure in measure_list:
      mean_measure, lower_bound_measure, upper_bound_measure = __cal_mean(max_len, hist_list, measure)
      model_result.append(mean_measure)
    result.append(model_result)
  return result
