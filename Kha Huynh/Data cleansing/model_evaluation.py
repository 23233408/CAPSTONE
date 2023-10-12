import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import mean_squared_error, confusion_matrix, roc_auc_score, precision_score, recall_score, f1_score, auc, make_scorer
from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve, balanced_accuracy_score

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
def plot_roc_curve(fpr, tpr, label = None):
    plt.plot(fpr, tpr, linewidth=2, label = label)
    plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate (Fall-Out)', fontsize=11)
    plt.ylabel('True Positive Rate (Recall)', fontsize=11)
    plt.grid(True)

def plot_auc_roc_curve(model, x_test, y_test):
  # Predict the test set using the best random forest regressor
  y_pred = model.predict(x_test)

  # Plotting ROC curve
  fpr_rf_test, tpr_rf_test, thresholds_roc_rf_test = roc_curve(np.argmax(y_test, axis=1), y_pred[:, 1], pos_label=1)
  # fpr_rf_test, tpr_rf_test, thresholds_roc_rf_test = roc_curve(y_test, y_pred, pos_label=1)
  auc_t0_rf = auc(fpr_rf_test, tpr_rf_test)
  print("AUC = {:.4f}".format(auc_t0_rf))

  plt.figure(figsize=(6, 6))
  plot_roc_curve(fpr_rf_test, tpr_rf_test)
  plt.title("ROC Curve - LSTM")
  plt.grid(False)
  plt.show()

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