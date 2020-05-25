from selenium import webdriver #웹페이지를 자동으로 테스트할 때 자수 사용 툴
from bs4 import BeautifulSoup #HTML 파싱 패키지
import time, os
from datetime import datetime
import pandas as pd

link = 'https://play.google.com/store/apps/details?id=com.miso&hl=ko&showAllReviews=true' #원하는 페이지의 링크

scroll_cnt = 10 #원하는 스크롤 수

#크롬드라이버 다운 :https://sites.google.com/a/chromium.org/chromedriver/home
driver = webdriver.Chrome('./chromedriver') #크롬 드라이버 경로
driver.get(link) #크롬드라이버에게 링크로 접속하라고 명령

os.makedirs('result', exist_ok=True) #새로운 폴더를 만든다

for i in range(scroll_cnt): #scroll_cnt만큼 for문
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #드라이버에게 ''문장의 자바 스크립트 실행 명령
  time.sleep(3)

  #더보기 버튼이 존재할경우 클릭
  try:
    #find_element_by_epath() XML문서에서 노드의 위치를 찾을 때 사용
    load_more = driver.find_element_by_epath('//*[contains(@class,"U26fgb 00WRKf oG5Srb C0oVfc n9lfj")]').click()
  except:
    print('Cannot find load more button...')

#리뷰 컨테이너 찾기
reviews = driver.find_elements_by_xpath('//*[@jsname="fk8dgd"]//div[@class="d15Mdf bAhLNe"]')

print('There are %d reviews avaliable!' %len(reviews))
print('Writing the data...')

#pd.DataFrame() : 빈 데이터 프레임 생성
df = pd.DataFrame(columns=['name', 'ratings', 'date', 'helpful', 'comment', 'developer_comment'])

#리뷰 데이터 찾기
for review in reviews:
  #html parser를 이용해서 parsing
  #get_attribute('innerHTML') : Html요소를 text형태로 가져온다
  soup = BeautifulSoup(review.get_attribute('innerHTML'), 'html.parser')

  #리뷰 작성자 찾기
  #soup.find : 파싱된 html에서 요소를 찾기
  name = soup.find(class_='X43Kjb').text

  #리뷰 평점 찾기
  ratings = int(soup.find('div', role='img').get('aria-label').replace('별표 5개 만점에', '').replace('개를 받았습니다.', '').strip())

  #리뷰 날짜 찾기
  date = soup.find(class_='p2TkOb').text
  date = datetime.strptime(date, '%Y년 %m월 %d일')
  date = date.strftime('%Y-%m-%d')

  #helpful
  helpful = soup.find(class_='jUL89d y92BAb').text
  if not helpful:
    helpful = 0

  #review text
  comment = soup.find('span', jsname='fbQN7e').text
  if not comment:
    comment = soup.find('span', jsname='bN97Pc').text

  #developer comment
  developer_comment = None
  dc_div = soup.find('div', class_='LVQB0b')
  if dc_div:
    developer_comment = dc_div.text.replace('\n', ' ')

  #append to dataframe
  #df.append() 데이터 프레임에 행을 추가하여 데이터 삽입
  df = df.append({
    'name':name,
    'ratings': ratings,
    'date': date,
    'helpful': helpful,
    'comment':comment,
    'developer_comment': developer_comment
  }, ignore_index=True)

  #scv 파일로 데이터프레임 저장
  filename = datetime.now().strftime('result/%Y-%m-%d_%H-%M-%S.csv')
  #df.to_csv() csv파일로 저장
  df.to_csv(filename, encoding='utf-8-sig', index=False)
  driver.stop_client() #selenium클라이언트 종료
  driver.close() #드라이버 종료

  print('Done!')
