import streamlit as st
import pandas as pd
from utils.helpers import read_df, write_df

def render():
    st.header("📆 مراحل المشروع")
    df = read_df("project_phases.xlsx")
    if df.empty:
        phases = ["تحديد الأرض", "استخراج التراخيص", ... "إعداد تقرير التسليم"]
        df = pd.DataFrame({"المرحلة": phases, "نسبة المرحلة":[10]*10, "تاريخ البداية":[""]*10,
                           "تاريخ النهاية":[""]*10, "تم التنفيذ":[False]*10, "مدة التنفيذ (أيام)":[0]*10})
    total = 0
    with st.form("phases"):
        for i in df.index:
            start = st.date_input(f"{df.at[i,'المرحلة']} بداية", key=f"s{i}")
            end = st.date_input(f"{df.at[i,'المرحلة']} نهاية", key=f"e{i}")
            done = st.checkbox("تم التنفيذ", df.at[i,"تم التنفيذ"], key=f"d{i}")
            dur = (end - start).days if start and end else 0
            df.at[i, "تاريخ البداية"] = str(start)
            df.at[i, "تاريخ النهاية"] = str(end)
            df.at[i, "تم التنفيذ"] = done
            df.at[i, "مدة التنفيذ (أيام)"] = dur
            if done: total += df.at[i,"نسبة المرحلة"]
        if st.form_submit_button("حفظ"):
            write_df(df, "project_phases.xlsx")
            st.success(f"نسبة الإنجاز: {total}%")
            st.progress(total)
            st.experimental_rerun()
