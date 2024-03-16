#important imports:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import  RandomizedSearchCV, train_test_split , GridSearchCV
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle
#To turn off warning messages.
import warnings
warnings.filterwarnings('ignore')


# Importing the dataset 
data = pd.read_csv("first inten project.csv")  

data1 = data.copy()
#Rename columns
n_cols = {'number of adults':'Num_of_Adults',
            'number of children':  'Num_of_Children',
            'number of weekend nights': 'Num_of_Weekend_Nights',
            'number of week nights' : 'Num_of_Week_Nights',
            'type of meal': 'Type_of_Meal',
            'car parking space' : 'Car_Parking_Space' ,
            'room type' : 'Room_Type',
            'lead time' : 'Lead_Time',
            'market segment type' : 'Market_Segment_Type',
            'repeated' : 'Repeated',
            'average price ':'AVG_Price',
            'special requests':'Special_Requests',
            'date of reservation':'Date_of_Reservation',
            'booking status':'Booking_Status'}

data1.rename(columns=n_cols ,inplace=True)


#Convert categorical to binary
data1['Booking_Status'] = data1['Booking_Status'].map({'Not_Canceled': 1, 'Canceled': 0, })
#Convert date to int
data1['Date_of_Reservation'] = pd.to_datetime(data1['Date_of_Reservation'],errors='coerce')
data1['day'] = data1['Date_of_Reservation'].dt.day
data1['month'] = data1['Date_of_Reservation'].dt.month
data1['year'] = data1['Date_of_Reservation'].dt.year


data1['Date_of_Reservation'] = data1['Date_of_Reservation'].fillna(data1['Date_of_Reservation'].mode()[0])
data1['day'] = data1['day'].fillna(data1['day'].mode()[0])
data1['month'] = data1['month'].fillna(data1['month'].mode()[0])
data1['year'] = data1['year'].fillna(data1['year'].mode()[0])



# extract the day, month, and year components
data1['Date_of_Reservation'] = data1['Date_of_Reservation'].astype(np.int64)
data1['day'] = data1['day'].astype(int)
data1['month'] = data1['month'].astype(int)
data1['year'] = data1['year'].astype(int)


#Using LabelEncoder
label_en = LabelEncoder()
data1['Market_Segment_Type'] = label_en.fit_transform(data1['Market_Segment_Type'])
data1['Room_Type'] = label_en.fit_transform(data1['Room_Type'])
data1['Type_of_Meal'] = label_en.fit_transform(data1['Type_of_Meal'])

outlier_indices = np.where((data1['AVG_Price'] >= 300) | (data1['AVG_Price'] <= 25))
final_data = data1.drop(outlier_indices[0])

final_data = final_data.drop(["Booking_ID"], axis = 1)  
X = final_data.drop(["Booking_Status"], axis = 1)  
y = final_data["Booking_Status"]
#Features selection
X = X.drop(["Num_of_Children", 
                    "P-not-C",
                    "P-C",
                    "Num_of_Weekend_Nights",
                    "Type_of_Meal",
                    "Room_Type",
                    "day",
                    "month",
                   "Num_of_Week_Nights",
                   "Num_of_Adults",
                   "Car_Parking_Space",
                   "Repeated"], axis = 1)  

#Scale all values for good Accuracy
sc = StandardScaler()
col = ['Lead_Time','Market_Segment_Type', 'AVG_Price', 'Special_Requests','year','Date_of_Reservation']
X[col] = sc.fit_transform(X[col])


#the training and testing set  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42) 

#Prepare for grid search
clf_knn=KNeighborsClassifier()
parametrs_knn={'n_neighbors':[1,3,5,7,9,11], 'metric':['euclidean','manhattan','chebyshev']}
grid_clf_knn=GridSearchCV(clf_knn, parametrs_knn, cv=6, n_jobs=-1)
grid_clf_knn.fit(X_train, y_train)


best_model_knn=grid_clf_knn.best_estimator_
y_pred_knn=best_model_knn.predict(X_test)

cm_knn = confusion_matrix(y_test, y_pred_knn)
print("Confution matrix for model " f'{best_model_knn} : \n',cm_knn)
ac_knn = accuracy_score(y_test, y_pred_knn)
print("Accuracy score for model " f'{best_model_knn} : ',ac_knn)
cr_knn = classification_report(y_test, y_pred_knn)
print("classification_report for model " f'{best_model_knn} : \n',cr_knn)


print(best_model_knn.score(X_test,y_test))
print(best_model_knn.score(X_train,y_train))


pickle.dump(best_model_knn, open('model.pkl' , 'wb'))

model = pickle.load(open('model.pkl' , 'rb'))

print(model.predict([[224,3,88,0,1443744000000000000,2015]]))

