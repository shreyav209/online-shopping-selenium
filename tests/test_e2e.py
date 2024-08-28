import pytest,time
from selenium.webdriver.common.by import By
from pages.login_page import CheckoutPage, LoginPage, ProductPage

#test data
username = 'standard_user'
password = 'secret_sauce'
zipcode = '292020'
products_to_add = ['Sauce Labs Backpack', 'Sauce Labs Bike Light']

# products_to_add = 'Sauce Labs Backpack'

@pytest.mark.usefixtures('browser_setup')
class TestE2E:

    def test_e2e(self):
        self.driver.get(self.urls['url'])
        loginpage = LoginPage(self.driver)
        productpage =ProductPage(self.driver)
        checkoutpage = CheckoutPage(self.driver)

        time.sleep(3)
        loginpage.getLoginUser(username,password)
        time.sleep(3)
        loginpage.doLogin()

        for products in products_to_add:
            productpage.addProductToCart(products)
        time.sleep(5)
        cart_count = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert int(cart_count) == len(products_to_add)

        productpage.clickOnCart()

        cart_product_name =checkoutpage.verifyProductInCart()
        for product_name in cart_product_name:
            assert product_name in cart_product_name

        checkoutpage.goCheckout()
        checkoutpage.userInformation(username,password,zipcode)
        checkoutpage.clickOnContinue()
        productPrice=checkoutpage.getProductPrice()
        sum_of_price = sum(productPrice)
        final_price = checkoutpage.getTotalPrice()
        assert sum_of_price  == final_price





