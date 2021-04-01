#This is CBPP(Compare Book Price Program) for homework
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome('C:\Users\a\Downloads\chromedriver_win32')

#Make  used book site
base_Url_kyobo = 'https://search.kyobobook.co.kr/web/search?vPstrKeyWord='
plusUrl_name = input("교보문고에서 찾는 중고책 이름을 입력하세요: ")
k_book_name = base_Url_kyobo + urllib.parse.quote_plus(plusUrl_name)
#Sum links
k_url = k_book_name+'&searchPcondition=1&collName=USED&vPstrTab=USED&from_coll=USED&currentPage=1&orderClick=LIP'

#read url and make html var
kyobo_html = urllib.request.urlopen(k_url).read()

soup = BeautifulSoup(kyobo_html,'html.parser')

#check booknumber
booknumber = soup.select('#searchCategory_0 small')[0].text

print()
print("관련된 검색물이"+booknumber+"개 있습니다.")
print()

if(int(booknumber)>20):
    print("목록이 너무 많아 1page만 보여드립니다.")
    count=20
else:
    count=int(booknumber)

print('*******이하 목록*******')

for i in range(count):
    title = soup.select('.type_list .detail strong')[i].text
    price = soup.select('.sell_price strong')[i].text
    status = soup.select('.price .status')[i].text

    print()
    print("제목:"+title)
    print("금액: "+price)
    print("품질: "+status[4:6])
    print()
        
print('*******출력 종료*******')
print()

print('--------------------여기까지 교보문고였습니다.--------------------')
print()

#-------------------------------여기까지가 인터넷 교보문고 결과물 -------------------------------

#Make  used book site
base_Url_Aladin = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord='
plusUrl_name = input("알라딘에서 찾는 중고책 이름을 입력하세요: ")
A_book_name = base_Url_Aladin + urllib.parse.quote_plus(plusUrl_name)

#Aladin can just use so there is NO sum process

#read url and make html var
Aladin_html = urllib.request.urlopen(A_book_name).read()

soup1 = BeautifulSoup(Aladin_html,'html.parser')

brower.get(A)
#check booknumber
a_booknumber = soup1.select('.search_t_g .ss_f_g_l')[0].text

print()
print("관련된 검색물이"+a_booknumber+"개 있습니다.")
print()

if(int(a_booknumber)>25):
    print("목록이 너무 많아 1page만 보여드립니다.")
    count=25
else:
    count=int(a_booknumber)

print('*******이하 목록*******')



for i in range(count):
    #title = soup1.select('.usedtable01 bo_used b')[i].text
    price = soup1.select('.usedtable01 .bo_used b')[i].text
    #상품품질 미구현
    #status = soup.select('.price .status')[i].text

    print()
    #print("제목:"+title)
    print("금액: "+price)
    #print("품질: "+status[4:6])
    print()
        
print('*******출력 종료*******')
print()

print('--------------------여기까지 알라딘이었습니다.--------------------')
print()
