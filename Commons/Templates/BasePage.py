

class BasePage:
    def __init__(self, page_obj):
        self.page = page_obj
        self.main_page_shortcut = None
        self.search_input = None
        self.help_button = None
        self.login_button = None
        self.language_selector = None

    async def navigate_to_main_page(self):
        self.main_page_shortcut = self.page.locator('[id="p-logo"]')
        await self.main_page_shortcut.click()
        await self.page.wait_for_load_state("networkidle")

    async def navigate_to_login_page(self):
        self.login_button = self.page.locator('[title="You\'re encouraged to log in; however, it\'s not mandatory. [alt-shift-o]"]')
        await self.login_button.click()
        await self.page.wait_for_load_state("networkidle")

    async def search(self, content:str = ""):
        self.search_input = self.page.locator('[aria-label="Search Wikipedia"]')
        await self.search_input.fill(content)
        await self.search_input.press("Enter")
        await self.page.wait_for_load_state("networkidle")

    async def get_help(self):
        self.help_button = self.page.locator('[href="/wiki/Help:Contents"]')
        await self.help_button.click()
        await self.page.wait_for_load_state("networkidle")

    async def get_title(self):
        res = await self.page.title()
        return res
