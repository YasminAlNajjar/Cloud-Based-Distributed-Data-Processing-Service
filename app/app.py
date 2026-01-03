# import streamlit as st
# import os

# =======================
#  تصميم الصفحة
# =======================
# st.set_page_config(
#     page_title="Cloud Data Processing",
#     page_icon="☁️",
#     layout="centered"
# )

# عنوان الصفحة
# st.markdown(
#     "<h1 style='text-align: center; color: #4B8BBE;'>☁️ Cloud-Based Distributed Data Processing Service</h1>",
#     unsafe_allow_html=True
# )
# st.write("---")  # خط فاصل

# =======================
#  رفع الملف 
# =======================
# st.markdown(
#     """
#     <style>
#     .stFileUploader > div > div > label > div {
#         background-color: #4B8BBE !important;
#         color: white !important;
#         font-size: 18px !important;
#         padding: 20px !important;
#         border-radius: 12px !important;
#         text-align: center !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# uploaded_file = st.file_uploader(
#     "📁 Click here to upload your dataset (CSV, JSON, TXT, PDF)",
#     type=["csv", "json", "txt", "pdf"],
#     accept_multiple_files=False
# )

# # =======================
# # معلومات الملف بعد الرفع
# # =======================
# if uploaded_file is not None:
#     file_name = uploaded_file.name
#     file_extension = os.path.splitext(file_name)[1]

#     st.success(f"✅ File uploaded successfully: **{file_name}**")
#     st.info(f"File type: `{file_extension}`")


import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from io import StringIO

st.title("Cloud-Based Data Processing Demo")

# -----------------------
# 1️⃣ رفع الملف
# -----------------------
uploaded_file = st.file_uploader("Upload your dataset (CSV, JSON, TXT)", type=["csv","json","txt"])

if uploaded_file:
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # قراءة البيانات
    if uploaded_file.name.endswith(".csv") or uploaded_file.name.endswith(".txt"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".json"):
        df = pd.read_json(uploaded_file)
    else:
        st.error("Unsupported file format!")
        st.stop()

    # -----------------------
    # 2️⃣ عرض معاينة البيانات
    # -----------------------
    st.write("### Preview of the dataset")
    st.dataframe(df.head())

    # -----------------------
    # 3️⃣ Descriptive Statistics
    # -----------------------
    st.write("### Descriptive Statistics")
    st.write(f"- Number of rows: {df.shape[0]}")
    st.write(f"- Number of columns: {df.shape[1]}")
    st.write("- Column data types:")
    st.write(df.dtypes)
    st.write("- Missing values % per column:")
    st.write(df.isnull().mean() * 100)
    st.write("- Unique values per column:")
    st.write(df.nunique())
    st.write("- Min/Max/Mean for numeric columns:")
    st.write(df.describe().T[['min','max','mean']])

    # -----------------------
    # 4️⃣ Simple ML Jobs (if numeric columns >=2)
    # -----------------------
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        st.write("### Linear Regression (first numeric column as target)")
        X = df[numeric_cols[1:]]
        y = df[numeric_cols[0]]
        lr = LinearRegression().fit(X, y)
        st.write(f"Coefficients: {lr.coef_}")
        st.write(f"Intercept: {lr.intercept_}")

        st.write("### KMeans Clustering (3 clusters)")
        km = KMeans(n_clusters=3, random_state=42)
        df['cluster'] = km.fit_predict(df[numeric_cols])
        st.dataframe(df.head())

    # -----------------------
    # 5️⃣ تنزيل النتائج
    # -----------------------
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name="processed_results.csv",
        mime='text/csv'
    )

