import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
#%matplotlib inline

#Assumption:
# -------------------------
#There can be a maximum of 8 people at the out at a time. If the number of people in the crowd crosses 8 then 
# that particular exit will be considered block
# Also, this programme assumes that given the exit door to be taken, the user will be able to find his/her way to the exit door.
#Training (off-line) and validation
dataset = pd.read_csv("CSI_Training-Set.csv") # CSI_Training-Set.csv contains the data generated after performing experiments in different scenarios 
dataset.shape
dataset.head()
x = dataset.drop('Population', axis=1)
y=dataset['Population']
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print X_train.shape
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

#Floor Plans
# The code has been written for providing the users the possible exit in some floor. The code can be extended to accomodate all floors. 
# This is just the prototype to explain the process.   
# For a dummy floor with 30 rooms
# The following assignment is done:
# Room numbers: 1-10 -> out preference: 0,1,2
# Room numbers: 11-20 -> out preference: 1,2,0
# Room numbers: 21-30 -> out preference : 2,0,1

#testing
# -----------

test_dataset = pd.read_csv("CSI_Test.csv") # CSI_Test.csv corresponds to the data that is being generated in real time.

x_t = dataset.drop('Population',axis=1)

y_t = classifier.predict(x_t)

floor = raw_input("Type the floor you are in: ")

room = input("Enter your room no: ")

if (room > 30):
    print "INVALID ROOM NUMBER! YOUR FLOOR HAS ONLY ROOM NUMBERS BETWEEN 1 TO 30 !!"
    room = input("Enter valid room no: ")

print("Please access out gate #: ")

out=-1
if room < 11:
    if(y_t[1]!='Eight'):
        out=1
        # break
    elif(y_t[1]=='Eight' and y_t[2]!='Eight'):
        out=2
        # break
    else:
        out=0
    print(out)

elif (room > 20):
    print "greater than 20"
    if room < 31:
        if(y_t[2]!='Eight'):
            out=2
       
        elif(y_t[2]=='Eight' and y_t[0]!='Eight'):
            out=0
        
        else:
            out=1
    print(out)

elif (room > 10):
    if room < 21:
        if(y_t[1]!='Eight'):
            out=1
        
        elif(y_t[1]=='Eight' and y_t[2]!='Eight'):
            out=2
        
        else:
            out=0
    print(out)

