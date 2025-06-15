import streamlit as st
from utils.helpers import read_df, write_df
import os

def render():
    st.header("📸 توثيق المشروع")
    uploaded = st.file_uploader("اختر صورة", type=["jpg","png"])
    desc = st.text_input("الوصف")
    date = st.date_input("التاريخ")
    if st.button("رفع"):
        if uploaded and desc:
            path = os.path.join("data/documentation", uploaded.name)
            with open(path, "wb") as f: f.write(uploaded.getbuffer())
            st.success("تم الرفع")
    files = os.listdir("data/documentation")
    st.subheader("الصور المرفوعة")
    for fn in files:
        st.image(os.path.join("data/documentation", fn), caption=fn, width=200)
        if st.button(f"حذف {fn}"):
            os.remove(os.path.join("data/documentation", fn))
            st.experimental_rerun()
