import pandas as pd
import numpy as np

np.random.seed(42)

n = 200

first_names = ["Ahmed", "Sara", "Omar", "Fatima", "Ali", "Aisha", "Hassan", "Mariam", "Khalid", "Noor"]
last_names = ["Khan", "Ahmed", "Ali", "Hussain", "Siddiqui", "Rahman", "Malik", "Sheikh", "Qureshi", "Farooq"]
regions = ["UAE", "KSA", "Qatar", "Oman", "Bahrain"]
legal_entities = ["Entity A", "Entity B", "Entity C"]
bu_names = ["Finance", "Operations", "HR", "IT", "Sales"]
jobs = ["Analyst", "Senior Analyst", "Manager", "Associate", "Lead"]
positions = ["Full-Time", "Contract", "Intern"]
departments = ["Data", "Finance", "HR", "Technology", "Business"]
managers = ["Manager 1", "Manager 2", "Manager 3", "Manager 4"]
status = ["Completed", "Deferred", "Initiated"]
Information = ["5 - Strongly Agree", "4 - Agree", "3 - Neither Agree nor Disagree", "2 - Disagree", "1 - Strongly Disagree"]
Principles = ["5 - Strongly Agree", "4 - Agree", "3 - Neither Agree nor Disagree", "2 - Disagree", "1 - Strongly Disagree"]
Support = ["5 - Strongly Agree", "4 - Agree", "3 - Neither Agree nor Disagree", "2 - Disagree", "1 - Strongly Disagree"]
Teamwork = ["5 - Strongly Agree", "4 - Agree", "3 - Neither Agree nor Disagree", "2 - Disagree", "1 - Strongly Disagree"]


df = pd.DataFrame({
    "First Name": np.random.choice(first_names, n),
    "Last Name": np.random.choice(last_names, n),
    "Region": np.random.choice(regions, n),
    "Legal Entity": np.random.choice(legal_entities, n),
    "BU Name": np.random.choice(bu_names, n),
    "Grade": np.random.randint(1, 10, n),
    "Job": np.random.choice(jobs, n),
    "Position": np.random.choice(positions, n),
    "Department": np.random.choice(departments, n),
    "Line Manager": np.random.choice(managers, n),
    "Status of Survey": np.random.choice(status, n, p=[0.6, 0.2, 0.2]),
    "BAND": pd.to_datetime(
        np.random.choice(pd.date_range("2022-01-01", "2025-12-31"), n)
    ),
    "Information": np.random.choice(Information, n),
    "Principles": np.random.choice(Principles, n),
    "Support": np.random.choice(Support, n),
    "Teamwork": np.random.choice(Teamwork, n),
    "Year": np.random.choice([2022, 2023, 2024, 2025], n)
})

file_path = "C:/Users/basil/OneDrive/Desktop/Base/Work/DP/employee_survey_sample1.xlsx"
df.to_excel(file_path, index=False)

file_path
