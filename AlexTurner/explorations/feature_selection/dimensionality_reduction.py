# Dimensionality Reduction

# PCA (Principal Component Analysis)
from sklearn.decomposition import PCA
import numpy as np


random_state=42



# split to X & Y
y = 'IS_SEPSIS'


# Initialize PCA and the X vector for dimensionality reduction
pca = PCA(n_components=5)

# Fit and transform the data
X_pca = pca.fit_transform(X)

# Explained variance
print("Explained Variance: ", pca.explained_variance_ratio_)




# Choosing number of components
# Plot the explained variance to choose an optimal number of components.

import matplotlib.pyplot as plt

# Fit PCA without reducing dimensionality
pca = PCA().fit(X)

# Plot the explained variances
plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Variance (%)')
plt.title('Explained Variance')
plt.show()


#t-SNE (t-Distributed Stochastic Neighbor Embedding)

#large set of correlated features.
# Cross-Validation loop required to avoid data leakage


# Apply PCA
# Initialize PCA
pca = PCA()

# Fit PCA
pca.fit(X_scaled)

# Plot explained variance
plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Variance (%)')
plt.title('Explained Variance')
plt.show()



# Transform Data and train model
# Apply PCA with selected number of components
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Initialize and train classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Evaluate the model
score = clf.score(X_test, y_test)
print("Classification Score: ", score)