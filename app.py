import streamlit as st
from utils.helpers import init_data_files
from pages import _1_costs, _2_documentation, _3_invoices, _4_project_phases

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

if page == "🧮 حساب التكاليف":
    _1_costs.app()
elif page == "📸 توثيق المشروع":
    _2_documentation.app()
elif page == "📄 توثيق الفواتير":
    _3_invoices.app()
elif page == "📆 مراحل المشروع":
    _4_project_phases.app()
