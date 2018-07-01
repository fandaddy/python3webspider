##Top 100 Movies in Maoyan

import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

pattern_split = re.compile('<dd>(.*?)</dd>', re.S)
pattern_search_title = re.compile('title="(.*?)"')
pattern_search_stars = re.compile('star.*?>(.*?)</p>', re.S)
pattern__releasetime = re.compile('<p class="releasetime">(.*?)</p>')
j = 0
for i in range (0,10):
    s = requests.session()
    url = 'http://maoyan.com/board/4?offset='+str(i);
    r = s.get(url, headers=headers)
    results = re.findall(pattern_split, r.text)
    for result in results:
        j = j + 1
        title = re.search(pattern_search_title, result)
        stars = re.search(pattern_search_stars, result)
        releasetime = re.search(pattern__releasetime, result)
        print(j)
        print('Movie:'+title.group(1))
        print('Stars:'+stars.group(1).strip()[3:])
        print('Release Time:'+releasetime.group(1))



