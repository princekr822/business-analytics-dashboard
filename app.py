import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from report_generator import *

st.set_page_config(page_title="Business Report Dashboard", layout="wide")

st.title("📊 Visualization Based Business Report")

uploaded_file = st.file_uploader("Upload your business data (CSV)", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)

    st.subheader("📌 Data Preview")
    st.dataframe(df)

    st.subheader("📊 Key Performance Indicators")
    sales, profit, orders = get_kpis(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"₹{sales}")
    col2.metric("Total Profit", f"₹{profit}")
    col3.metric("Total Orders", orders)

    st.subheader("🌍 Sales by Region")
    region_data = sales_by_region(df)
    fig1 = px.bar(region_data, x='Region', y='Sales', color='Region')
    st.plotly_chart(fig1)

    st.subheader("📦 Profit by Product")
    product_data = profit_by_product(df)
    fig2 = px.pie(product_data, names='Product', values='Profit')
    st.plotly_chart(fig2)

    st.subheader("📈 Sales Over Time")
    fig3 = px.line(df, x='Date', y='Sales')
    st.plotly_chart(fig3)

    st.subheader("🔥 Correlation Heatmap")
    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    st.pyplot(plt)

else:
    st.info("Please upload a CSV file to generate report.")