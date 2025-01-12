# **Analyzing Global Protests and Democracy Since 1990**

## **Overview**
This project explores two datasets to understand global protests and their relationship with democratic indicators. By combining data on mass mobilization with governance metrics, this analysis investigates patterns, trends, and correlations between protests and socio-political conditions.

## **Datasets**
### 1. **Mass Mobilization Dataset**
- **Focus**: Tracks protest events globally, capturing information on their type, scale, and outcomes.
- **Key Features**:
  - Dates and locations of protests.
  - Types of demands made (e.g., economic, political, social).
  - Government responses to protests.

### 2. **V-Dem Dataset (Varieties of Democracy)**
- **Focus**: Measures the quality and characteristics of democracy in different countries.
- **Key Features**:
  - Indicators of democratic governance (e.g., electoral integrity, civil liberties).
  - Political participation and freedom of expression.
  - Trends in authoritarian practices.

## **Objective**
To examine the relationship between the number of protests in a country and key democratic indicators, such as freedom of expression and government accountability, and to identify trends over time.

## **Key Steps**
1. **Data Cleaning and Preprocessing**:
   - Filtered incomplete rows and removed irrelevant data (e.g., protests marked as `0` or incomplete 2020 data).
   - Standardized country names for compatibility across datasets.
   
2. **Visualization and Analysis**:
   - Created scatter plots to compare protest frequency with democratic indicators (e.g., freedom of expression, Liberal Democracy Index).
   - Fit regression models to analyze trends and predict future protest levels.
   - Explored correlations between protests and democratic quality.

3. **Focus Period**:
   - Analysis centers on the years 1990–2019.
   - Option to narrow the scope to specific decades or regions.

## **Libraries Used**
- **Pandas**: Data manipulation and analysis.
- **Matplotlib & Seaborn**: Visualization.
- **NumPy**: Numerical computations.
- **Scikit-learn**: Regression modeling.

## **Key Findings**
- Demonstrated the relationship between protest levels and governance indicators.
- Identified countries with high protest frequencies and varying levels of democracy.
- Highlighted trends in protest activity over the decades.

## **Usage**
This project provides a framework for researchers and policymakers to:
- Examine trends in global protests.
- Investigate how governance affects public mobilization.
- Use predictive models to anticipate future protest activity.

## **Getting Started**
1. Clone the repository or download the project files.
2. Ensure the following dependencies are installed:
   ```bash
   pip install pandas matplotlib seaborn numpy scikit-learn
   ```
3. Run the Jupyter notebook to reproduce the analysis and visualizations.

## **Potential Extensions**
- Expanding the analysis to include more variables, such as economic indicators or social inequality metrics.
- Performing region-specific or country-specific deep dives.
- Incorporating data for 2020 and beyond to account for the impact of COVID-19 on protests.

***

List of References:
- https://careerfoundry.com/en/blog/data-analytics/open-data-sources/ (Accessed 26 December 2024).
- https://www.kaggle.com/datasets/mysterymeatie/protests-from-1990-to-march-2020/data (Accessed 2 January 2025)
- Clark, David; Regan, Patrick, 2016, "Mass Mobilization Protest Data", https://doi.org/10.7910/DVN/HTTWYL, Harvard Dataverse, V5, UNF:6:F/k8KUqKpCa5UssBbL/gzg== [fileUNF] (Accessed 3 January 2025)
- https://www.geeksforgeeks.org/boolean-indexing-in-pandas/ (Accessed 3 January 2025)
- https://favtutor.com/articles/convert-pandas-series-to-dataframe/ (Accessed 3 January 2025)
- https://www.datacamp.com/tutorial/python-round-to-two-decimal-places (Accessed 12 January 2025)
- https://www.kaggle.com/code/nargisbegum82/step-by-step-ml-linear-regression