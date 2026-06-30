# ==========================================
# Pandas Basics — Ayesha Mumtaz
# ==========================================

import pandas as pd

# ---- 1. Series Banao ----
print("=" * 40)
print("1. Pandas Series")
print("=" * 40)

s = pd.Series([10, 20, 30, 40, 50])
print(s)

# ---- 2. DataFrame Banao ----
print("\n" + "=" * 40)
print("2. Pandas DataFrame")
print("=" * 40)

data = {
    "Name"   : ["Ayesha", "Sara", "Ali", "Usman"],
    "Age"    : [20, 21, 22, 19],
    "Marks"  : [85, 90, 78, 92],
    "Grade"  : ["A", "A+", "B+", "A+"]
}

df = pd.DataFrame(data)
print(df)

# ---- 3. DataFrame Info ----
print("\n" + "=" * 40)
print("3. DataFrame Info")
print("=" * 40)

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nBasic Stats:\n", df.describe())

# ---- 4. Data Access ----
print("\n" + "=" * 40)
print("4. Data Access")
print("=" * 40)

print("Names Column:\n", df["Name"])
print("\nFirst 2 Rows:\n", df.head(2))

# ---- 5. Filtering ----
print("\n" + "=" * 40)
print("5. Filtering Data")
print("=" * 40)

high_marks = df[df["Marks"] > 85]
print("Students with Marks > 85:\n", high_marks)
