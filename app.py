# ✅ إنشاء ملف التطبيق app.py
with open("app.py", "w", encoding="utf-8") as f:
    f.write('''import streamlit as st
import pandas as pd
import base64
import altair as alt

st.set_page_config(page_title="منصة المؤشرات", layout="wide")

digital_df = pd.read_csv("digital_long_clean.csv")
knowledge_df = pd.read_csv("knowledge_long_clean.csv")

def set_background(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .main, .block-container {{
            background-color: rgba(255, 255, 255, 0.0);
        }}
        header, footer {{
            background-color: rgba(255, 255, 255, 0.0);
        }}
        .dataframe th, .dataframe td {{
            font-size: 18px !important;
        }}
        label, .stSelectbox label, .stMarkdown p {{
            font-size: 20px !important;
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# Assuming PIC11.jpg is available in the same directory
# You might need to upload this image to your Colab environment
set_background("PIC11.jpg")

st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: rgba(0, 0, 0, 0.6); color: white; border-radius: 10px;'>
        <h1 style='margin-bottom: 0;'>منصة المؤشرات الرقمية والمعرفية</h1>
        <p style='margin-top: 5px;'>تحليل تفاعلي ومقارن للمؤشرات الوطنية</p>
    </div>
""", unsafe_allow_html=True)

indicator_type = st.selectbox("اختر نوع المؤشر", ["الاقتصاد الرقمي", "المعرفة"])
df = digital_df if indicator_type == "الاقتصاد الرقمي" else knowledge_df

year_col = [col for col in df.columns if "السنة" in col][0]
country_col = [col for col in df.columns if "الدولة" in col][0]

col1, col2, col3 = st.columns(3)
with col1:
    country1 = st.selectbox("الدولة الأولى", sorted(df[country_col].unique()), key="c1")
with col2:
    country2 = st.selectbox("الدولة الثانية", sorted(df[country_col].unique()), key="c2")
with col3:
    year = st.selectbox("اختر السنة", sorted(df[year_col].unique()), key="y")

df1 = df[(df[country_col] == country1) & (df[year_col] == year)]
df2 = df[(df[country_col] == country2) & (df[year_col] == year)]

id_vars = [year_col, country_col]
value_vars = [col for col in df.columns if col not in id_vars]
long1 = df1.melt(id_vars=id_vars, value_vars=value_vars, var_name="المؤشر", value_name="القيمة1")
long2 = df2.melt(id_vars=id_vars, value_vars=value_vars, var_name="المؤشر", value_name="القيمة2")

merged = pd.merge(long1, long2, on="المؤشر", suffixes=('_الدولة_الأولى', '_الدولة_الثانية'))
merged['الفرق'] = merged['القيمة1'] - merged['القيمة2']

st.subheader(f"مقارنة المؤشرات بين {country1} و {country2} لعام {year}")

# Display the comparison table
st.dataframe(merged[['المؤشر', 'القيمة1', 'القيمة2', 'الفرق']].set_index('المؤشر'))

# Create a chart to visualize the difference
chart = alt.Chart(merged).mark_bar().encode(
    x=alt.X('المؤشر:N', sort='-y'),
    y=alt.Y('الفرق:Q'),
    tooltip=['المؤشر', 'القيمة1', 'القيمة2', 'الفرق']
).properties(
    title=f'الفرق في المؤشرات بين {country1} و {country2} لعام {year}'
).interactive()

st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>تم تطوير هذه المنصة باستخدام Streamlit و Pandas</p>", unsafe_allow_html=True)
''')
