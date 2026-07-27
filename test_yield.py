def demo():
    print("Trước yield")
    yield "giá trị"
    print("Sau yield")

gen = demo()
print(next(gen))   # in "Trước yield", rồi in "giá trị"