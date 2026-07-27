# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://demo.playwright.dev/todomvc")
    
#     page.fill(".new-todo", "Học Playwright ngày 3")
#     page.keyboard.press("Enter")
#     page.wait_for_timeout(1000)
    
#     todo_text = page.locator(".todo-list li").first.inner_text()
#     print("Todo vừa tạo:", todo_text)
#     assert "Học Playwright" in todo_text, f"FAIL: {todo_text}"
#     print("PASS: Tạo todo thành công")
    
#     browser.close()

# from playwright.sync_api import sync_playwright

# # with sync_playwright() as p:
# #     browser = p.chromium.launch(headless=False)
# #     page = browser.new_page()
#     page.goto("https://demo.playwright.dev/todomvc")
    
#     # Dùng placeholder thay vì class
#     page.fill("input[placeholder='What needs to be done?']", "Test bằng placeholder")
#     page.keyboard.press("Enter")
#     page.wait_for_timeout(1000)
    
#     todo_text = page.locator(".todo-list li").first.inner_text()
#     print("Todo:", todo_text)
#     assert "Test bằng placeholder" in todo_text
#     print("PASS")
    
#     browser.close()


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.playwright.dev/todomvc")

    todos = ["Học Python", "Học Playwright", "Viết test case"]
    for todo in todos:
        page.fill(".new-todo", todo)
        page.keyboard.press("Enter")

    page.wait_for_timeout(1000)
    count = page.locator(".todo-list li").count()
    print(f"Số todo: {count}")
    assert count == 3, f"FAIL: expected 3, actual {count}"
    print("PASS: Đủ 3 todo")

   # Đánh dấu todo đầu tiên là done
    page.locator(".todo-list li").first.locator(".toggle").click()
    page.wait_for_timeout(500)
    # Đếm số todo đã completed
    completed = page.locator(".todo-list li.completed").count()
    print(f"Completed: {completed}")
    assert completed == 1, f"FAIL: expected 1, actual {completed}"
    print("PASS: Đánh dấu completed thành công")

    # Hover vào item đầu tiên để hiện nút xóa
    page.locator(".todo-list li").first.hover()
    page.locator(".todo-list li").first.locator(".destroy").click()
    page.wait_for_timeout(500)

    count_after = page.locator(".todo-list li").count()
    print(f"Số todo sau khi xóa: {count_after}")
    assert count_after == 2, f"FAIL: expected 2, actual {count_after}"
    print("PASS: Xóa todo thành công")

    browser.close()