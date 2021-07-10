from behave import given, when, then
from selenium import webdriver
from time import sleep


url = "https://www.saucedemo.com/"


@given('I open the browser')
def launchBrowser(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    sleep(3)


@given('open saucedemo.com page')
def openSauceDemoPage(context):
    context.driver.get(url)


@then('I log into the online shop')
def logIn(context):
    loginForm = context.driver.find_element_by_xpath('//input[@placeholder="Username"]')# noqa
    loginForm.click()
    loginForm.send_keys("standard_user")

    passwordForm = context.driver.find_element_by_xpath('//input[@placeholder="Password"]')# noqa
    passwordForm.click()
    passwordForm.send_keys('secret_sauce')

    btnLogin = context.driver.find_element_by_id("login-button").click()# noqa
    sleep(3)


@then('I reset app state')
def resetApp(context):
    burgerMenu = context.driver.find_element_by_id("react-burger-menu-btn").click()# noqa
    resetAppState = context.driver.find_element_by_id("reset_sidebar_link").click()# noqa
    sleep(3)
    closeBurgerMenu = context.driver.find_element_by_id("react-burger-cross-btn").click()# noqa


@when('I add Sauce Labs Bolt T-Shirt into the cart')
def addProduct(context):
    addTshirt = context.driver.find_element_by_xpath('//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()# noqa
    shoppingCart = context.driver.find_element_by_xpath('//a[@class="shopping_cart_link"]').click()# noqa
    productInCart = context.driver.find_element_by_xpath('//div[@class="inventory_item_name"]')# noqa
    productInCart_text = productInCart.text
    assert "Sauce Labs Bolt T-Shirt" == productInCart_text


@then('I place an order')
def placeOrder(context):
    checkoutButton = context.driver.find_element_by_id("checkout").click()# noqa

    firstName = context.driver.find_element_by_id("first-name")
    firstName.click()
    firstName.send_keys("John")

    lastName = context.driver.find_element_by_id("last-name")
    lastName.click()
    lastName.send_keys("Stone")

    postalCode = context.driver.find_element_by_id("postal-code")
    postalCode.click()
    postalCode.send_keys("12-345")

    continueButton = context.driver.find_element_by_id("continue").click()# noqa
    sleep(2)

    itemNameCheck = context.driver.find_element_by_xpath('//div[@class="inventory_item_name"]')# noqa
    itemNameCheck_text = itemNameCheck.text
    assert "Sauce Labs Bolt T-Shirt"  == itemNameCheck_text# noqa
    sleep(2)

    finishButton = context.driver.find_element_by_id("finish").click()# noqa

    afterOrder = context.driver.find_element_by_xpath('//h2[@class="complete-header"]')# noqa
    afterOrder_text = afterOrder.text
    assert "THANK YOU FOR YOUR ORDER" == afterOrder_text


@then('I log out')
def logOut(context):
    burgerMenu = context.driver.find_element_by_id("react-burger-menu-btn").click()# noqa
    sleep(2)
    logoutButton = context.driver.find_element_by_xpath('//a[@id="logout_sidebar_link"]').click()# noqa
    btnLogin = context.driver.find_element_by_id("login-button").is_displayed()# noqa
    sleep(2)


@then('I close browser')
def closeBrowser(context):
    context.driver.close()
