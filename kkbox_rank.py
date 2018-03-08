import os

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

			try:
				song_dict[song] += (rank+1)
			except KeyError:
				song_dict[song] = (rank+1)

			pair_dict[song] = [singer_1, singer_2]

print("Songs: ", len(song_dict))

sorted_songs = sorted(song_dict, key=song_dict.get, reverse=False)
with open("./kkbox_songs_tw.txt", "w") as f:
	for song in sorted_songs:
		line = "{}\t{}\t{}".format(song, pair_dict[song][0], pair_dict[song][1])
		# print(line)
		f.write(line)
