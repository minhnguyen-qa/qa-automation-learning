# QA Automation Learning Journey

Portfolio ghi lại quá trình tự học automation testing trong 4 tuần, 
áp dụng trên nền tảng 6+ năm kinh nghiệm QA manual.

## Công nghệ sử dụng
- **UI Automation:** Python, Playwright, Page Object Model, pytest
- **API Automation:** Python requests, Postman, Newman
- **Performance Testing:** JMeter
- **Database:** SQLite (data validation)
- **CI/CD:** GitHub Actions

## Cấu trúc project
- `todo_page.py` — Page Object Model cho UI testing
- `test_pytest_basic.py` — Test case Playwright + pytest
- `test_api.py` — Test case API (GET/POST/PUT/DELETE)
- `test_sql.py` — Test case validate dữ liệu SQLite
- `conftest.py` — Fixture dùng chung
- `jmeter/` — Test Plan JMeter
- `.github/workflows/` — CI/CD tự động chạy test mỗi lần push

## Cách chạy test
\`\`\`
pip install -r requirements.txt
pytest -v
\`\`\`