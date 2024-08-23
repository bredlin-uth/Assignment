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
    list_of_news = (By.XPATH, "//div[@role='heading' and @style]")
    list_of_description = (By.XPATH, "//div[@role='heading' and @style]/following-sibling::div")

    def get_sources(self, topic):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),\"" + topic + "\")]/preceding-sibling::div/span")

    def topic_description(self, topic):
        return self.driver.find_element(By.XPATH, "//div/following-sibling::div[@role='heading' and contains(.,\""+ topic +"\")]/following-sibling::div")

    def topic_posted_date(self, topic):
        return self.driver.find_element(By.XPATH, "//div/following-sibling::div[@role='heading' and contains(.,\""+ topic +"\")]/following-sibling::div/span")

    def search_news(self, value):
        self.driver.find_element(*self.search_tb).send_keys(value, Keys.ENTER)

    def click_on_news_tab(self):
        self.driver.find_element(*self.news_tab).click()

    def get_matching_news(self, content):
        list_news = self.driver.find_elements(*self.list_of_news)
        list_content = content.lower().split(" ")
        news = []
        for element in list_news:
            ele = element.text.lower()
            if all(txt in ele for txt in list_content):
                news.append(element.text)
        return news

    def get_the_news_description(self, topic):

        return self.topic_description(topic).text

    def get_the_new_posted_date(self, topic):
        text = self.topic_posted_date(topic).text
        return Common_Utils.get_date(text)

    def get_matching_sources(self, content):
        sources = []
        for i in content:
            topic = Common_Utils.split_string(i)[0]
            text = self.get_sources(topic).text
            sources.append(text)
        return set(sources)
