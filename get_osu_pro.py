from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sys
import pprint
import re

options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

def htmlwrite(contents):
	path="C:\\Users\\kaiouga02jp\\Desktop\\osu_pro\\osu_pro.html"
	code='<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><meta http-equiv="refresh" content="5; URL="><link rel="stylesheet" type="text/css" href="style.css"><title>osu_pro</title></head><body><div id="content1"><div class="avatar-top"><div class="avatar"></div></div><h1><div id="user_name">'
	code+=contents[0]
	code+='</div></h1></div><div id="content2"><div class="ele1">世界ランキング'
	code+='</div><div class="ele2">'
	code+=contents[2]
	code+='</div><div class="ele1">'
	code+='国別ランキング'
	code+='</div><div class="ele2">'
	code+=contents[4]
	code+='</div><div class="ele1">pp</div><div class="ele2">'
	code+=contents[10]
	code+='</div><div class="ele1">プレイ時間</div><div class="ele2">'
	code+=contents[6]
	code+='</div><div class="ele1">メダル</div><div class="ele2">'
	code+=contents[8]
	code+='</div></div></body></html>'
	f=open(path,"w",encoding="utf-8-sig")
	f.write(code)
 
while True:
	content=[]

	driver.get("https://osu.ppy.sh/users/11030197")

	html = driver.page_source
	
	soup=BeautifulSoup(html,"lxml")
	tests=soup.find_all("span",attrs={"class":"u-ellipsis-overflow"},text=re.compile("kaiouga02jp"))
	for test in tests:
		content.append(test.string)
	tests=soup.select('.profile-header__top')
	for test in tests:
		tests2=test.select('.value-display')
		for test2 in tests2:
			content.append(test2.contents[0].string)
			content.append(test2.contents[1].string)
	htmlwrite(content)
	time.sleep(30)
	del content

driver.quit()

"""
kaiouga02jp
Global Ranking
#15,810
Country Ranking
#985
Total Play Time
2d 22h 2m
Medals
26
pp
3,204
"""
