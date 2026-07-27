import pytest
from playwright.sync_api import sync_playwright
from todo_page import TodoPage

@pytest.fixture
def todo_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield TodoPage(page)
        browser.close()