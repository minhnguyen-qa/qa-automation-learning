class TodoPage:
    def __init__(self, page):
        self.page = page
        self.input = ".new-todo"
        self.todo_list = ".todo-list li"
    
    def goto(self):
        self.page.goto("https://demo.playwright.dev/todomvc")
    
    def add_todo(self, text):
        self.page.fill(self.input, text)
        self.page.keyboard.press("Enter")
        self.page.locator(self.todo_list).first.wait_for(timeout=100)
    
    def count_todos(self):
        return self.page.locator(self.todo_list).count()