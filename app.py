# ✅ تثبيت Streamlit و Cloudflare Tunnel
!pip install streamlit -q
!wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
!chmod +x cloudflared

# ✅ إنشاء ملفات البيانات
with open("digital_long_clean.csv", "w", encoding="utf-8") as f:
    f.write("""السنة,الدولة,المؤسسات,البنية التحتية,التعليم/ القوى العاملة,الحكومة الالكترونية,الابتكار,الجهوزية والمعرفة التكنولوجية,تطور الاسولق /بيئة العمل,نمو السوق المالي,التنمية المستدامة,مؤشر الاقتصاد الرقمي
2018,ليبيا,26.24,27.69,36.62,39.33,29.1,40.35,27.96,29.16,14.81,30
2018,الامارات,5.83,78.38,79.04,82.92,65.26,82.65,67.07,64.38,64.38,75
2018,نونس,48.42,45.45,58.93,62.54,39.39,53.56,53.1,40.42,63.23,51
2018,السعودية,55.72,62.68,66.01,78.04,49.31,69.31,66.03,52.5,71.46,63
2018,مصر,38.47,45.03,40.07,48.8,35.1,50.22,56.27,48.12,62.14,47
2020,ليبيا,5.11,20.72,42.56,11.95,16.07,5.18,19.97,18.84,46.65,17
2020,الامارات,74.73,94.06,73.74,71.64,40.92,20.54,58.06,72.93,74.32,70
2020,نونس,47.7,43.68,61.64,50.75,28.2,13,36.5,48.65,56.67,44
2020,السعودية,55.18,65.91,77.06,70.65,43.4,15.83,45.69,70.85,60.61,59
2020,مصر,42.77,40.46,54.59,51.95,32.62,14.75,36.64,51.23,52.22,42
2022,ليبيا,32.96,12.83,35.17,20.05,27.34,6.52,22.29,32.58,23.55,23
2022,الامارات,65.69,71.83,98.28,73.2,63.94,28.35,73.67,85.45,73.21,71
2022,نونس,63.15,37.48,58.04,65.26,44.66,21.38,59,57.11,70.15,54
2022,السعودية,65.4,57.55,76.97,80.24,61.37,20.85,73.6,82.77,75.93,66
2022,مصر,50.82,39.25,59.33,55.27,47.1,20.66,64.9,66.56,65.77,52
2024,ليبيا,7,26,12,34,10,20,25,6,20,21
2024,الامارت,67,88,55,90,61,86,69,72,77,75
2024,تونس,46,49,49,65,23,55,69,18,75,50
2024,السعودية,54,82,69,85,49,78,56,81,78,72
2024,مصر,35,58,39,59,28,64,51,22,67,50
""")

with open("knowledge_long_clean.csv", "w", encoding="utf-8") as f:
    f.write("""السنة,الدولة,التعليم قبل الجامعي,التعليم التقني والتدريب المهني,التعليم العالي,البحث والتطوير والابتكار,تكنولوجيا المعلومات والاتصالات,الاقتصاد,البيئة التمكينية
2020,ليبيا,40,30,25,20,35,45,28
2020,الامارات,85,75,80,70,90,88,82
2020,السعودية,70,65,68,60,75,72,70
2020,مصر,55,50,52,45,60,58,55
2022,ليبيا,42,32,28,22,38,48,30
2022,الامارات,88,78,82,72,92,90,85
2022,السعودية,73,68,70,62,78,75,72
2022,مصر,58,53,55,47,63,60,58
""")

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
