
# 📊 Automated EDA (Exploratory Data Analysis)

**Automated EDA** is a Python-based tool designed to automate the process of Exploratory Data Analysis (EDA). This project provides a streamlined solution for generating comprehensive reports, visualizing distributions, and performing preliminary data preprocessing—all with minimal effort from the user. Built with `Streamlit` for an intuitive and interactive web interface, this tool enables data scientists and analysts to quickly understand the structure and nuances of their data.

---

## ✨ Features

- **Data Summary**: Automatically generate a summary of the dataset, including:
  - Number of rows and columns
  - Missing values detection
  - Basic statistics (mean, median, standard deviation, etc.)

- **Visualizations**:
  - Count plots for categorical variables.
  - Histograms and box plots for numerical variables.
  - Correlation matrix heatmaps for numeric features.
  - Dependency and relationship plots between features.

- **Preprocessing**:
  - Option to perform basic data preprocessing, such as handling missing values or removing duplicates.

- **Streamlit Integration**:
  - A user-friendly web interface built with `Streamlit`, allowing interactive exploration of your data without writing additional code.

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have the following installed:

- Python 3.7+
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/)
- [Streamlit](https://streamlit.io/)

### Installation
1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/automated-eda.git
    cd automated-eda
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Open your web browser and navigate to `http://localhost:8501` to use the app.

---

## 🔧 Usage

1. **Upload a Dataset**: After launching the app, upload your CSV dataset.
2. **Explore the Data**: View the summary of the data including types, missing values, and basic statistics.
3. **Choose Columns for Analysis**: Select columns from the dropdown to generate relevant statistics and plots.
4. **Visualize Relationships**: Explore the relationships between different features via correlation matrices and scatter plots.
5. **Data Preprocessing**: Use the preprocessing features to handle missing data or prepare the dataset for further analysis.

---

## 📦 Project Structure

```
automated-eda/
│
├── src/
│   ├── app.py                 # Main file for running the Streamlit app
│   ├── column_selector.py     # Column selection and statistics
│   ├── preprocessing.py       # Basic preprocessing (missing values, duplicates)
│   ├── summary.py             # Data summary logic
│   └── visualization.py       # Plotting functions (histograms, boxplots, heatmaps)
│
├── requirements.txt           # Dependencies
├── README.md                  # This file
└── data/                      # Sample datasets
```

---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `Pandas` for data manipulation and analysis.
  - `NumPy` for numerical operations.
  - `Plotly` for visualizations.
  - `Streamlit` for building an interactive web interface.

---

## 👨‍💻 Author

Developed by **[Michał Piechota]**