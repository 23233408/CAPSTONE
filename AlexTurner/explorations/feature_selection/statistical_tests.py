from sklearn.feature_selection import SelectKBest, chi2, f_classif, mutual_info_classif

# Chi-Squared
chi_selector = SelectKBest(chi2, k=10)
X_kbest = chi_selector.fit_transform(X, y)

# ANOVA F-value
fvalue_selector = SelectKBest(f_classif, k=10)
X_kbest = fvalue_selector.fit_transform(X, y)

# Mutual Information
mi_selector = SelectKBest(mutual_info_classif, k=10)
X_kbest = mi_selector.fit_transform(X, y)

#Recursive Feature Elimination (RFE)

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

rfe = RFE(model, 10)
fit = rfe.fit(X, y)

# LASSO (L1 Regularization)

from sklearn.linear_model import LassoCV

lasso = LassoCV(cv=5).fit(X, y)
important_features = np.where(lasso.coef_ != 0)[0]

#Tree-based Methods

from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

# Random Forest
# Use the feature_importances_ attribute.
rf = RandomForestClassifier()
rf.fit(X, y)
important_features = rf.feature_importances_

# XGBoost
# Use the plot_importance function
xg_model = xgb.XGBClassifier()
xg_model.fit(X, y)
xgb.plot_importance(xg_model)


# Feature engineering
# Aggregated Features: Mean/Median/Max/Min values of vital signs over a period.



# Interaction Features: Ratios or differences between related features 
# ratio of white blood cell count to red blood cell count

