name = "goorm"
age = 25
height = 181.523456

print("저의 이름은 %s입니다."%name)

print("저는 %d살입니다."%25)
print("제 나이는 %d살입니다."%age)
print("제 나이는 %s살입니다."%age)
print("제 나이는 %.2f살입니다."%age)

print("저의 키는 %fcm입니다."%height)
print("저의 키는 %.2fcm입니다."%height)
print("저의 키는 %dcm입니다."%height)

print("저의 성은 '%c'입니다."%"남")

print("저의 나이는 16진수로 표현하면 %x, 8진수로 표현하면 %o입니다."%(age,age))

print("%10d %010d"%(10,10))

print("%8s %8d %8s"%("김구름",6,"컴퓨터공학"))
print("%-8s %-8d %-8s"%("김구름",6,"컴퓨터공학"))