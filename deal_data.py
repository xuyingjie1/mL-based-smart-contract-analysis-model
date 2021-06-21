import pandas as pd
data = pd.read_csv("solidity7.csv")
data.dropna(inplace=True)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
train_labels = pd.Series(["reentrancy"]*50+["not reentrancy"]*50)
data["labels"]=train_labels
x_train,x_test  = train_test_split(data)
x_train_lables = x_train["labels"]
x_test_lables = x_test["labels"]
x_train = x_train.iloc[:,0:-1]
x_test = x_test.iloc[:,0:-1]
# 使用knn进行分类
knn_class = KNeighborsClassifier(n_neighbors=43)
knn_class.fit(x_train,x_train_lables)
predict = knn_class.predict(x_test)
accurate_1 = accuracy_score(predict,x_test_lables)
recall = recall_score(predict,x_test_lables,average='micro')
precision = precision_score(predict,x_test_lables,average='macro')
print("The KNN:", accurate_1, recall, precision)
sgd_clf = SGDClassifier(random_state=35)
sgd_clf.fit(x_train, x_train_lables)
predict = sgd_clf.predict(x_test)
accurate1 = accuracy_score(predict,x_test_lables)
recall = recall_score(predict,x_test_lables,average='micro')
precision = precision_score(predict,x_test_lables,average='macro')
print("The SGD:", accurate1, recall, precision)
