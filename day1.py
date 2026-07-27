# Bài 1: biến và print
name = "Minh"
experience = 6
role = "QA"

print("Tên:",name)
print("Kinh nghiệm:", experience,"năm")
print("Vai trò", role)

# Bài 2: vòng lặp
print("\nĐếm từ 1 đến 5")
for i in range(1,6):
    print(i)

#Bài 3: List
skills = ["Manual Testing","Postman", "Jmeter", "Linux", "Docker"]
for skill in skills:
    print("-", skill)

#Bài 4: If/else
years = 6
if years >= 5:
    print("\nlevel: Senior")
else:
    print ("\nLevel: Junior/Mid")