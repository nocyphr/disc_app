from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    context.driver = webdriver.Chrome(options=options)



# This function will be called after all features are executed
def after_all(context):
    context.driver.quit()


@given(u'the url \'{url}\'')
def step_impl(context, url):
    context.url = url


@when(u'I visit the url')
def step_impl(context):
    context.driver.get(context.url)


@then(u'the element {element} with text {text} is found')
def step_impl(context, element, text):
    # Wait up to 10 seconds for at least one element to be present
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, element))
    )
    
    # Fetch all elements of the given type
    elements = context.driver.find_elements(By.TAG_NAME, element)
    
    # Check each element to see if the desired text is present
    matching_texts = [elem.text for elem in elements if text in elem.text]
    
    # Assert that at least one element contained the desired text
    assert_that(matching_texts).is_not_empty()
