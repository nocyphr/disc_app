from requests import get
from assertpy import assert_that
from selenium import webdriver


@given(u'the url \'{url}\'')
def step_impl(context, url):
    context.url = url


@when(u'I visit the url')
def step_impl(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)

    driver.get(context.url)
    context.result = driver.page_source     
    driver.quit()


@then(u'the text {text} is found')
def step_impl(context, text):
    assert_that(context.result).contains(text)
    