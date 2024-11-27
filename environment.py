import os
import asyncio
import allure
from behave import fixture, use_fixture
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

async def browser_chrome_fixture(context):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()
    await page.set_viewport_size({"width": 1280, "height": 720})
    print("Browser started successfully")
    # Navigate to the login page
    await page.goto(os.getenv('baseURL'))  # Ensure LOGIN_URL is set in .env
    context.browser = browser
    context.playwright = playwright
    context.page = page
    return page

def before_all(context):
    allure_results_dir = './allure-results'
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

def before_scenario(context, scenario):
    asyncio.run(browser_chrome_fixture(context))

def after_scenario(context, scenario):
    asyncio.run(cleanup_browser(context, scenario))

async def cleanup_browser(context, scenario):
    if hasattr(context, 'page'):
        if scenario.status == 'failed':
            screenshot_path = os.path.join('allure-results', f'{scenario.name}_screenshot.png')
            await context.page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        await context.page.close()
    if hasattr(context, 'browser'):
        await context.browser.close()
    if hasattr(context, 'playwright'):
        await context.playwright.stop()