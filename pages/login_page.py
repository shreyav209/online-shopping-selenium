
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
        print(self.get_all_elements(self.allproducts))
        return self.get_all_elements(self.allproducts)

    def addProductToCart(self,product_name):
        products = self.getProductList()
        for product in products:
            productText = product.text
            if productText in product_name:
                # print('<<<< inside if >>>>')
                add_btn = product.find_element(By.XPATH,"//button[contains(@id,'add-to-cart')]")
                add_btn.click()

    def clickOnCart(self):
        self.do_click(self.cartBtn)
        # print(self.get_element_text(self.cartCount))
        # return self.get_element_text(self.cartCount)


class CheckoutPage(ProductPage):

    checkout_btn = (By.ID,'checkout')
    firstName = (By.ID,'first-name')
    lastName = (By.ID,'last-name')
    zipCode = (By.ID,'postal-code') 
    continueBtn = (By.ID,'continue')
    productPrice = (By.XPATH,"//div[@class ='inventory_item_price']")
    finalPrice = (By.XPATH,"//div[@class ='summary_subtotal_label']")

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
        print(self.get_all_elements(self.productPrice))
        return self.get_all_elements(self.productPrice)

    def getProductPrice(self):

        price_list = self.get_all_elements(self.productPrice)
        for p in price_list:
            priceText = p.text
            print('<<<< priceText >>>>',priceText)
            price_without_dollar = priceText.replace('$','')
            print(price_without_dollar)
            price = price_without_dollar.split('.')
            print(price)
        print(p.find_element(By.XPATH,"//div[@class ='inventory_item_price']"))
        return p.find_element(By.XPATH,"//div[@class ='inventory_item_price']")

    def getTotalPrice(self):
        final_price = self.get_element_text(self.finalPrice)
        # finalPriceText = final_price.text
        print('<<<< priceText >>>>',final_price)
