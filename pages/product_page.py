from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        add_button.click()
        self.solve_quiz_and_get_code()

    # --- НОВЫЕ МЕТОДЫ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ ---
    def get_product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    # --- ОБНОВЛЕННЫЕ МЕТОДЫ ПРОВЕРКИ ---
    def should_be_add_to_basket_message_with_correct_name(self):
        # Проверяем, что сообщение о добавлении появилось
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-success"), "Success message is not presented"
        
        # Получаем название товара из сообщения
        message_product_name = self.browser.find_element(By.CSS_SELECTOR, ".alert-success strong").text
        # Получаем название товара со страницы (через новый метод)
        page_product_name = self.get_product_name()
        
        assert page_product_name == message_product_name, \
            f"Product name in message '{message_product_name}' does not match page name '{page_product_name}'"

    def should_be_correct_basket_total(self):
        # Получаем цену товара со страницы (через новый метод)
        page_product_price = self.get_product_price()
        # Получаем стоимость корзины из сообщения
        basket_total = self.browser.find_element(By.CSS_SELECTOR, ".alert-info .alertinner strong").text
        
        assert page_product_price == basket_total, \
            f"Basket total '{basket_total}' does not match product price '{page_product_price}'"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except:
            return False