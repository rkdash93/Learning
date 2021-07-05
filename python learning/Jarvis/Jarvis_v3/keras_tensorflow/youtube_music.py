import re
import urllib,requests

def y_search(search):
    search=search.replace('play ','')
    y_song='Playing ' + search
    print(y_song + '....')                    
    search=search.replace(' ','+')
    print(search)
    youtube = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)
    #print(youtube.read().decode())
    video_ids = re.findall(r'watch\?v=(\S{11})',youtube.read().decode())
    print(video_ids)
    y_url = "https://www.youtube.com/watch?v=" + str(video_ids[0])
    return y_song,y_url