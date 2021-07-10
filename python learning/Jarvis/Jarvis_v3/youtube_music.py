import re
import urllib,requests

def y_search(search,h_e_param):
    if h_e_param == 'e':
        search=search.replace('play ','')
    elif h_e_param == 'h':
        search=search.replace('sunao ','')                    
    search=search.replace(' ','+')
    print(search)
    youtube = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)
    #print(youtube.read().decode())
    video_ids = re.findall(r'watch\?v=(\S{11})',youtube.read().decode())
    #print(video_ids)
    y_url = "https://www.youtube.com/watch?v=" + str(video_ids[0])
    return y_url

  