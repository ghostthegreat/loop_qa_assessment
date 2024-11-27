import asyncio
from playwright.async_api import Page, TimeoutError
from pages.test_base_page import BasePage

class CrossFunctionalPage(BasePage):
    def __init__(self, page: Page, context):
        super().__init__(page)
        self.context = context

    async def navigate_to_cross_functional_page(self):
        # Implement navigation logic here
        await self.page.goto("https://app.asana.com/0/123456789/cross-functional")  # Update URL accordingly
        print("Navigated to Cross-functional project plan page")

    def get_column_locator(self, column_name: str):
        return self.page.locator(f"div[aria-label='{column_name}']")

    def get_task_locator(self, column_name: str, task_name: str):
        return self.page.locator(f"div[aria-label='{column_name}'] span:text('{task_name}')")

    def get_task_tags_locator(self, column_name: str, task_name: str):
        task_locator = self.get_task_locator(column_name, task_name)
        return task_locator.locator("..").locator("div.BoardLayout-customPropertiesAndTags span")

    async def verify_task_in_column(self, column_name: str, task_name: str):
        column_locator = self.get_column_locator(column_name)
        assert await column_locator.is_visible(), f"Column '{column_name}' is not visible"
        task_locator = self.get_task_locator(column_name, task_name)
        assert await task_locator.is_visible(), f"Task '{task_name}' is not found in column '{column_name}'"
        # Store the task details in context for tag verification
        self.context.current_task_name = task_name
        self.context.current_column_name = column_name

    async def verify_task_tags(self, column_name: str, task_name: str, expected_tags: list[str]):
        tag_elements = await self.get_task_tags_locator(column_name, task_name).all_inner_texts()
        for tag in expected_tags:
            assert tag in tag_elements, f"Expected tag '{tag}' not found for task '{task_name}'"