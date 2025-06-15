import streamlit as st
from pages import _init_pages  # يستدعى صفحات المشروع
from utils.helpers import init_data_files

st.set_page_config(page_title="🏗️ تطبيق توثيق مشروع بناء عمارة", layout="wide")

# التأكد من وجود ملفات البيانات المحلية
init_data_files()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
html, body, [class*="css"] { direction: rtl; font-family: 'Cairo', sans-serif; background-color: #f9f9f9; }
</style>
""", unsafe_allow_html=True)

st.title("🏗️ تطبيق توثيق مشروع بناء عمارة")
st.caption("إعداد: أنس الراجح")

page = st.sidebar.radio("🔹 اختر صفحة:", [
    "🧮 حساب التكاليف",
    "📸 توثيق المشروع",
    "📄 توثيق الفواتير",
    "📆 مراحل المشروع"
])

_init_pages(page)
