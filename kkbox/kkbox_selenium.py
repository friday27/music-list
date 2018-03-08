from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

start = datetime.now()

# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com/")

day365 = pd.date_range("10/18/2017", periods=365, freq='D')
day365 = [day.strftime("%Y-%m-%d") for day in day365]

for day in day365:
	page_start = datetime.now()
	driver = webdriver.Chrome()
	driver.get("https://kma.kkbox.com/charts/daily/song?date="+day)
	time.sleep(1)
	songs = driver.find_elements_by_class_name('charts-list-song')
	singers = driver.find_elements_by_class_name('charts-list-artist')
	songs = [x.text for x in songs if x.text != ""]
	singers = [y.text for y in singers if y.text != ""]

	filename = "./kkbox_tw/" + day + ".txt" 
	with open(filename, "w") as f:
		for i in range(len(songs)):
			song = songs[i].split("-")[0].split("(")[0].strip()
			singer = singers[i].split(",")
			singer_1 = singer[0].strip()
			singer_2 = singer[1].strip() if len(singer) > 1 else ""
			line = "{}\t{}\t{}\n".format(song, singer_1, singer_2)
			# print(line)
			f.write(line)

	print("file: {}, time: {}".format(filename, datetime.now()-page_start))
	driver.close()
print("Execution time: {}".format(datetime.now() - start))
