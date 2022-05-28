from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,"email")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkBox = (By.ID,"exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH,"//input[@value='Submit']")
    successMessage = (By.CLASS_NAME,"alert-success")

    def __init__(self,driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return  self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return  self.driver.find_element(*HomePage.successMessage)