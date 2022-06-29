str = " Hello goorm! I study Python  "

num = str.count(' ')
print("빈칸의 개수는 %d입니다."%num)
print("처음 등장하는 '1'의 인덱스 값은 %d입니다."%str.find('1'))
print("Good day에서 처음 등장하는 'y'의 인덱스 값은 %d입니다."%"Good day".index('y'))

print(" ".join(str))
print(str.upper())
print(str.lower())
print(str.lstrip())
print(str.rstrip())
print(str.strip())
print(str.replace('Python','C'))
print(str.split())
