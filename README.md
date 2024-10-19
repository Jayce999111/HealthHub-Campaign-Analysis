# HealthHub Campaign Analysis

## Project Background

HealthHub is a healthcare company focused on delivering high-quality health services and promoting awareness through targeted campaigns via its website and mobile app.

The company has accumulated significant amounts of data on its sales, campaigns, operational efficiency, plan offerings, and loyalty programs, which have been underutilized. This project aims to thoroughly analyze and synthesize this data to uncover critical insights that can improve HealthHub's commercial success.

### Key Insights and Recommendations:

- **Signup Trends Analysis**: Evaluation of historical signup patterns, both **globally** and **by campaign type**, focusing on total signups, cost, and Average Order Value (AOV).
  
- **Click Conversion Rate into Signups**: An analysis of HealthHub's various campaign types to understand their impact on signups and the value they bring to the organization.

- **Seasonal and Time-Based Trends**: An examination of how seasonal trends affect signup patterns and the effectiveness of timing in campaign launches.

- **Cost Analysis**: A detailed review of the costs associated with each campaign type, highlighting areas for optimization and efficiency in marketing spend.

![ERD Diagram](./images/EDR.png)

---

## Executive Summary

### Overview of Findings:

After peaking in late 2021, HealthHub's sales significantly declined by 2022. Key performance indicators show two consecutive years of increases in order volume and revenue by **6.67%**, with the **average signup cost** now at **$3.30**. While these increases can be broadly attributed to a return to pre-pandemic normalcy, additional contributing factors are explored in the following sections, which also highlight key opportunities for improvement.

Below is an overview page from the Power BI dashboard, with more examples included throughout the report. The entire interactive dashboard can be downloaded [here](#).

---

![Overview Diagram](./images/overview.png)

### Sales Trends:

- The company's sales peaked in 2021 with **1,541,000 orders**, totaling **$7,560,146** in yearly revenue. This peak aligns with the surge in healthcare demand during the COVID-19 pandemic, as consumer behavior shifted with more people seeking healthcare services and products online.
- Starting in the first quarter of 2023, the average order value (AOV) dropped year-over-year for 24 consecutive months, marking a **21% decrease** compared to the previous year’s AOV.
- Despite this decline in AOV, both signups and revenue have increased as more customers are joining campaigns. Though customers are opting for lower-priced campaigns more frequently, the increased transaction volume pushed the company’s revenue to an all-time high of **$8,320,576**.
- A significant drop in AOV was also observed in early 2020, largely due to the lower-cost **COVID-19 Vaccination Drive** campaign, which contributed to the overall decrease.
![Salesview Diagram](./images/sales_trend.png)
### Product Performance:

- **55%** of the company's **orders** come from just four campaigns: COVID-19 Vaccination Drive, Telehealth Access Initiative, Community Wellness Programs, and Mental Wellness Program, These four campaigns account for **$4.61 million** in revenue in 2024.
- The **COVID Awareness** category has underperformed, contributing only **5.31%** of total revenues and orders, despite having one of the lowest signup costs.
- The **Telehealth Access Initiative** campaign has continued to grow since 2021, reaching **9.86%** in 2024. It remains one of the largest revenue contributors, accounting for **23%** of total revenue.


### Campaign Summary:

- **Social Media** shows high engagement, with campaigns like the **COVID-19 Vaccination Drive** achieving the highest conversion rate of **37.5%**, while the **Seasonal Flu Vaccination** follows closely at **32.61%**.
- Interestingly, **TV** campaigns, despite being traditionally broad-reach, exhibit lower conversion rates, such as **Mental Wellness Awareness** at **25%** and **Heart Health Awareness Drive** at **21.82%**.
- **Email** platforms, used for the **Telehealth Access Initiative** and **Diabetes Management Program**, have steady conversion rates (around **27%**), reflecting targeted reach but slightly lower engagement compared to social media-driven campaigns.
![Media Diagram](./images/conversion_trend.png)

### Recommendations:

Based on the uncovered insights, the following recommendations have been provided:

- With **55%** of the orders and revenue coming from just four campaigns, diversifying the offerings is crucial. Expanding the media strategy for promoting these campaigns, particularly through social media, could provide upsell opportunities.

- Creating loyalty programs to boost conversion rates: In order to convert non-members, consider offering a one-time-only sign-up discount with increased general marketing of membership benefits and savings. Focus targeted and personalized ads on previous customers, and utilize past signup data to increase marketing efforts when previously purchased products need updating.

- Focus on Volume-Driven Campaigns: Based on sales trends users are more likely to sign up for lower-cost campaigns, creating multiple frequent campaigns with affordable entry points. This strategy leverages the demand for lower-priced options it will boosting participation and driving higher cumulative revenue.

- Despite the general sales success of the COVID-19 campaign, vaccine sales have been disappointingly low, contributing only **5%** of revenue in 2024. Enhancing marketing efforts targeting previous vaccine users for booster shots could significantly boost sales.

- Capitalize on the growing share of the Telehealth Access Initiative campaign by introducing higher-cost, higher-value campaigns within the same category, such as specialized consultations or premium health packages.
