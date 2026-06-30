print("code started")
import traceback
try:
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    data={
    "income":[20000,25000,30000,40000,45000,50000,55000,60000,65000,70000],
    "creditScore":[600,650,700,750,800,850,900,950,1000,1050],
    "loanAmount":[10000,15000,20000,25000,30000,35000,40000,45000,50000,55000],
    "Approved":[0,0,0,0,1,1,1,1,1,1],
    "EmploymentStatus":[0,0,0,0,1,1,1,1,1,1]
}
    df=pd.DataFrame(data)
    x=df[["income","creditScore","loanAmount","EmploymentStatus"]]
    y=df["Approved"]
    model=DecisionTreeClassifier()
    model.fit(x,y)
    print("\n==============loan prediction system==================\n")
    income=int(input("Enter your income: "))
    creditScore=int(input("Enter your credit score: "))
    loanAmount=int(input("Enter the loan amount: "))
    employmentStatus=int(input("Enter your employment status (0 for unemployed, 1 for employed): "))
    result=model.predict([[income,creditScore,loanAmount,employmentStatus]])
    print("\n==============loan prediction result==================\n")

    if result[0]==1:
        print("Congratulations! Your loan has been approved.")
    else:
        print("Sorry, your loan is not approved.")
    print("\n==============SUGGESTIONs==================\n")
    if creditScore<700:
        print("Consider improving your credit score by paying bills on time and reducing debt.")
    if income<30000:
        print("Consider increasing your income through additional work or education.")
    if loanAmount>30000:
        print("Consider applying for a smaller loan amount to increase your chances of approval.")
    if employmentStatus==0:
        print("Consider seeking employment to improve your chances of loan approval.")
except Exception as e:
    print("error:",e)
    traceback.print_exc()
print("code ended")    