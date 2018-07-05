import requests
import re

city_choose_dict = {
    '1':"重庆",
    '2':"武汉"
}

city_dict = {
    '1':'zhongqing',
    '2':'wuhan',
}

for show in city_choose_dict:
    print(show, ': ', city_choose_dict[show])

num = input("选择你要关注的City:\n")

city_s = city_dict[num]
s = requests.session()
url = 'http://www.yinhangzhaopin.com/'
r = s.get(url)

pattern_sh1 = re.compile('sh-nr.*?<ul>(.*?)</ul>', re.S)
pattern_sh2 = re.compile('sh-nr-1.*?<ul>(.*?)</ul>', re.S)

result1 = re.search(pattern_sh1, r.text)
result2 = re.search(pattern_sh2, r.text)
result = result1.group(1)+result2.group(1)

key_str = '<li><a href="(.*?'+city_s+'.*?)"'
pattern_city_link = re.compile(key_str)

city_link = re.search(pattern_city_link, result).group(1)

pattern_bank = re.compile('<dl>(.*?)</dl>', re.S)
r = s.get(city_link)
results = re.findall(pattern_bank, r.text)
for result in results:
    title = re.search('title.*?>(.*?)</a>', result, re.S).group(1)
    detail_link = re.search('<a href="(.*?)"', result, re.S).group(1)

