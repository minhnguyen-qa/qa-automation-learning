from playwright.sync_api import sync_playwright
from todo_page import TodoPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    todo = TodoPage(page)
    todo.goto()
    todo.add_todo("Học pytest")
    print("Số todo:", todo.count_todos())
    
    browser.close()