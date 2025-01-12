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


## **List of References:**
***
- Alaş, B., 2020. Matplotlib: A Complete Data Visualization Guide. Kaggle. Available at: https://www.kaggle.com/code/berkayalan/matplotlib-a-complete-data-visualization-guide [Accessed 12 January 2025].
- CareerFoundry, 2024. Open Data Sources. Available at: https://careerfoundry.com/en/blog/data-analytics/open-data-sources/ (Accessed: 26 December 2024).
- Clark, D. and Regan, P., 2021. Mass Mobilization Protest Data. Harvard Dataverse. Available at: https://doi.org/10.7910/DVN/HTTWYL (Accessed: 3 January 2025).
- DataCamp, 2025. Python: Round to Two Decimal Places. Available at: https://www.datacamp.com/tutorial/python-round-to-two-decimal-places (Accessed: 12 January 2025).
- DataCamp, 2025. Pandas Sort Values. Available at: https://www.datacamp.com/tutorial/pandas-sort-values?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157156376311&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=726015683493&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9197253&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-jan25&gad_source=1&gclid=CjwKCAiA7Y28BhAnEiwAAdOJUGLgHgAAxvWLYXa8VglE5eQeU_Aek6ssoVyr3tnttGscpmGmLSAicBoC56sQAvD_BwE (Accessed: 12 January 2025).
- FavTutor, 2025. Convert Pandas Series to DataFrame. Available at: https://favtutor.com/articles/convert-pandas-series-to-dataframe/ (Accessed: 3 January 2025).
- GeeksforGeeks, 2025. Boolean Indexing in Pandas. Available at: https://www.geeksforgeeks.org/boolean-indexing-in-pandas/ (Accessed: 3 January 2025).
- GeeksforGeeks, 2025. Change the X or Y ticks of a Matplotlib figure. Available at: https://www.geeksforgeeks.org/change-the-x-or-y-ticks-of-a-matplotlib-figure/ [Accessed 12 January 2025].
- Kaggle, 2025. Protests from 1990 to March 2020 Dataset. Available at: https://www.kaggle.com/datasets/mysterymeatie/protests-from-1990-to-march-2020/data (Accessed: 2 January 2025).
- Kaggle, 2025. Step-by-Step ML: Linear Regression. Available at: https://www.kaggle.com/code/nargisbegum82/step-by-step-ml-linear-regression (Accessed: 12 January 2025).
- Matplotlib, 2024. Pie and Donut Labels. Available at: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html (Accessed: 3 January 2025).
- OpenAI, 2025. ChatGPT. Available at: https://openai.com/chatgpt (Accessed: 12 January 2025).
- Proclus Academy, 2025. Customize Matplotlib Pie Chart. Available at: https://proclusacademy.com/blog/customize_matplotlib_piechart/ (Accessed: 12 January 2025).
- Python Graph Gallery, 2021. Line chart with dual Y-axis in Matplotlib. Available at: https://python-graph-gallery.com/line-chart-dual-y-axis-with-matplotlib/#:~:text=The%20first%20axis%20has%20a,twinx()%20.&text=As%20can%20be%20seen%20above,goes%20from%204%20to%2020 [Accessed 8 January 2025].
- V-Dem Institute, 2025. V-Dem Dataset Version 14. Available at: https://v-dem.net/data/the-v-dem-dataset/ (Accessed: 2 January 2025).
