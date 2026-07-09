import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
df=pd.read_csv("loan_approval_data.csv")
df.head()
df.info()
#handle missing vals
categorical_cols=df.select_dtypes(include=["object"]).columns
numerical_cols=df.select_dtypes(include=["float64"]).columns
categorical_cols
rom sklearn.impute import SimpleImputer

num_imp=SimpleImputer(strategy="mean")
df[numerical_cols]=num_imp.fit_transform(df[numerical_cols])
cat_imp=SimpleImputer(strategy="most_frequent")
df[categorical_cols]=cat_imp.fit_transform(df[categorical_cols])
#EDA
#see how balanced our classes are 
classes_count=df["Loan_Approved"].value_counts()

plt.pie(classes_count, labels=["NO","Yes"],autopct="%1.1f%%")
plt.title("Is_loan approver or nao")
#analyse categories
'''gender_cnt= df["Gender"].value_counts()
ax=sns.barplot(gender_cnt)
ax.bar_label(ax,containers[0])'''

edu_cnt=df["Education_Level"].value_counts()
ax = sns.barplot(edu_cnt)
ax.bar_label(ax.containers[0])
#analyse income
sns.histplot(
    data=df,
    x = "Applicant_Income",
    bins=20)
sns.histplot(
    data=df,
    x = "Coapplicant_Income",
    bins=20)
#outliers _ boxplots
sns.boxplot(
    data=df,
    x="Loan_Approved",
    y="Applicant_Income")
fig,axes=plt.subplots(2,2)

sns.boxplot(ax=axes[0,0],data=df,x="Loan_Approved",y="Applicant_Income")
sns.boxplot(ax=axes[1,0],data=df,x="Loan_Approved",y="Credit_Score")
sns.boxplot(ax=axes[0,1],data=df,x="Loan_Approved",y="DTI_Ratio")
sns.boxplot(ax=axes[1,1],data=df,x="Loan_Approved",y="Savings")

plt.tight_layout()
#credit score for lone appruval
sns.histplot(
    data=df,
    x="Credit_Score",
    hue="Loan_Approved",
    bins=20,
    multiple="dodge"
)
#encoding categorical feature
df=df.drop("Applicant_ID",axis=1)
df.head()
df.columns
df.info()
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

le = LabelEncoder()

df["Education_Level"] = le.fit_transform(df["Education_Level"])
df["Loan_Approved"] = le.fit_transform(df["Loan_Approved"])
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

cols = ["Employment_Status", "Marital_Status", "Loan_Purpose", "Property_Area","Gender","Employer_Category"]

ohe = OneHotEncoder(
    drop="first",
    sparse_output=False,
    handle_unknown="ignore"
)

encoded = ohe.fit_transform(df[cols])

encoded_df = pd.DataFrame(
    encoded,
    columns=ohe.get_feature_names_out(cols),
    index=df.index
)

df = pd.concat([df.drop(columns=cols), encoded_df], axis=1)

print(df.head())
ohe.get_feature_names_out(cols)
#correlationheat map
nums_cols=df.select_dtypes(include="number")
corr_met=nums_cols.corr()

plt.figure(figsize=(15,8))
sns.heatmap(
    corr_met,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)
nums_cols.corr()["Loan_Approved"].sort_values(ascending=False)
#train test split 
X=df.drop("Loan_Approved",axis=1)
y=df["Loan_Approved"]
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=20,random_state=42)
from sklearn.preprocessing import StandardScaler
import numpy as np

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled
#train and evaluate
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

log_model = LogisticRegression()
log_model.fit(X_train_scaled,y_train)

y_pred=log_model.predict(X_test_scaled)

#EVALUATION
print("Logistic regression")
print("Precision: ",precision_score(y_test,y_pred))
print("Recall: ",recall_score(y_test,y_pred))
print("F1_score: ",f1_score(y_test,y_pred))
print("Accuracy: ",accuracy_score(y_test,y_pred))
print("CM: ",confusion_matrix(y_test,y_pred))
#knn
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=7)
knn_model.fit(X_train_scaled,y_train)

y_pred=knn_model.predict(X_test_scaled)

#EVALUATION
print("knn model")
print("Precision: ",precision_score(y_test,y_pred))
print("Recall: ",recall_score(y_test,y_pred))
print("F1_score: ",f1_score(y_test,y_pred))
print("Accuracy: ",accuracy_score(y_test,y_pred))
print("CM: ",confusion_matrix(y_test,y_pred))
#naivebayes
from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model.fit(X_train_scaled,y_train)

y_pred=nb_model.predict(X_test_scaled)

#EVALUATION
print("GaussianNB model")
print("Precision: ",precision_score(y_test,y_pred))
print("Recall: ",recall_score(y_test,y_pred))
print("F1_score: ",f1_score(y_test,y_pred))
print("Accuracy: ",accuracy_score(y_test,y_pred))
print("CM: ",confusion_matrix(y_test,y_pred))
#best model is naive bayes
'''#feature engineering
df["DTI_Ratio_sq"]=df["DTI_Ratio"] == 2
df["Credit_Score_sq"]=df["Credit_Score"] == 2

df["Applicant_Income_log"]=np.log1p(df["Applicant_Income"])

X=df.drop(columns=["Loan_Approved","Credit_Score","DTI_Ratio","Applicant_Income"])
y=df["Loan_Approved"]'''

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=20,random_state=42)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
