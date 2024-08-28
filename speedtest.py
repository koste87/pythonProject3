from selenium.webdriver import Chrome

driver = Chrome()
driver.get("http://google.com")

element = driver.find_element_by_xpath("//inout[@name='q']")

element.send_keys("Selenium")

driver.quit()
