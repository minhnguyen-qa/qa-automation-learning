import os
import json
from datetime import datetime

# -------------------------------------------
# PHẦN 1: Đọc/ghi file — dùng khi lưu test data, log kết quả test

# Ghi file text
def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("test_log.txt", "a",encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message} \n")

write_log ("Test bắt đầu")
write_log ("Login thành công")
write_log ("Verify dashboard OK")
write_log ("Test kết thúc")
print ("Đã ghi file test_log.txt")

# Đọc file text lại
print ("\n Nội dung file log:")
with open ("test_log.txt", "r") as f:
    content = f.read()
    print (content)

# -------------------------------------------
# PHẦN 2: Đọc/ghi JSON — quan trọng nhất vì API trả về JSON

# Ghi JSON file (giả lập lưu test data)

test_data = {
    "users": [
        {"username": "admin", "password": "Admin@123", "role": "admin"},
        {"username": "tester", "password": "Test@123", "role": "viewer"},
        {"username": "guest", "password": "Guest@123", "role": "guest"}
    ]
}

with open ("test_data.json", "w") as f:
    json.dump (test_data, f, indent=2)
print ("Đã ghi file test_data.son")

# Đọc JSON file lại

with open ("test_data.json", "r") as f:
    loaded_data = json.load(f)

print ("\nTest users:")
for user in loaded_data ["users"]:
    print (f" User name: {user['username']} | Role: {user ['role']}")

# -------------------------------------------
# PHẦN 3: os module — kiểm tra file/folder tồn tại chưa

print ("\n ---Kiểm tra file---")
files = ["test_log.txt", "test_data.json", "không_có_file_txt"]
for file in files:
    if os.path.exists (file):
        print (f" v {file} tồn tại")
    else:
        print (f"x {file} không tồn tại")

# -------------------------------------------
# PHẦN 4: Bài tập tổng hợp — giả lập mini test runner
# Kết hợp tất cả những gì đã học: dict, list, function, try/except, file

def run_test (name, expected, actual):
    result = "PASS" if expected == actual else "FAIL"
    msg =  f"{name}: {result} (expected={expected}) actual={actual}"
    print (msg)
    with open ("result.txt",  "a", encoding="utf-8") as f:
        f.write (msg + "\n")
    return result

run_test ("TC01 - Status code", 200, 200)
run_test ("TC02 - Wrong status", 200, 404)
run_test("TC03 - Username", "minh_qa", "minh_qa")

results = []
results.append(run_test("TC01 - Status code", 200, 200))
results.append(run_test("TC02 - Wrong status", 200, 404))
results.append(run_test("TC03 - Username", "minh_qa", "minh_qa"))

print (f"\nTotal: {len(results)} | Pass: {results.count('PASS')} | Fail: {results.count('FAIL')}")