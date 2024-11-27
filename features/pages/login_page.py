import os
from playwright.async_api import Page, TimeoutError
from config import config 

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.login_button_email_locator = self.page.locator("#lui_0")
        self.login_button_continue_locator = self.page.locator("div:has-text('Continue')")
        self.login_button_pass_locator = self.page.locator("#lui_6")
        self.login_button_login_locator = self.page.locator("div:has-text('Log in')")


    async def login(self):
       
           

            await self.login_button_email_locator.wait_for(state='visible', timeout=10000)
           
            await self.login_button_email_locator.click()
            
            await self.login_button_email_locator.fill(os.getenv('USERNAME'))
            
       
            
            await self.login_button_continue_locator.wait_for(state='visible', timeout=10000)
           
            await self.login_button_continue_locator.click()
            
    
           
            await self.login_button_pass_locator.wait_for(state='visible', timeout=10000)
            
            await self.login_button_pass_locator.click()
           
            await self.login_button_pass_locator.fill(os.getenv('PASSWORD'))
            
           
           
            await self.login_button_login_locator.wait_for(state='visible', timeout=10000)
           
            await self.login_button_login_locator.click()
            
            
