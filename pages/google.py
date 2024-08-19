from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generic_utils import Common_Utils


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    search_tb = (By.NAME, "q")
    top_stories = (By.XPATH, "//div[@id='search']/descendant::span/span[.='Top stories']")
    flash_news = (By.XPATH, "//div[@id='search']/descendant::a[@class='WlydOe']")
    news_tab = (By.XPATH, "//div[@role='listitem']/descendant::div[.='News']")
    list_of_news = (By.XPATH, "//div/following-sibling::div[@role='heading']")

    def topic_description(self, topic):
        topic = topic.lower()
        return self.driver.find_element(By.XPATH, f"//div/following-sibling::div[@role='heading' and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{topic}')]/following-sibling::div")
        # return self.driver.find_element(By.XPATH, f"//div/following-sibling::div[@role='heading' and contains(.,'{topic}')]/following-sibling::div")

    def topic_posted_date(self, topic):
        topic = topic.lower()
        return self.driver.find_element(By.XPATH, f"//div/following-sibling::div[@role='heading' and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{topic}')]/following-sibling::div/span")
        # return self.driver.find_element(By.XPATH, f"//div/following-sibling::div[@role='heading' and contains(.,'{topic}')]/following-sibling::div/span")

    def search_news(self, value):
        self.driver.find_element(*self.search_tb).send_keys(value, Keys.ENTER)

    def click_on_news_tab(self):
        self.driver.find_element(*self.news_tab).click()

    def validate_top_stories(self):
        return self.driver.find_element(*self.top_stories).is_displayed()

    def click_on_the_first_news(self):
        list_news = self.driver.find_elements(*self.flash_news)
        for news in list_news:
            news.click()
            break


    def get_the_news_text(self, content):
        list_news = self.driver.find_elements(*self.list_of_news)
        news_content = ""
        for news in list_news:
            if news.text.__contains__(content):
                news_content = news.text
                break
        return news_content

    def get_the_news_description(self, topic):
        return self.topic_description(topic).text

    def get_the_new_posted_date(self, topic):
        text = self.topic_posted_date(topic).text
        return Common_Utils.get_date(text)
