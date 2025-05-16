import streamlit as st
import pandas as pd

# Đọc file Excel
df = pd.read_excel("dulieu.xlsx", sheet_name="Du lieu ST")

st.title("🔍 Tra cứu thông tin theo mã khuôn")

# Nhập mã khuôn
keyword = st.text_input("Nhập mã khuôn (ví dụ: BR0356):")

if keyword:
    result = df[df['PART NO'].str.contains(keyword, case=False, na=False)]

    if result.empty:
        st.warning("Không tìm thấy kết quả.")
    else:
        st.subheader("📄 Kết quả tìm được:")
        st.dataframe(result[['PART NO', 'PART NAME', 'CÔNG ĐOẠN', 'ST man', 'ST máy']])

        st.markdown(f"### 📊 Tổng ST man: `{result['ST man'].sum():.5f}`")
        st.markdown(f"### ⚙️ Tổng ST máy: `{result['ST máy'].sum():.5f}`")
