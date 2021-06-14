from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    GOOGLE_SEARCH_FIELD   = (By.CLASS_NAME, "gLFyf gsfi")
    GOOGLE_NAVIGATION_BAR = (By.CLASS_NAME, "MUFPAc")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def check_navigation_bar(self):
        all_list     = self.find_elements(YandexSeacrhLocators.GOOGLE_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu