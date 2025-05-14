# 🌳 Carbon Sequestration in Woodland City of London

**Author**: Kamran Ali  
**M.Sc. Data Science**  
**University of Surrey, United Kingdom**

[Download PDF](../assets/Portfolio_Project_Report.pdf)
---

## 📆 Table of Contents

1. [Introduction](#1-introduction)  
2. [Literature Review](#2-literature-review)  
3. [Methodology](#3-methodology)  
4. [Data Analysis & Results](#4-data-analysis--results)  
5. [Results Discussion](#5-results-discussion)  
6. [Conclusion](#6-conclusion)  
7. [Recommendations and Shortcomings](#7-recommendations-and-shortcomings)  
8. [Way Forward](#8-way-forward)  
9. [Bibliography](#9-bibliography)  

---

## 1. Introduction

### 1.1 Background
Urbanization and environmental change are reshaping cities worldwide. As urban areas expand, so does their contribution to greenhouse gas emissions. Urban forestry is emerging as a vital solution, offering a natural method for CO2 capture. In cities like London, with extensive green networks, trees play a key role in reducing carbon and supporting biodiversity.

### 1.2 Problem Statement
Despite known benefits, the **carbon sequestration capacity** of urban forests in London remains under-analyzed. There's a need for comprehensive data and evaluation of species-specific contributions and management practices.

### 1.3 Research Objectives
- Assess carbon stocks in urban forests.  
- Explore biodiversity's influence on carbon capture.  
- Evaluate existing management practices.  
- Offer practical and policy-based recommendations.

### 1.4 Research Questions
- What are the key emission sources in London's urban forests?  
- How much carbon do these forests store?  
- How does biodiversity impact sequestration?  
- What is the role of current management strategies?

### 1.5 Importance of Study
This research provides critical insights for environmental managers, policymakers, and urban planners. It highlights the carbon and economic benefits of urban trees while promoting sustainable development.

### 1.6 Structure of Report
The report is structured into chapters covering the introduction, literature, methodology, analysis, discussion, and conclusions with recommendations.

---

## 2. Literature Review
- Emphasizes the carbon capture potential of UK woodlands.  
- Discusses policy relevance and economic valuation of tree-based ecosystem services.  
- Reviews studies on climate change, urban forestry, and sustainable planning.  
- Highlights global efforts in reforestation and afforestation for climate resilience.

---

## 3. Methodology

### 3.1 Approach
Used **CRISP-DM** (Cross-Industry Standard Process for Data Mining):
- Business Understanding  
- Data Understanding  
- Data Preparation  
- Modeling (Regression, Random Forest)  
- Evaluation  
- Deployment

### 3.2 Tools & Sources
- **Python** (Pandas, Seaborn, Scikit-Learn)  
- **Excel**  
- **Data Sources**: i-Tree Eco Project, ECAD, GOV.UK, EEA

### 3.3 Analytical Methods
- Exploratory Data Analysis (EDA)  
- Correlation & Multivariate Regression  
- Random Forest modeling  
- Emission value assessment and pollutant analysis  
- Climate and weather data integration

---

## 4. Data Analysis & Results

### 4.1 Emission Trends
- CO2 emissions in London dropped from **51 Mt (2000)** to **28 Mt (2020)**.  
- Major emission sources: Domestic, Industrial, Transport.  
- Cleaner fuels and efficiency gains driving reduction.

### 4.2 Tree Resources
- London has **8.4 million trees**, with 21% canopy cover.  
- Trees remove over **2,200 tons** of pollutants annually.  
- **Value of carbon stored**: ~**£147 million**.  
- Tree services (cooling, air purification): worth over **£200 million/year**.

### 4.3 Tree Species Composition
- Common species: Sycamore, English Oak, Silver Birch, Hawthorn.  
- Diversity highest in Greater London; supports ecosystem resilience.

### 4.4 Pollution Removal Value (Annually)

| Pollutant | Inner London | Outer London | Greater London |
|----------|--------------|--------------|----------------|
| CO       | £10,360     | £19,561     | £29,921        |
| NO2      | £28.4M      | £26.5M      | £54.9M         |
| PM10     | £28.6M      | £34.7M      | £63.3M         |

### 4.5 Cost & Energy Savings
- Trees near buildings reduce heating/cooling costs.  
- Greater London annual savings: **£315,477**.  
- Reduced carbon footprint from lower energy use.

### 4.6 Weather & CO2 Correlation
- Max Temperature negatively correlated with CO2 (-0.54).  
- Cloud cover and particulate matter significantly influence local climate.  
- Correlation Heatmap & Matrix used for visual insight.

### 4.7 Regression Analysis
- **OLS Regression**: R² = 0.96 (excellent fit).  
- **Random Forest**: MSE = 0.57; R² = -0.23 (less accurate).  
- Temperature trends influenced by CO2, cloud cover, sunshine, and radiation.

---

## 5. Results Discussion
- London's CO2 emissions are decreasing, thanks to cleaner energy and green infrastructure.  
- Urban forests significantly contribute to pollutant removal and energy savings.  
- Strong evidence supports policy focus on expanding tree cover and improving biodiversity.

---

## 6. Conclusion
Urban woodlands are **critical natural assets**. London's green infrastructure removes pollutants, stores carbon, cools buildings, and enhances biodiversity. With smart data-driven strategies, their role in climate adaptation can be amplified.

---

## 7. Recommendations and Shortcomings

### Recommendations:
- Increase species diversity in urban planting.  
- Prioritize afforestation in high-emission areas.  
- Integrate urban forestry into city planning.

### Shortcomings:
- Some datasets lacked granularity.  
- Future models should integrate socio-economic and behavioral factors.

---

## 8. Way Forward
- Develop predictive models using real-time satellite and IoT data.  
- Engage communities in tree stewardship.  
- Expand research into ecosystem service valuation.

---

## 9. Bibliography
- London i-Tree Eco Project  
- OurWorldInData.org  
- ECAD.eu  
- Data.gov.uk  
- Academic and policy publications on urban forestry and carbon sequestration
