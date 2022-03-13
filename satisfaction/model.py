import pandas as pd
import pickle
df1=pd.read_csv("dataset_form.csv")

x=df1.drop(['satisfaction','Unnamed: 0'],axis=1)
y=df1['satisfaction']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.25)

from sklearn.ensemble import RandomForestClassifier
rm=RandomForestClassifier(n_estimators=500,max_features="sqrt",max_depth=80)
rm.fit(x_train,y_train)

pickle.dump(rm,open('model.pkl','wb'))
