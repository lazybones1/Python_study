from selenium import webdriver

url = 'http://www.naver.com'

browser = webdriver.Chrome('./chromedriver')
browser.get(url)

login_bt = browser.find_element_by_class_name('link_login')
login_bt.click()

id=browser.find_element_by_id('id')
id.send_keys('id input')

pw=browser.find_element_by_id('pw')
pw.send_keys('pw input')

naver_submit = browser.find_element_by_class_name('btn_global')
naver_submit.click()

browser.stop_client()
browser.close()
