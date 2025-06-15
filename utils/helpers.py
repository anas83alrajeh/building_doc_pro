import os
import pandas as pd

def init_data_files():
    os.makedirs("data/documentation", exist_ok=True)
    os.makedirs("data/invoices", exist_ok=True)
    files = {
        "tasks.xlsx": ["اسم المهمة","العدد","سعر الوحدة","التكلفة"],
        "invoices.xlsx": ["اسم الفاتورة","التاريخ","القيمة","اسم الملف"],
        "project_phases.xlsx": ["المرحلة","نسبة المرحلة","تاريخ البداية","تاريخ النهاية","تم التنفيذ","مدة التنفيذ (أيام)"]
    }
    for name, cols in files.items():
        path = os.path.join("data", name)
        if not os.path.exists(path):
            pd.DataFrame(columns=cols).to_excel(path, index=False)

def read_df(name):
    return pd.read_excel(os.path.join("data", name))

def write_df(df, name):
    df.to_excel(os.path.join("data", name), index=False)
# Helper functions for Excel and Google Drive API
