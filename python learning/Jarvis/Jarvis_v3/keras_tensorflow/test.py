import urllib,re
import requests,json

old_url = 'https://www.youtube.com/results?search_query='
youtube = urllib.request.urlopen('https://www.youtube.com/results?search_query=bulleya')
#print(youtube.read().decode())
video_ids = re.findall(r'watch\?v=(\S{11})',youtube.read().decode())
print(video_ids)
# url = "https://www.youtube.com/watch?v=" + str(video_ids[0])
# print(url)