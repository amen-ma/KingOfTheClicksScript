from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


base_url = "https://kingoftheclicks.com/?ref=memeguel"


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)



driver.get(base_url)

print(driver.title)

driver.maximize_window()
driver.implicitly_wait(20)
actions = ActionChains(driver)

helpMiggy1 = driver.find_element_by_xpath("//button[@class='btn advance border red']")
driver.implicitly_wait(2)
helpMiggy2 = driver.find_element_by_xpath("//span[@class='btn border teal']")


helpMiggy1.click()
actions.click(helpMiggy2)

for i in range(1):
	actions.perform()
	count = helpMiggy2.text
	print(count)