from pages.test_base_page import BasePage
from playwright.async_api import Page

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navigate_to_cross_functional_page = page.locator("xpath = //*[@id='asana_sidebar']/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/nav/div[2]/div/div[1]/a")
        self.navigate_to_work_requests_page = page.locator("xpath = //*[@id='asana_sidebar']/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/nav/div[2]/div/div[2]/a")


    async def navigate_to_cross_functional_page(self):
        await self.navigate_to_cross_functional_page.click()

    async def navigate_to_work_requests_page(self):
        await self.navigate_to_work_requests_page.click()