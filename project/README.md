# **Analyzing Global Protests and Democracy Since 1990**
Author: Myles Henehan, Atlantic Technological University
Module: Programming for Data Analytics

## Introduction
This project explores the intersection of global protest movements and democracy using data from 1990 to 2019. Two primary datasets were utilised:

1. **Mass Mobilization Data**: Covers 162 countries from 1990 to 2019, documenting aspects such as protester demands, government responses, locations, and protester identities.
2. **Varieties of Democracy (V-Dem) Dataset**: Measures five principles of democracy — electoral, liberal, participatory, deliberative, and egalitarian. The analysis focuses on the 1990-2019 period to align with the Mass Mobilization dataset.

The datasets were used to explore relationships between protests and socio-political conditions, providing insights into trends, patterns, and correlations.

## Project Directory Structure
```
project-directory/
├── project.ipynb        # The main Jupyter Notebook
├── README.md            # Project documentation
├── .gitignore           # Git configuration to exclude unnecessary files
├── data/                # Directory containing datasets
│   ├── massmobilization.csv
│   ├── v-dem.csv.gz
├── vdem_data.db      # SQLite database file
```

## Analysis Conducted
- **Data Cleaning and Preprocessing**:
  - Addressed missing values.
  - Aligned timeframes and standardised country names.
- **Exploratory Data Analysis (EDA)**:
  - Examined trends in global protests over time.
  - Investigated protester demands.
  - Visualised democratic indices and their changes across regions.
- **Correlation Analysis**:
  - Studied relationships between democratic principles and protest frequency.
- **Regional Comparisons**:
  - Compared protest activities and democratic scores across countries.

## Caveats
- The accuracy of the analysis depends on the reliability of the datasets.
- Correlation does not imply causation; further investigation is needed for causal inferences.

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
- Luo, S., 2024. Protests from 1990 to March 2020 Dataset. Available at: https://www.kaggle.com/datasets/mysterymeatie/protests-from-1990-to-march-2020/data (Accessed: 2 January 2025).
- Kaggle, 2025. Step-by-Step ML: Linear Regression. Available at: https://www.kaggle.com/code/nargisbegum82/step-by-step-ml-linear-regression (Accessed: 12 January 2025).
- Matplotlib, 2024. Pie and Donut Labels. Available at: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html (Accessed: 3 January 2025).
- OpenAI, 2025. ChatGPT. Available at: https://openai.com/chatgpt (Accessed: 12 January 2025).
- Proclus Academy, 2025. Customize Matplotlib Pie Chart. Available at: https://proclusacademy.com/blog/customize_matplotlib_piechart/ (Accessed: 12 January 2025).
- Python Graph Gallery, 2021. Line chart with dual Y-axis in Matplotlib. Available at: https://python-graph-gallery.com/line-chart-dual-y-axis-with-matplotlib/#:~:text=The%20first%20axis%20has%20a,twinx()%20.&text=As%20can%20be%20seen%20above,goes%20from%204%20to%2020 [Accessed 8 January 2025].
- Scikit-learn. (n.d.) Model selection. Available at: https://scikit-learn.org/stable/model_selection.html (Accessed: 12 January 2025).
- V-Dem Institute, 2025. V-Dem Dataset Version 14. Available at: https://v-dem.net/data/the-v-dem-dataset/ (Accessed: 2 January 2025).
