import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as slt

data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
Y = data[["Salary"]]

model = LinearRegression()
model.fit(X,Y)

slt.title("Salary prediction based on experience")
slt.write("Enter your year of experience to predict your salary")

year_input = slt.number_input("Year of Experience",min_value=0.0,max_value=50.0,step=0.1)

if year_input:
    print(year_input)
    
    predicted_salary = model.predict([[year_input]]).item()
    slt.success(f"Estimated Salary: {predicted_salary:,.2f}")

    
    
slt.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(X, Y, color="blue", label="Actual Data")
ax.plot(X, model.predict(X), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

slt.pyplot(fig)