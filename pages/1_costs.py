import streamlit as st
import pandas as pd
from utils.helpers import read_df, write_df

def render():
    st.header("🧮 حساب التكاليف")
    df = read_df("tasks.xlsx")
    st.dataframe(df)
    with st.form("cost_form"):
        name = st.text_input("اسم المهمة")
        qty = st.number_input("العدد", min_value=1, step=1)
        price = st.number_input("سعر الوحدة", min_value=0.0, format="%.2f")
        if st.form_submit_button("أضف المهمة"):
            cost = qty * price
            df.loc[len(df)] = [name, qty, price, cost]
            write_df(df, "tasks.xlsx")
            st.experimental_rerun()
    if not df.empty:
        total = df["التكلفة"].sum()
        area = st.number_input("مساحة المشروع (م²)", min_value=0.1, format="%.2f")
        if area:
            st.markdown(f"**التكلفة الكلية:** {total:.2f}")
            st.markdown(f"**التكلفة لكل متر مربع:** {total/area:.2f}")
