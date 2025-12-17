# Employee Survey Data Generator

## 📊 Overview

This Python script generates a synthetic dataset simulating employee survey responses for organizational analysis. The dataset includes demographic information, employment details, and Likert-scale survey responses across multiple dimensions.

It can be used in pretty much every scenario, you just have to change names and variables. Extremely helpful for those who do not have datasets to work with initially. Start right away!

## 🚀 Features

- **Synthetic Data Generation**: Creates realistic employee survey data for testing and development
- **Customizable Parameters**: Easily adjust sample size, categories, and distributions
- **Regional Focus**: Middle Eastern context with appropriate names and regions
- **Structured Output**: Clean Excel format ready for analysis

## 📁 Dataset Structure

### Employee Demographics
- **First Name & Last Name**: Middle Eastern names for regional authenticity
- **Region**: UAE, KSA, Qatar, Oman, Bahrain
- **Legal Entity**: Entity A, B, or C

### Employment Details
- **BU Name**: Business unit (Finance, Operations, HR, IT, Sales)
- **Grade**: Numerical grade from 1-9
- **Job**: Position title (Analyst, Senior Analyst, Manager, etc.)
- **Position Type**: Full-Time, Contract, Intern
- **Department**: Functional department
- **Line Manager**: Reporting manager
- **BAND**: Random date between 2022-01-01 and 2025-12-31

### Survey Components
- **Status of Survey**: Completed, Deferred, or Initiated
- **Survey Dimensions** (5-point Likert scale):
  - Information
  - Principles
  - Support
  - Teamwork
- **Year**: Survey year (2022-2025)

## 🛠️ Technical Details

### Dependencies
```python
pandas >= 1.0.0
numpy >= 1.18.0
openpyxl  # For Excel export
```

### Installation
```bash
pip install pandas numpy openpyxl
```

### Usage
1. **Basic Execution**:
```python
python employee_survey_generator.py
```

2. **Customize Parameters**:
   - Modify `n` for different sample sizes
   - Adjust arrays to add/remove categories
   - Change probability distributions in `np.random.choice()`

3. **Output**:
   - Excel file saved to: `C:/Users/basil/OneDrive/Desktop/Base/Work/DP/employee_survey_sample1.xlsx`

## 📈 Data Distributions

### Survey Status (Default)
- **60%**: Completed
- **20%**: Deferred
- **20%**: Initiated

### Survey Response Scales
All survey questions use a 5-point Likert scale:
1. 5 - Strongly Agree
2. 4 - Agree
3. 3 - Neither Agree nor Disagree
4. 2 - Disagree
5. 1 - Strongly Disagree

## 🔧 Customization Options

### Sample Size
```python
n = 500  # Change to generate more/fewer records
```

### Add New Categories
```python
# Example: Add new job titles
jobs = ["Analyst", "Senior Analyst", "Manager", "Associate", "Lead", "Director", "VP"]
```

### Modify Date Range
```python
"BAND": pd.to_datetime(np.random.choice(pd.date_range("2020-01-01", "2024-12-31"), n))
```

## 📊 Potential Use Cases

1. **HR Analytics**: Analyze survey trends across departments/regions
2. **Dashboard Development**: Test BI tools with realistic data
3. **Machine Learning**: Train models for sentiment analysis
4. **Training**: Data analysis workshops and tutorials
5. **System Testing**: Validate HRIS or survey platforms

## ⚙️ Configuration Tips

### Reproducibility
The script uses `np.random.seed(42)` for consistent results. Remove or change the seed for different random generations.

### Export Format
Change `to_excel()` to other formats:
```python
df.to_csv("output.csv", index=False)  # CSV format
df.to_json("output.json", orient="records")  # JSON format
```

### Performance
For larger datasets (>10,000 records), consider:
- Using categorical data types
- Chunked processing
- Memory optimization techniques

## 🧹 Data Quality Features

- **Consistent Data Types**: Proper datetime formatting for BAND column
- **Realistic Distributions**: Weighted probabilities for survey status
- **Domain Relevance**: Region-specific names and structures
- **No Missing Values**: Complete dataset generation

## 📝 Code Structure

```
employee_survey_generator.py
├── Import libraries
├── Set random seed
├── Define categorical variables
├── Create DataFrame with 17 columns
├── Generate random data for each column
├── Export to Excel
└── Return file path
```

## 🔍 Example Analysis Queries

```python
# Load and explore data
df = pd.read_excel("employee_survey_sample1.xlsx")

# Survey completion rate by region
completion_rate = df.groupby('Region')['Status of Survey'].value_counts(normalize=True)

# Average survey scores by department
df['Info_Score'] = df['Information'].str.split(' - ').str[0].astype(int)
avg_scores = df.groupby('Department')['Info_Score'].mean()

# Year-over-year survey participation
participation = df['Year'].value_counts().sort_index()
```

## ⚠️ Limitations

1. **Synthetic Data**: Not real employee information
2. **Random Relationships**: No causal relationships between variables
3. **Simplified Distributions**: Equal probability for most categories
4. **No Time Series Patterns**: Random date assignments

## 🤝 Contributing

To enhance this generator:
1. Add correlation structures between variables
2. Include more sophisticated distributions
3. Add data validation rules
4. Create parameter configuration file
5. Add unit tests

## 📄 License

This tool is for educational and testing purposes. Ensure compliance with data privacy regulations when using similar structures with real employee data.

## 🆘 Support

For issues or enhancements:
1. Check Python and library versions
2. Verify file path permissions
3. Ensure sufficient disk space
4. Validate categorical arrays aren't empty

---

*Note: This generator creates fictional data for testing purposes only. Always anonymize and protect real employee information according to organizational policies and data protection regulations.*
