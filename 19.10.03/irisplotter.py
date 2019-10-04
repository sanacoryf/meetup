from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as numpy

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']



def plottwofeatures(x_var,y_var):
    for t, marker, c in zip(range(3), ">ox", "rgb"):
        plt.scatter(features[target==t,x_var],
            features[target==t,y_var],
            marker = marker, c=c)

    plt.xlabel(feature_names[x_var])
    plt.ylabel(feature_names[y_var])
    
    fn = "plot{0}{1}.pdf".format(x_var,y_var)
    print(fn)
    plt.savefig(fn)
    plt.clf()





for i in range(3):
    for j in range(i+1,4):
        plottwofeatures(i,j)


print(feature_names)

