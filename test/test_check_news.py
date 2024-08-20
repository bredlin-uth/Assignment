import os
import time
import pytest

from generic_utils import Common_Utils
from pages.google import GooglePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestNews:

    def test_check_news_is_real_or_fake(self):
        sheet_name = Common_Utils.get_config("excel info", "sheet_name")
        search_page = GooglePage(self.driver)
        file = os.path.join(os.path.dirname(os.path.abspath('.')), Common_Utils.get_config("excel info", "excel_path"))
        last_row = Common_Utils.get_row_count(file, sheet_name)
        content = Common_Utils.read_data_from_excel(file, sheet_name, last_row, 1)
        search_page.search_news(content)
        search_page.click_on_news_tab()

        topic = search_page.get_the_news_text(content)
        if topic != "":
            description = search_page.get_the_news_description(topic)
            Common_Utils.write_data_into_excel(file, sheet_name, last_row, 3, description)

            date = search_page.get_the_new_posted_date(topic)
            Common_Utils.write_data_into_excel(file, sheet_name, last_row, 2, date)

            print("Real News")
        else:
            print("Fake News")
