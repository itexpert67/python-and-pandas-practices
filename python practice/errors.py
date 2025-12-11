# ============================
# 1. SYNTAX ERROR
# Uncomment to see error
# if True print("Hi Farooq")
# ============================


# ============================
# 2. INDENTATION ERROR
# Uncomment to see error
# for i in range(5):
# print(i)
# ============================


# ============================
# 3. NAME ERROR
# name_error
# ============================
print("NAME ERROR:")
try:
    print(age)
except Exception as e:
    print(e)


# ============================
# 4. TYPE ERROR
# ============================
print("\nTYPE ERROR:")
try:
    x = 5 + "Farooq"
except Exception as e:
    print(e)


# ============================
# 5. VALUE ERROR
# ============================
print("\nVALUE ERROR:")
try:
    int("hello")
except Exception as e:
    print(e)


# ============================
# 6. ZERO DIVISION ERROR
# ============================
print("\nZERO DIVISION ERROR:")
try:
    10 / 0
except Exception as e:
    print(e)


# ============================
# 7. INDEX ERROR
# ============================
print("\nINDEX ERROR:")
try:
    nums = [1, 2, 3]
    print(nums[10])
except Exception as e:
    print(e)


# ============================
# 8. KEY ERROR
# ============================
print("\nKEY ERROR:")
try:
    data = {"name": "Farooq"}
    print(data["age"])
except Exception as e:
    print(e)


# ============================
# 9. ATTRIBUTE ERROR
# ============================
print("\nATTRIBUTE ERROR:")
try:
    s = "Farooq"
    s.push()
except Exception as e:
    print(e)


# ============================
# 10. IMPORT ERROR
# ============================
print("\nIMPORT ERROR:")
try:
    import farooq_abc_random
except Exception as e:
    print(e)


# ============================
# 11. FILE NOT FOUND ERROR
# ============================
print("\nFILE NOT FOUND ERROR:")
try:
    open("farooq.txt")
except Exception as e:
    print(e)


# ============================
# 12. OVERFLOW ERROR
# ============================
print("\nOVERFLOW ERROR:")
try:
    import math
    print(math.exp(1000))
except Exception as e:
    print(e)


# ============================
# 13. ASSERTION ERROR
# ============================
print("\nASSERTION ERROR:")
try:
    age = 10
    assert age > 18
except Exception as e:
    print(e)


# ============================
# 14. RECURSION ERROR
# ============================
print("\nRECURSION ERROR:")
try:
    def loop():
        return loop()
    loop()
except Exception as e:
    print(e)


# ============================
# 15. MEMORY ERROR
# ============================
print("\nMEMORY ERROR:")
try:
    huge = [1] * (10**12)
except Exception as e:
    print(e)


print("\n\n--- END OF ALL PYTHON ERRORS ---")
