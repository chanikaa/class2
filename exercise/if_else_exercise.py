# จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้
# คะแนน 80 - 100 ได้ A
# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F
# และให้แสดงผลตามตัวอย่างด้านล่าง
# Enter your score: 49
# grade:  F

score = int(input("Enter your score : "))

if score > 79:
    print("grade : A")
elif score > 74:
    print("grade : B+")
elif score > 69:
    print("grade : B")
elif score > 64:
    print("grade : C+")
elif score > 59:
    print("grade : C")
elif score > 54:
    print("grade : D+")
elif score > 49:
    print("grade : D")
else:
    print("grade : F")