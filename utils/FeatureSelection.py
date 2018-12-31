# Feature Importance
from utils.MlUtils import load_csv
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier

# load the iris datasets
dataset = load_csv('../data/flights.csv')
x
# fit an Extra Trees model to the data
model = ExtraTreesClassifier()
model.fit(dataset.data, dataset.target)
# display the relative importance of each attribute
print(model.feature_importances_)
