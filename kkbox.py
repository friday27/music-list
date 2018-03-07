import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

this_year = str(datetime.now().year)
this_month = "{:02d}".format(datetime.now().month)

one_year = []
m = int(this_month)
y = this_year
for month in range(m, m-12, -1):
	if month <= 0:
		month = month + 12
		y = str(int(this_year)-1)
	one_year.append(y+"{:02d}".format(month))
# print(one_year)    

for cal in one_year:
	start_point = datetime.now()
	url = 'https://www.kkbox.com/hk/tc/charts/chinese-monthly-song-' + cal + '.html'
	res = requests.get(url)
	soup = BeautifulSoup(res.text, "lxml")

	song100 = soup.find_all(name="a", attrs={"class": "play-btn"})
	singer100 = soup.find_all(name="h5", attrs={"class": "artist"})

	filename = "./kkbox/kkbox_"+cal+".txt"
	with open(filename, "w") as f:
		for item in zip(song100, singer100):
			song = item[0]['data-name']
			song = song.split("-")[0].strip()

			singer = item[1].get_text()
			singer = singer.split("(")
			singer_1 = singer[0].strip()
			singer_2 = singer[1].split(")")[0].strip() if len(singer) > 1 else ""

			# print("{:15s}\t{:20s}\t{:10s}".format(song, singer_1, singer_2))
			line = "{:15s}\t{:20s}\t{:10s}\n".format(song, singer_1, singer_2)
			f.write(line)

	print("Execution Time: {}, File: {}".format(datetime.now()-start_point, filename))
