import pandas as pd

# โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv("sales.csv")

# แสดงข้อมูล 5 แถวแรก
print("----- HEAD -----")
print(df.head())

# ดูโครงสร้างข้อมูล
print("\n----- INFO -----")
print(df.info())

# ดูสถิติพื้นฐาน
print("\n----- DESCRIBE -----")
print(df.describe())


# ---------- DATA CLEANING ----------

# ตรวจสอบว่าคอลัมน์ไหนมีค่าว่างบ้าง
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# ลบแถวที่มีค่าว่างทั้งหมด
df_clean = df.dropna()

# แสดงข้อมูลหลังทำความสะอาด
print("\n----- CLEAN DATA -----")
print(df_clean)

# บันทึกเป็นไฟล์ใหม่
df_clean.to_csv("sales_clean.csv", index=False)

print("\nClean data saved as sales_clean.csv")
