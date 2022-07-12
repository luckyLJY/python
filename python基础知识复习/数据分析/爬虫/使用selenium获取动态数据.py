from selenium import webdriver
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get ('http://q.stock.sohu.com/cn/600519/1shq.shtml')
em = driver.find_element_by_id('BIZ_hq_historySearch')
print(em.text)
driver.quit()