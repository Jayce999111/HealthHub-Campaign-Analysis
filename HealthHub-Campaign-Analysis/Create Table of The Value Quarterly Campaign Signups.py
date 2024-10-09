import pandas as pd

# First table (summary data with campaign type and cost per signup)
summary_data = {
    'Campaign Name': ['COVID-19 Vaccination Drive', 'Telehealth Access Initiative', 'Mental Wellness Awareness', 'Preventive Care Checkups', 'Elderly Care Outreach'],
    'Campaign Type': ['COVID Awareness', 'Telehealth Services', 'Mental Health Awareness', 'Preventive Health', 'Senior Health Services'],
    'Cost per Signup ($)': [3.33, 5.45, 5.00, 4.29, 6.67]
}

# Second table (yearly signups data)
yearly_data = {
    'Campaign Name': ['COVID-19 Vaccination Drive', 'COVID-19 Vaccination Drive', 'Telehealth Access Initiative', 'Mental Wellness Awareness', 'Preventive Care Checkups', 'Elderly Care Outreach'],
    'Year': [2020, 2021, 2020, 2020, 2020, 2020],
    'Q1 Signups': [50000, 100000, 20000, 15000, 15000, 10000],
    'Q2 Signups': [60000, 120000, 30000, 18000, 20000, 12000],
    'Q3 Signups': [70000, 110000, 40000, 20000, 18000, 14000],
    'Q4 Signups': [80000, 80000, 50000, 22000, 22000, 15000]
}

# Create DataFrames
df_summary = pd.DataFrame(summary_data)
df_yearly = pd.DataFrame(yearly_data)

# Merge both tables to get cost per signup and campaign type for each campaign
merged_df = pd.merge(df_yearly, df_summary, on='Campaign Name')

# Calculate total money for each quarter
merged_df['Q1 Total Money ($)'] = merged_df['Q1 Signups'] * merged_df['Cost per Signup ($)']
merged_df['Q2 Total Money ($)'] = merged_df['Q2 Signups'] * merged_df['Cost per Signup ($)']
merged_df['Q3 Total Money ($)'] = merged_df['Q3 Signups'] * merged_df['Cost per Signup ($)']
merged_df['Q4 Total Money ($)'] = merged_df['Q4 Signups'] * merged_df['Cost per Signup ($)']

# Group by 'Campaign Type' and calculate the total money spent per type for each quarter
grouped_by_type = merged_df.groupby('Campaign Type').sum(numeric_only=True)

# Select and rename the relevant columns
grouped_by_type = grouped_by_type[['Q1 Total Money ($)', 'Q2 Total Money ($)', 'Q3 Total Money ($)', 'Q4 Total Money ($)']]

# Display the final table
print(grouped_by_type)
