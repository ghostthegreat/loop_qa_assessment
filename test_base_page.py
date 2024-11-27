from playwright.async_api import Page
class BasePage:
    def __init__(self, page: Page):
        self.page = page
    def find_element(self, locator):
        return self.page.locator(locator)