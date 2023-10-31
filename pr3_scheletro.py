## no dataset considered
###STANDARDIZATION
from sklearn.preprocessing import StandardScaler
import pandas as pd

scaler = StandardScaler()
data_sd = pd.DataFrame(scaler.fit_transform(data)) 
data_sd.dropna(axis=0, how='any', inplace=True) #on rows, delete any row with at least one missing value, True let us working on the original dataset, not on a copy
data_sd.dropna(axis=1, how='any', inplace=True) #on columns
data_sd.fillna(data_sd.mean(), inplace=True)

###PRINCIPAL COMPONENT ANALISYS
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

pca1 = PCA()
pca1.fit(data_sd)
cum_var= np.sum(pca1.explained_variance_ratio_[:2])* 100
print(f'Cumulate percentage of explained variance of the model, 2 PC. {cum_var:.2f}%')
pca = PCA(n_components=2)
data_pca = pd.DataFrame(data=pca.fit_transform(data_sd), columns=['PC1', 'PC2'])    #new dataset based on pca
cum_var1= np.cumsum(pca1.explained_variance_ratio_)
plt.plot(cum_var1),plt.xlabel('# principal components-1'), plt.ylabel('Cumulative sum of variance'),plt.title('Cumulative Variance plot'), plt.xlim(1,5)
#cumulative variance explained by each principal component. 
#The x-axis shows the number of principal components, while the y-axis shows the cumulative sum of explained variance.

#controlla errore nel punto di partenza del plot!!!


###TRAIN TEST
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #random state is for setting the seed

###RANDOM FOREST
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
# The hyperparameters of the model have a specif meaning, such as:
# "n_estimators" indicates the number of trees in the forest.
# "max_features="auto"" indicates the maximum number of features to consider when splitting a node, here it is set to the square root of the total number of features.
# "random_state=42" is the random seed, it ensure reproducibility.
# "max_depth=3" the maximum depth of each tree.
# 
# At the end of the code, we evaluate the model performance using 'score' method, which returns the coefficient of determination R^2 of the prediction. 
# The R^2 score measures the proportion of variance in the target variable that is explained by the model.
rfr = RandomForestRegressor(n_estimators=100, max_features="auto", random_state=42, max_depth= 3)
rfr.fit(X_train, y_train)
y_pred = rfr.predict(X_test)
accuracy = rfr.score(X_test, y_test)
print("Accuracy:", accuracy)
plt.figure(figsize=(30, 30))
plot_tree(rfr.estimators_[0], filled=True)
plt.show()


### GRADIENT BOOSTING
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# It constructs a sequence of simple decision trees in which each tree is built based on the reults of the
# previous tree predictive error.
# It relies on the intuition that the best possible next model, when combined with previous models, 
# minimizes the overall prediction error. 
# We aim to fit the gradient boosting regressor on the training data in order to end up with the best parittion 
# of data based on the Friedman means squared error.
# This one is the mse with improvement score by Friedman, that allows to produce better approximations.
gbr = GradientBoostingRegressor(loss='ls',learning_rate=0.1,n_estimators=100, random_state=42, max_depth=3) 
gbr.fit(X_train, y_train)
y_pred = gbr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
accuracy = gbr.score(X_test, y_test)
print("Accuracy:", accuracy)
print(f'Mean squared error: {mse:.2f}%')
plt.figure(figsize=(20, 20))
plot_tree(gbr.estimators_[0][0], filled=True)
plt.show()


###KMEANS
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# It is an unsipervised learning method, so a clustering algorithm that aims to find the best number
# of group in order to minimize the squarred error between the mean of a cluster and the observation within 
# that cluster. We produce a kmeans analysis on a range of possibles values for k that goes from 2 to 14, and we select the 
# best one according to the silhoette index.
sse = []
for k in range(2, 15):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)
plt.plot(range(2, 15), sse, marker='o')
plt.xlabel('Numero di cluster')
plt.ylabel('SSE')
plt.show()
# A line plot is generated with K values on the x-axis and SSE values on the y-axis.
silhouette_scores=[]
clusters = range(2, 15)
for n_clusters in clusters:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    silhouette = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(silhouette)
# The Silhouette is a measure of the quality of a partition of dataset and it is computed by the
# difference between the average distance between a point and points in the same cluster, and the average distance
# between our point and points in near different clusters, it ranges from -1 to 1.
# The optimal K value will have the highest Silhouette score, indicating the best clustering performance.
kmeans = KMeans(n_clusters=7, random_state=42)  #refit the kmeans by using the number of clusters selected
kmeans.fit(X)
silhouette = silhouette_score(X, kmeans.labels_)
print('Silhouette score:', silhouette)
X_new= X.iloc[:, :].values
labels= kmeans.fit_predict(X)
print(labels)
plt.scatter(X_new[:, 0], X_new[:, 1], c=labels, s=50, cmap='viridis')
plt.show()
# The "s" parameter controls the size of the plotted points, and the "cmap" parameter specifies the color map.


### HIERARCHICAL- WARD METHOD
import scipy.cluster.hierarchy as hy
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
# The hierarchical methods create sequences of partitions as homogeneous as possibile within and as heretogeneous as possible betewwn. 
# Here we use an agglomerative clustering algorithm that merges clusters according to the ward method linkage.
# Ward aims to group clusters that minimises the sum of squared error. 
Z = linkage(X, 'ward')
fig = plt.figure(figsize=(15, 15))
dn = dendrogram(Z)
plt.title('Ward Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()



