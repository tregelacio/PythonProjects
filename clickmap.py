from selenium import webdriver

url = 'http://google.com'
driver = webdriver.Chrome()
driver.get(url)

element = driver.find_element_by_id("fakebox-input")
element.click()