from requests import get
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given(u'the url \'{url}\'')
def step_impl(context, url):
    context.url = url


@when(u'I visit the url')
def step_impl(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    context.driver = webdriver.Chrome(options=options)
    context.driver.get(context.url)



@then(u'the element {element} with text {text} is found')
def step_impl(context, element, text):
    # Wait up to 10 seconds for an h2 element to be present
    content = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, element))
    )
    
    result = content.text
    context.driver.quit()
    assert_that(result).is_equal_to(text)

    