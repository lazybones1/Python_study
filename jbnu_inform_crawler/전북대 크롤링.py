from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import sys, os
from datetime import datetime

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)

page_cnt = 5;
df = pd.DataFrame(columns=['title', 'link', 'date'])

for page in range(1, page_cnt+1):
    url = f"https://www.jbnu.ac.kr/kor/?menuID=139&pno={page}"
    driver.get(url)
    try:
        list = driver.find_elements_by_xpath('//*[@class="page_list"]/table[@class="ta_bo"]/tbody/tr')
        print("find %d page list" %len(list))
    except:
        print("xpath err")
        driver.stop_client()
        dirver.quit()
        sys.exit()

    for i in list:
        soup = BeautifulSoup(i.get_attribute('innerHTML'), 'html.parser')

        title = soup.find('td', {'class':'left'}).find('a')["title"]
        link = soup.find('td', {'class':'left'}).find('a')["href"]
        date = soup.findAll('td', {'class':'mview'}, limit=2)[1].text

        df = df.append({
        'title': title,
        'link': link,
        'date': date
        }, ignore_index=True)
    print(page)

os.makedirs('result', exist_ok=True)
filename = datetime.now().strftime('result/%Y-%m-%d_%H-%M-%S.csv')
df.to_csv(filename, encoding='utf-8-sig', index=False)

driver.stop_client()
driver.quit()
print("done!")
sys.exit()
