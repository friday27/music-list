import os
import re

def remove_punctuation(line):
	rule_zh = re.compile(u"[^0-9\u4e00-\u9fa5]")  # [^a-zA-Z0-9\u4e00-\u9fa5]
	line_zh = rule_zh.sub('',line)
	rule_en = re.compile(u"[^a-zA-Z0-9]")
	line_en = rule_en.sub('',line)
	return line_zh, line_en

for dirs, _, filenames in os.walk("./kkbox_tw/"):
	txt_files = ["./kkbox_tw/"+x for x in filenames if x[-4:] == ".txt"]

song_dict = dict()
pair_dict = dict()

for txt in txt_files:
	with open(txt, "r") as f:
		pairs = f.readlines()

		for rank, pair in enumerate(pairs):
			pair = pair.split("\t")
			song = pair[0]
			
			singer_1 = pair[1]
			singer_2 = pair[2] if len(pair) > 2 else ""
			singer_1_zh, singer_1_en = remove_punctuation(singer_1)
			singer_2_zh, singer_2_en = remove_punctuation(singer_2)

			try:
				song_dict[song] += (rank+1)
			except KeyError:
				song_dict[song] = (rank+1)

			pair_dict[song] = [singer_1_zh, singer_1_en, singer_2_zh, singer_2_en]

print("Songs: ", len(song_dict))

sorted_songs = sorted(song_dict, key=song_dict.get, reverse=False)
with open("./kkbox_songs_tw.txt", "w") as f:
	for song in sorted_songs:
		line = "{}\t{}\t{}\t{}\t{}\n".format(song, pair_dict[song][0], pair_dict[song][1], pair_dict[song][2], pair_dict[song][3])
		# print(line)
		f.write(line)
