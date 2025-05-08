from playwright.sync_api import sync_playwright
 
def run(playwright):
    # 启动浏览器
    browser = playwright.chromium.launch(headless=False)  # headless=True 表示无头模式
    context = browser.new_context()
 
    # 打开新页面
    page = context.new_page()
 
    # 导航到URL
    page.goto("https://example.com")
 
    # 截取屏幕截图
    page.screenshot(path="example.png")
 
    # 关闭浏览器
    browser.close()
 
with sync_playwright() as playwright:
    run(playwright)