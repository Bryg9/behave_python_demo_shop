from behave import given, when, then
from selenium import webdriver
from time import sleep


url = "https://www.saucedemo.com/"


@given('I launch the browser')
def launchBrowser(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    sleep(3)


@when('open saucedemo.com page')
def openSauceDemoPage(context):
    context.driver.get(url)


@then('verify if the logo is present on main page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath('//div[@class="bot_column"]').is_displayed()# noqa
    assert status is True
    sleep(3)


@then('close browser')
def closeBrowser(context):
    context.driver.close()
