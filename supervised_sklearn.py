from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

plt.style.use('ggplot')

#load dataset
iris = dataset.load_iris()

type(iris)

print(iris.keys())


#check the type of the data
type(iris.data), type(iris.target) #shows they are numpy arrays

irish.data.shape #shows (150,4) rows and columns respectively

#print array index
iris.target_names

#EXPLORATORY DATA ANALYSIS (EDA)

#assign to values
x = iris.data
y = iris.target

df = pd.DataFrame(x, columns=iris.feature_names)

print(df.head())

#visual EDA
_ = pd.plotting.scatter_matrix(df,c=y,figsize=[8,s=150,marker=D])


#CLASSIFYING USING K-NEAREST ALGORITHM
#using sklearn to fit a classifier
from sklearn.neighbors import KNeighborsClassifier

#instantiate the classifier
knn = KNeighborsClassifier(n_neighbors=6)

#fit the data of iris into the model
knn.fit(iris['data'],iris['target'])

#print shape
iris['data'].shape  #(150,4)
iris['target'].shape

#predicting on unlabeled data
x_new = np.array([[5.6,2.8,5,0.2],
                  [4,2.5,6,8.6],
                  [1.8,2.6,5,10.5]])

#now perform prediction
prediction = knn.predict(x_new)

#check shape
x_new.shape

#print prediction
print('prediction: {}'.format(prediction))

[1,1,0] #output prediction


#Prediction002 
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier 

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party',axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)

# Predict the labels for the training data X
y_pred = knn.predict(X)
X_new = knn.predict(X_new)

# Predict and print the label for the new data point X_new
new_prediction = np.array(X_new)
print("Prediction: {}".format(new_prediction))


#UPNEXT- MEASURING MODEL PERFORMANCE
#split your data into training and testing

#train/test split
from sklearn.model_selection import train_test_split

X_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

#instantiate the classifier
knn = KNeighborsClassifier(n_neighbors=8)

#feed in the test data
knn.fit(X_train, y_train)

#predict
y_pred = knn.predict(x_test)

print("test set prediction:\n {}".format(y_pred))

#check accuracy test in percentage
knn.score(x_test, y_test)   #0.95555555 output sample meaning 95% accurate

# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys())
print(digits.DESCR)

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

#PERform MNIST no. detection
# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Create feature and target arrays
X = digits.data
y = digits.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))

# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train,y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()


#REGRESSION WITH BOSTON HOUSE DATASET

#first import and load dataset
boston = pd.load_csv('boston.csv')

#display the recent data
print(boston.head())

#now create feature and Target
X = boston.drop('MEDV',axis=1).Values
y = boston['MEDV'].values

#predict house from a single feature column no. 5
X_room = X[:,5]

#you can check the type of the data
type(X_rooms), type(y) #numpy arrays

#reshape
y = y.reshape(-1 ,1)
X_rooms = X_rooms.reshape(-1, 1)

#plot house numbers vs number of rooms
plt.scatter(X_rooms, y)
plt.ylabel('value of houses/1000($)')
plt.xlabel('No. of rooms')
plt.show();

#Fitting a Linear Regression Model
import numpy as np
from sklearn.linear_model import LinearRegression

#instantiate the model
reg = LinearRegression()

#fit the model
reg.fit(X_rooms, y)

#prediction_space
prediction_space =  np.linspace(min(X_rooms), max(X_rooms)).reshape(-1,1)

#plot the line
plt.scatter(X_rooms, y, color='blue')
plt.plot(prediction_space, reg.predict(prediction_space), color='black', linewidth=3)
plt.show()


#Importing data for supervised Learning to predict Life expectancy of a country using their GDP
# Import numpy and pandas
import numpy as np
import pandas as pd

# Read the CSV file into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create arrays for features and target variable
y = df['life'].values
X = df['fertility'].values

# Print the dimensions of X and y before reshaping
print("Dimensions of y before reshaping: {}".format(y.shape))
print("Dimensions of X before reshaping: {}".format(X.shape))

# Reshape X and y
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)

# Print the dimensions of X and y after reshaping
print("Dimensions of y after reshaping: {}".format(y.shape))
print("Dimensions of X after reshaping: {}".format(X.shape))

#output
    Dimensions of y before reshaping: (139,)
    Dimensions of X before reshaping: (139,)
    Dimensions of y after reshaping: (139, 1)
    Dimensions of X after reshaping: (139, 1)
    


#THE BASICS OF LINEAR REGRESSION

#Linear Regression on all features
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

reg_all = LinearRegression()

reg_all.fit(X_train, y_train)
y_pred=reg_all.predict(X_test)
reg_all.score(X_test, y_test)



#LINEAR REGRESSION TO DO LIFE EXPECTANCY PREDICTION
# Import LinearRegression
from sklearn.linear_model import LinearRegression

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# Fit the model to the data
reg.fit(X_fertility,y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2 
print(reg.score(X_fertility, y))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()


#TRAIN/TEST FOR LINEAR REGRESSION
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train,y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error: {}".format(rmse))


#CROSS VALIDATION
#spliting the data into test and train and using Folder mathods for training.
#Hold one folder for testing and iterate through the rest as training data

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

reg = LinearRegression()

cv_results = cross_val_score(reg, X, y, cv=5)

print(cv_results) #prints an array

#you can also compute the mean 
np.mean(cv_results)

#EX 002
# Import the necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg,X,y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

#outputs 
[0.81720569 0.82917058 0.90214134 0.80633989 0.94495637]
Average 5-Fold CV Score: 0.8599627722793232


#K-FOLDER CV_COMPARISON
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Perform 3-fold CV
cvscores_3 = cross_val_score(reg, X, y, cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 = cross_val_score(reg, X,y, cv=10)
print(np.mean(cvscores_10))

#output
0.8718712782622108
0.8436128620131201

#using the time loops to check for comparison,
In [3]: %timeit cross_val_score(reg, X, y, cv = 3)
100 loops, best of 3: 7.83 ms per loop

In [10]: %timeit cross_val_score(reg, X, y, cv = 10)
10 loops, best of 3: 24.5 ms per loop


