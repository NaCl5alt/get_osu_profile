from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sys
import pprint
import re
import os

options = Options()
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

def htmlwrite(contents):
	path=os.getcwd()+'\\osu_pro.html'
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
	
	url="https://osu.ppy.sh/users/"

	args = sys.argv
	arg_len = len(args)

	if arg_len < 2:
		user="kaiouga02jp"
		mode="mania"
	elif arg_len >= 3:
		mode=args[2]
		user=args[1]
	else:
		mode="mania"
		user=args[1]

	url+=user+"/"+mode

	driver.get(url)

	html = driver.page_source
	
	soup=BeautifulSoup(html,"lxml")
	texts=soup.find_all("span",attrs={"class":"u-ellipsis-overflow"},text=re.compile(user, re.IGNORECASE))
	for text in texts:
		content.append(text.string)
	texts=soup.select('.profile-header__top')
	for text in texts:
		texts2=text.select('.value-display')
		for text2 in texts2:
			content.append(text2.contents[0].string)
			content.append(text2.contents[1].string)

	htmlwrite(content)
	time.sleep(30)
	del content

driver.quit()
