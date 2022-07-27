from pytube import 
from sys import argv

link = argv[1]
yt = YouTube(link)

print ("title ",yt.title)
print ('view ',yt.views)

yd = yt.streams.get_highest_resulotion()
yd.dowmload('Users/ACER/OneDrive/Documents/belajar python/tugas_tugas/ed')