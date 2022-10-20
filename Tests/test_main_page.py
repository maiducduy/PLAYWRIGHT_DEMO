import pytest
from Commons.MainPage import MainPage


class Test:
    TEST_URL = "https://en.wikipedia.org/wiki/Main_Page"

    async def create_page(self, aplaywright, url):
        browser = await aplaywright.chromium.launch(channel="chrome")
        context = await browser.new_context()
        page = await context.new_page()
        res = await page.goto(url)  # This statement is requesting the website and waiting for the response
        assert res.status == 200, "Response code is not 200"  # This statement is verifying the response code, if not 200, it raises an assertion
        return page

    @pytest.mark.asyncio
    async def test_login_button(self, aplaywright):
        """
        This test case verifies whether login page is navigated if users click the login button
        """
        page = await self.create_page(aplaywright, Test.TEST_URL)
        obj = MainPage(page)

        await obj.navigate_to_login_page()
        title = await obj.get_title()
        assert title == "Log in - Wikipedia"

    @pytest.mark.asyncio
    async def test_search_field(self, aplaywright):
        """
        This test case verifies whether results page is navigated if users search an information
        """
        page = await self.create_page(aplaywright, Test.TEST_URL)
        obj = MainPage(page)

        title_tmp = " - Search results - Wikipedia"

        await obj.search("Python")
        title = await obj.get_title()
        assert title == "Python" + title_tmp

        await obj.navigate_to_login_page()

        await obj.search("Linkin Park")
        title = await obj.get_title()
        assert title == "Linkin Park" + title_tmp

    @pytest.mark.asyncio
    async def test_help(self, aplaywright):
        """
        This test case verifies whether help page is navigated if users click "help"
        """
        page = await self.create_page(aplaywright, Test.TEST_URL)
        obj = MainPage(page)

        await obj.get_help()
        title = await obj.get_title()
        assert title == "Help:Contents - Wikipedia"

    @pytest.mark.asyncio
    async def test_changing_language(self, aplaywright):
        """
        This test case verifies whether language of this page is changed to Vietnamese
        """
        page = await self.create_page(aplaywright, Test.TEST_URL)
        obj = MainPage(page)

        await obj.change_to_vietnamese()
        title = await obj.get_title()
        assert title == "Wikipedia, bách khoa toàn thư mở"
