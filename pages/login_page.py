
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass


class LoginPage(BaseClass):

    username = (By.ID,'user-name')
    password = (By.ID,'password')
    login_btn = (By.ID,'login-button')

    def __init__(self, driver):
        self.driver = driver

    def getLoginUser(self,username,password):
        username = self.do_send_keys(self.username,username)
        password = self.do_send_keys(self.password,password)
        return username,password

    def doLogin(self):
        self.do_click(self.login_btn)

class ProductPage(BaseClass):

    
    allproducts = (By.XPATH,"//a[contains(@id,'title_link')]/div")
    addToCart = (By.ID,'add-to-cart-sauce-labs-bolt-t-shirt')
    cartBtn = (By.XPATH,"//div[@id= 'shopping_cart_container']")

    def __init__(self, driver):
        self.driver = driver

    def getProductList(self):
        return self.get_all_elements(self.allproducts)

    def addProductToCart(self,product_name):
        products = self.getProductList()
        for product in products:
            if product.text in product_name:
                add_btn = product.find_element(By.XPATH,"//button[contains(@id,'add-to-cart')]")
                add_btn.click()
                

    def clickOnCart(self):
        self.do_click(self.cartBtn)


class CheckoutPage(ProductPage):

    checkout_btn = (By.ID,'checkout')
    firstName = (By.ID,'first-name')
    lastName = (By.ID,'last-name')
    zipCode = (By.ID,'postal-code') 
    continueBtn = (By.ID,'continue')
    productPrice = (By.XPATH,"//div[@class ='inventory_item_price']")
    finalPrice = (By.XPATH,"//div[@class ='summary_subtotal_label']")
    finishBtn = (By.ID,'finish')
    thankYouMessage = (By.CLASS_NAME, 'complete-header')

    def verifyProductInCart(self):
        products = self.getProductList()
        for product in products:
            productText = product.text
            return productText
        
    def goCheckout(self):
        return self.do_click(self.checkout_btn)
        

    def userInformation(self,firstname,lastname,zipcode):
        firstname = self.do_send_keys(self.firstName,firstname)
        lastname = self.do_send_keys(self.lastName,lastname)
        zipcode = self.do_send_keys(self.zipCode,zipcode)
        return firstname,lastname,zipcode

    def clickOnContinue(self):
        return self.do_click(self.continueBtn)

    def getProductPrice(self):
        return self.get_all_elements(self.productPrice)

    def getProductPrice(self):

        price_list = self.get_all_elements(self.productPrice)
        prices =[]
        for p in price_list:
            priceText = p.text
            price_without_dollar = priceText.replace('$','') # Remove the dollar sign
            price = float(price_without_dollar) # Convert the value to a float
            prices.append(price) # Collect each price in the list
        return prices

    def getTotalPrice(self):
        finalText = self.get_element_text(self.finalPrice)
        finalprice_split = finalText.split(':')  # This will split the string into ["Item total", " 39.98"]
        final_without_dollar =  finalprice_split[1].strip().replace("$", "")  # Strip any whitespace and convert to float
        final_price = float(final_without_dollar)
        return final_price

    def doFinish(self):
        self.do_click(self.finishBtn)

    def getThankYouMessage(self):
        return self.get_element_text(self.thankYouMessage)