from .Templates.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, page_obj):
        super().__init__(page_obj)

    async def change_to_vietnamese(self):
        self.language_selector = self.page.locator('[title="Vietnamese"]')
        await self.language_selector.click()
        await self.page.wait_for_load_state("networkidle")