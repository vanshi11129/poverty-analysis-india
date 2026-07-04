# poverty-analysis-india
This is a poverty analysis for all the states/UT in India. 
It is an end-to-end data analytics project analyzing poverty trends across India using official government datasets. This project combines Python for data cleaning and Exploratory Data Analysis (EDA) with, Power BI to build an interactive dashboard for visual insights and a report of the findings.

🚀 Project Overview

Understanding poverty metrics is critical for effective policymaking and socio-economic development. This repository tracks the process of taking raw, complex government data, refining it, uncovering key underlying trends, and translating those findings into an intuitive, interactive visual dashboard.

Key Objectives:

1.Clean and restructure government data for analysis.

2.Perform EDA and a dynamic dashboard to understand the data. 

3.Write a report of the findings.

🛠️ Tech Stack 

Data Source: Dataset by Open Government Data of India

Data Cleaning & EDA: Python (Pandas, Matplotlib, Seaborn).

Data Visualization: Power BI.

Google Docs for writing the report.

⚙️ Data Pipeline & Methodology

1. Data Cleaning (Python)
Raw government files often come with complex formatting. The initial processing involved:

A. Column Renaming: Standardized lengthy column headers into clean, lowercase, underscore-separated names for better readability and coding efficiency.

B. Feature Dropping: Identified and removed columns which served no purpose and columns that had "NULL" written instead of just having a blank value.

3. Exploratory Data Analysis (EDA)

Using Jupyter Notebooks, Python was leveraged to understand the underlying distributions and relationships:

A.  Analyzed state-wise poverty ratios to pinpoint high-priority regions.

B.  Visualized correlations between poverty indicators and external socio-economic factors.

C.  Generated distribution plots, bar charts, and heatmaps to reveal hidden structural patterns.

4. Dashboarding (Power BI)
The cleaned dataset was imported into Power BI to create a view of the insights:

A. Designed KPI cards for instant overviews.
B. Implemented state-by-state geographical map visualizations.
C.  Added interactive slicers (as per states/UT) allowing users to know as per specific places into specific data segments.
