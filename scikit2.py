from sklearn.datasets import load_boston
X,y = load_boston(return_X_y=True)      #we get 2 arrays

from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
mod=LinearRegression()
mod.fit(X,y)
mod.predict(X)
mod=KNeighborsRegressor().fit(X,y)
pred= mod.predict(X)

from matplotlib import pyplot as plt
plt.scatter(pred,y)
plt.show()

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
mod =KNeighborsRegressor().fit(X,y)
pipe=Pipeline([
    ("scale", StandardScaler()),
    ("model",KNeighborsRegressor())
])
pipe.fit(X,y)
pred=pipe.predict(X)
plt.scatter(pred, y)
plt.show()

from sklearn.model_selection import GridSearchCV
pipe.get_params()
GridSearchCV(estimator=pipe,
             param_grid={"model_n_neighbors": [1,2,3,4,5,6,7,8,9,10]},
             cv=3)
mod.fit(X,y);
print(pd.dataframe(mod.cv_results_))

print(load_boston()["DESCR"])