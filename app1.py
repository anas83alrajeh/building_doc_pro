import streamlit as st

st.set_page_config(page_title="🏗️ منصة إدارة وتوثيق البناء", layout="wide", page_icon="🏗️")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3132/3132693.png", width=80)
st.sidebar.title("القائمة الرئيسية")
pages = {
    "الصفحة الرئيسية": "الرئيسية",
    "المهام والمراحل": "المهام",
    "توثيق بالصور": "الصور",
    "الفواتير والتكاليف": "الفواتير",
    "إحصائيات المشروع": "الإحصائيات",
    "إدارة المستخدمين": "المستخدمين"
}
choice = st.sidebar.radio("انتقل إلى:", list(pages.keys()))

if choice == "الصفحة الرئيسية":
    st.markdown("""
    <div dir=\"rtl\" style=\"text-align:right;\">
      <h1>🏗️ منصة إدارة مشروع بناء عمارة</h1>
      <p><strong>إعداد: أنس الراجح</strong></p>
      <ul>
        <li>إدارة المهام والمراحل والفواتير</li>
        <li>توثيق بالصور والتقارير</li>
        <li>إحصائيات فورية وتنبيهات متقدمة</li>
      </ul>
      <p>🧾 استخدم القائمة الجانبية للتنقل بين الصفحات</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("إجمالي التكلفة", "120,000 ريال")
    col2.metric("عدد المهام", "24")
    col3.metric("نسبة الإنجاز", "65%")
    st.info("ابدأ في إدارة وتوثيق مشروعك بسهولة واحترافية.")

elif choice == "المهام والمراحل":
    from pages import tasks
    tasks.render()

elif choice == "توثيق بالصور":
    from pages import photos
    photos.render()

elif choice == "الفواتير والتكاليف":
    from pages import invoices
    invoices.render()

elif choice == "إحصائيات المشروع":
    from pages import stats
    stats.render()

elif choice == "إدارة المستخدمين":
    from pages import users
    users.render()