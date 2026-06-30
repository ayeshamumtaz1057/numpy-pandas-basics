# ==========================================
# Data Analysis — Ayesha Mumtaz
# ==========================================

import pandas as pd
import numpy as np

# ---- 1. Student Data ----
print("=" * 40)
print("Student Data Analysis")
print("=" * 40)

data = {
    "Name"        : ["Ayesha", "Sara", "Ali", "Usman", "Fatima"],
    "Study_Hours" : [5, 8, 3, 7, 6],
    "Attendance"  : [90, 95, 70, 88, 92],
    "Marks"       : [85, 92, 65, 88, 90]
}

df = pd.DataFrame(data)
print(df)

# ---- 2. Analysis ----
print("\n" + "=" * 40)
print("Analysis Results")
print("=" * 40)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Top Student:", df.loc[df["Marks"].idxmax(), "Name"])

# ---- 3. Correlation ----
print("\n" + "=" * 40)
print("Correlation")
print("=" * 40)

corr = df["Study_Hours"].corr(df["Marks"])
print(f"Study Hours vs Marks Correlation: {corr:.2f}")
