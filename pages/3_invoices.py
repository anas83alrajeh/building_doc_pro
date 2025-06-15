import streamlit as st
import os
from utils.helpers import read_df, write_df

def render():
    st.header("📄 توثيق الفواتير")
    df = read_df("invoices.xlsx")
    uploaded = st.file_uploader("ارفق فاتورة", type=["jpg","png"])
    name = st.text_input("اسم الفاتورة")
    date = st.date_input("التاريخ")
    value = st.number_input("القيمة", min_value=0.0, format="%.2f")
    if st.button("إضافة"):
        if uploaded and name and value:
            fn = uploaded.name; path = os.path.join("data/invoices", fn)
            with open(path, "wb") as f: f.write(uploaded.getbuffer())
            df.loc[len(df)] = [name, date, value, fn]
            write_df(df, "invoices.xlsx")
            st.experimental_rerun()
    st.dataframe(df)
    total_task = read_df("tasks.xlsx")["التكلفة"].sum()
    total_inv = df["القيمة"].sum()
    st.markdown(f"- إجمالي تكاليف: {total_task:.2f}")
    st.markdown(f"- إجمالي فواتير: {total_inv:.2f}")
    st.markdown(f"- المتبقي: {total_task-total_inv:.2f}")
