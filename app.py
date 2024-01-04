import streamlit as st

st.set_page_config(page_title="CSV Data Analyzing Tool")
st.title("CSV Data Analyzing Tool...💁 ")
st.subheader("I can help you in performing Data Analysis on a CSV File ")


# Upload the file (csv files)
pdf = st.file_uploader("Upload CSV files here", type=["csv"],accept_multiple_files=True)

submit=st.button("Analyze Data")

if submit:
    st.write("Response")
