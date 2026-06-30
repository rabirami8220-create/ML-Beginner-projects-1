import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data={
    "CGPA":[9.0,8.5,7.0,6.5,8.0],
    "Aptitude":[85,80,70,60,75],
    "Placement":[1,1,0,0,1],
    "communication":[8,7,6,5,7],
    "Codingscore":[90,85,70,60,80]
}
df=pd.DataFrame(data)
X=df[["CGPA","Aptitude","communication","Codingscore"]]
y=df["Placement"]
model=DecisionTreeClassifier()
model.fit(X,y)
print("\n=======PLCEMENT PREDICTION========\n")
cgpa=float(input("Enter CGPA: "))
aptitude=int(input("Enter Aptitude Score: "))
communication=int(input("Enter Communication Score: "))
codingscore=int(input("Enter Coding Score: "))
prediction=model.predict([[cgpa,aptitude,communication,codingscore]])
if prediction[0]==1:
    print("The student is likely to get placed.")
else:
    print("The student is not likely to get placed.")
print("\nRecommendations:")
if aptitude<70:
    print("- Improve aptitude skills through practice and coaching.")
if communication<6:
    print("- Work on improving communication skills.")
if codingscore<70:
    print("- Focus on enhancing coding skills.")
if cgpa<7.0:
    print("- Aim to improve CGPA through consistent academic performance.")