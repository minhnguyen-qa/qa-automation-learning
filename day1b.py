# PHẦN 1: Dictionary (dict) — dùng nhiều trong automation để lưu data
# Dict là cặp key:value, như JSON trong API response

tester = {
    "name":"Minh",
    "experience":6,
    "role":"senior QA",
    "skills":["Postman","Jmeter","Linux"]
}

#đọc giá trị từ Dict
print("Tên",tester["name"])
print("Role",tester["role"])
print("Skill đầu tiên:", tester["skills"][0])

#Thêm key mới vào Dict
tester["location"] ="Ho Chi Minh City"
print("Location", tester["location"])

#Loop qua dict
print ("\n Toàn bộ thông tin: ")
for key, value in tester.items():
    print(f" {key}: {value}")

# -------------------------------------------

# PHẦN 2: Function — đóng gói code để tái sử dụng

def check_level (years):
    if years >=5:
        return "Senior"
    elif years >=2:
        return "Mid"
    else:
        return "Junior"
    
def greet_tester (name,years):
    level = check_level (years)
    print (f"xin chào {name}! Bạn là {level} với {years} năm kinh nghiệm" )
    
#Gọi Function
greet_tester ("Minh",6)
greet_tester ("Lan",3)
greet_tester ("Nam",1)

# -------------------------------------------
# PHẦN 3: try/except — xử lý lỗi (quan trọng khi viết automation)
# Trong automation, API có thể trả về data sai — cần handle lỗi

def get_value_from_response (data,key):
    try:
        value = data[key]
        print(f"Lấy được giá trị: {value}")
        return value
    except KeyError:
        print(f"Không tìm thấy key '{key}' trong response")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None
    
# Giả lập API response (dict)
api_response = {
    "status": "success",
    "code": 200,
    "data": {"user_id": 123, "username": "minh_qa"}
}

print ("\n--- Test get_value_from_response")
get_value_from_response (api_response, "status")
get_value_from_response (api_response, "token")
get_value_from_response (api_response, "code")

# -------------------------------------------
# PHẦN 4: f-string — cách format string hay dùng nhất trong Python
name = "Minh"
score = 95.5
print (f"\nKết quả test của {name}:{score}%")
print(f"Pass hay Fail: {'PASS' if score >=80 else 'FAIL'}")