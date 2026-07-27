# from playwright.sync_api import sync_playwright
# from todo_page import TodoPage

# def test_add_one_todo():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         todo = TodoPage(page)
#         todo.goto()
#         todo.add_todo("Học pytest")
#         assert todo.count_todos() == 1
#         browser.close()

# def test_add_two_todos():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         todo = TodoPage(page)
#         todo.goto()
#         todo.add_todo("Việc 1")
#         todo.add_todo("Việc 2")
#         assert todo.count_todos() == 2
#         browser.close()

# import pytest
# from playwright.sync_api import sync_playwright
# from todo_page import TodoPage

# @pytest.fixture
# def todo_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         yield TodoPage(page)
#         browser.close()

def test_add_one_todo(todo_page):
    todo_page.goto()
    todo_page.add_todo("Học pytest")
    assert todo_page.count_todos() == 1

def test_add_two_todos(todo_page):
    todo_page.goto()
    todo_page.add_todo("Việc 1")
    todo_page.add_todo("Việc 2")
    assert todo_page.count_todos() == 2