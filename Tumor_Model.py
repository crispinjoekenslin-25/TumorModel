# Gene Expression of Tumor for Kaggle Dataset from https://www.kaggle.com/datasets/brsahan/genomic-data-for-cancer/data

# Created by Crispin Joe Kenlin A - 14.08.2024

#Importing Libraries
#Download required libraries using pip or conda
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score,confusion_matrix
from sklearn.model_selection import train_test_split

# Import data and clean
file = r"" # path to your gene_expression.csv file within the ""
data = pd.read_csv(file)

# print(data.head())  
# Optional to check the data import 

# Declare features and output
data_features = data.drop("Cancer_Present",axis=1)
data_output = data["Cancer_Present"]

# print(data_output.head(),"\n",data_features.head()) 
# Optional to check features and output

# Declare the Train Test and Split 
x_train, x_test, y_train, y_test = train_test_split(data_features,data_output,train_size=0.8,random_state=23)
# Init. model
model = RandomForestClassifier()
model.fit(x_train,y_train)
# Y prediction for calculating scores
y_pred = model.predict(x_test)

print(f"Accuracy score : {accuracy_score(y_test,y_pred):.2f}")
print(f"Precision score : {precision_score(y_test,y_pred):.2f}")
print(f"Confusion Matrix : {confusion_matrix(y_test,y_pred)}")

# Function for prediction
def prediction():
    gene_a = float(input("Enter Gene A expression : "))
    gene_b = float(input("Enter Gene B expression : "))
    query = pd.DataFrame([[gene_a, gene_b]],columns=["Gene_1", "Gene_2"])
    predicted_output = model.predict(query)
    if predicted_output == 0:
        print("Prediction : No tumor")
    else:
        print("Prediction : Tumor Present")

# Run prediction function
prediction()