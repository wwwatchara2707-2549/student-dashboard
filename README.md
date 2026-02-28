📊 Student GPA Analytics Dashboard
🧾 Project Overview

Student GPA Analytics Dashboard เป็น Web Application ที่พัฒนาโดยใช้ Python Dash และ Plotly
เพื่อวิเคราะห์และแสดงผลข้อมูลเกรดเฉลี่ย (GPA) ของนักศึกษาแบบ Interactive

ระบบนี้ออกแบบให้ผู้ใช้สามารถ:

เลือกสาขาวิชา (Major)

กำหนดช่วง GPA

วิเคราะห์ข้อมูลผ่านกราฟ 3 รูปแบบ

โดยข้อมูลจะอัปเดตแบบ Dynamic ผ่าน Dash Callback โดยไม่ต้องรีเฟรชหน้าเว็บ

🎯 Project Objectives

สร้าง Dashboard ที่มีอย่างน้อย 3 กราฟ

มี Interactive ระหว่าง Components

ใช้ Git พร้อมหลัก Commit Early & Commit Often

มีอย่างน้อย 25 Commits

อธิบายโค้ดและวิธีรันอย่างชัดเจน

🏗 System Architecture
User Interaction (Dropdown / Slider)
            ↓
Dash Callback Function
            ↓
Data Filtering (Pandas)
            ↓
Generate Charts (Plotly Express)
            ↓
Update Graph Components
📊 Features
1️⃣ Interactive Filtering

Dropdown สำหรับเลือกสาขา

Range Slider สำหรับกำหนดช่วง GPA

ทุกกราฟอัปเดตพร้อมกันผ่าน Callback

2️⃣ Visualization (3 Graphs)

📊 Bar Chart
แสดงจำนวนผู้เรียนตามเงื่อนไขที่เลือก

📈 Line / Scatter Chart
แสดงแนวโน้มและการกระจายของ GPA

🥧 Pie Chart / Histogram
แสดงสัดส่วนหรือการกระจายข้อมูล

🛠 Technologies Used

Python 3.x

Dash

Plotly Express

Pandas

Git & GitHub

🧠 Code Explanation
1️⃣ Import Libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

Dash → สร้าง Web Application

dcc → ใช้สร้าง Interactive Components

html → ใช้จัด Layout

Pandas → จัดการข้อมูล

Plotly → สร้างกราฟ

2️⃣ Load Dataset
df = pd.read_csv("students.csv")

โหลดข้อมูลนักศึกษาจากไฟล์ CSV เพื่อนำมาใช้วิเคราะห์

3️⃣ Layout Design
app.layout = html.Div([
    dcc.Dropdown(id="major-dropdown", ...),
    dcc.RangeSlider(id="gpa-slider", ...),
    dcc.Graph(id="graph-1"),
    dcc.Graph(id="graph-2"),
    dcc.Graph(id="graph-3")
])

Layout ประกอบด้วย:

ตัวกรองข้อมูล

กราฟแสดงผล

4️⃣ Callback (Core Logic)
@app.callback(
    Output("graph-1", "figure"),
    Output("graph-2", "figure"),
    Output("graph-3", "figure"),
    Input("major-dropdown", "value"),
    Input("gpa-slider", "value")
)

ขั้นตอนการทำงาน:

รับค่าจาก Dropdown และ Slider

กรองข้อมูลด้วย Pandas

สร้างกราฟใหม่ด้วย Plotly

ส่งผลลัพธ์กลับไปแสดงบนหน้าเว็บ

Dashboard จะอัปเดตแบบ Dynamic โดยไม่ต้อง Reload หน้าเว็บ

🔄 Git Workflow

โปรเจคนี้ใช้หลักการ:

Commit Early

Commit Often

มีมากกว่า 25 Commits

สามารถตรวจสอบประวัติการพัฒนาได้ที่ GitHub Repository

🚀 Installation & Running Guide
1️⃣ Clone Repository
git clone <YOUR_GITHUB_URL>
cd student-dashboard
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:8050
📷 Example Output

(เพิ่ม Screenshot Dashboard ตรงนี้เพื่อความประทับใจ)

📈 Learning Outcomes

จากโปรเจคนี้ได้เรียนรู้:

การสร้าง Web Dashboard ด้วย Dash

การทำ Interactive Data Visualization

การใช้ Callback Logic

การจัดการข้อมูลด้วย Pandas

การใช้ Git แบบมืออาชีพ

🏁 Conclusion

โปรเจคนี้แสดงให้เห็นถึงการพัฒนา Dashboard แบบ Interactive
โดยใช้ Data Visualization เพื่อวิเคราะห์ข้อมูลเชิงลึก

โครงสร้างระบบออกแบบให้เข้าใจง่าย
และสามารถต่อยอดไปสู่ระบบวิเคราะห์ข้อมูลขนาดใหญ่ได้ในอนาคต