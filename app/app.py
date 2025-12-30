#import streamlit as st
#import os

#st.title("Cloud-Based Distributed Data Processing Service")

#st.write("Upload a dataset in CSV, JSON, or TXT format.")

#uploaded_file = st.file_uploader(
 #   "Upload dataset",
 #   type=["csv", "json", "txt", "pdf"]
#)

#if uploaded_file is not None:
 #   file_name = uploaded_file.name
 #   file_extension = os.path.splitext(file_name)[1]

   # st.success(f"File uploaded: {file_name}")
   # st.write("File type:", file_extension)

import streamlit as st
import os

# =======================
# 🎨 تصميم الصفحة
# =======================
st.set_page_config(
    page_title="Cloud Data Processing",
    page_icon="☁️",
    layout="centered"
)

# عنوان الصفحة
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>☁️ Cloud-Based Distributed Data Processing Service</h1>",
    unsafe_allow_html=True
)
st.write("---")  # خط فاصل

# =======================
# 📂 رفع الملف بشكل جميل
# =======================
st.markdown(
    """
    <style>
    .stFileUploader > div > div > label > div {
        background-color: #4B8BBE !important;
        color: white !important;
        font-size: 18px !important;
        padding: 20px !important;
        border-radius: 12px !important;
        text-align: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "📁 Click here to upload your dataset (CSV, JSON, TXT, PDF)",
    type=["csv", "json", "txt", "pdf"],
    accept_multiple_files=False
)

# =======================
# ✅ معلومات الملف بعد الرفع
# =======================
if uploaded_file is not None:
    file_name = uploaded_file.name
    file_extension = os.path.splitext(file_name)[1]

    st.success(f"✅ File uploaded successfully: **{file_name}**")
    st.info(f"File type: `{file_extension}`")

    col1, col2 = st.columns(2)
    col1.metric("File Size (KB)", f"{round(len(uploaded_file.getbuffer())/1024, 2)} KB")
    col2.metric("Extension", file_extension)
