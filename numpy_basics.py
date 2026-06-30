# ==========================================
# NumPy Basics — Ayesha Mumtaz
# ==========================================

import numpy as np

# ---- 1. Array Banao ----
print("=" * 40)
print("1. NumPy Arrays")
print("=" * 40)

arr1 = np.array([1, 2, 3, 4, 5])
print("Simple Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# ---- 2. Array Properties ----
print("\n" + "=" * 40)
print("2. Array Properties")
print("=" * 40)

print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

# ---- 3. Array Operations ----
print("\n" + "=" * 40)
print("3. Array Operations")
print("=" * 40)

a = np.array([10, 20, 30, 40, 50])
print("Original:", a)
print("Add 5:", a + 5)
print("Multiply 2:", a * 2)
print("Square Root:", np.sqrt(a))

# ---- 4. Math Functions ----
print("\n" + "=" * 40)
print("4. Math Functions")
print("=" * 40)

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))

# ---- 5. Zeros & Ones ----
print("\n" + "=" * 40)
print("5. Special Arrays")
print("=" * 40)

print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Range:", np.arange(0, 10, 2))
