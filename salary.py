import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Salary Dashboard",
    layout="wide"
)

st.title("💼 Employee Salary Dashboard")
st.write("A simple data product built using Streamlit.")

# -------------------------
# Load Dataset
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("salary.csv")

df = load_data()

# -------------------------
# Display Dataset
# -------------------------
st.header("Dataset")

st.dataframe(df, use_container_width=True)

# -------------------------
# Dataset Information
# -------------------------
st.header("Dataset Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())

st.write(df.describe())

# -------------------------
# Sidebar Filter
# -------------------------
st.sidebar.header("Filter")

numeric_columns = df.select_dtypes(include="number").columns.tolist()

selected_column = st.sidebar.selectbox(
    "Choose Numeric Column",
    numeric_columns
)

# -------------------------
# Histogram
# -------------------------
st.header(f"Distribution of {selected_column}")

fig, ax = plt.subplots(figsize=(7,4))
df[selected_column].hist(
    bins=20,
    ax=ax
)

ax.set_xlabel(selected_column)
ax.set_ylabel("Frequency")

st.pyplot(fig)

# -------------------------
# Correlation Heatmap
# -------------------------
st.header("Correlation Heatmap")

fig2, ax2 = plt.subplots(figsize=(8,6))

corr = df.corr(numeric_only=True)

im = ax2.imshow(corr)

ax2.set_xticks(range(len(corr.columns)))
ax2.set_xticklabels(corr.columns, rotation=90)

ax2.set_yticks(range(len(corr.columns)))
ax2.set_yticklabels(corr.columns)

plt.colorbar(im)

st.pyplot(fig2)

# -------------------------
# Raw Statistics
# -------------------------
st.header("Statistics")

st.dataframe(df.describe())

# -------------------------
# Download Dataset
# -------------------------
csv = df.to_csv(index=False)

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="salary.csv",
    mime="text/csv"
)