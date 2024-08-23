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
        # content = input("Enter the news topic: ")
        content = "tungabhadra dam gate crash"
        search_page.search_news(content)
        search_page.click_on_news_tab()

        topic1 = search_page.get_matching_news(content)
        if not topic1:
            print("Fake News")
        else:
            print("Real News")
            topic = Common_Utils.split_string(topic1[0])
            Common_Utils.write_data_into_excel(file, sheet_name, last_row + 1, 1, content)
            description = search_page.get_the_news_description(topic[0])
            print("Description:", description)
            Common_Utils.write_data_into_excel(file, sheet_name, last_row + 1, 3, description)

            date = search_page.get_the_new_posted_date(topic[0])
            print("Posted Date:", date)
            Common_Utils.write_data_into_excel(file, sheet_name, last_row + 1, 2, date)

            sources = search_page.get_matching_sources(topic1)
            value = ", ".join(sources)
            print("Sources:", value)
            Common_Utils.write_data_into_excel(file, sheet_name, last_row + 1, 4, value)


