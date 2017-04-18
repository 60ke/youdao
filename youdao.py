import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
data = {}
data['type']= 'AUTO'
data['i'] = 'my'
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] ='UTF-8'
data['action'] ='FY_BY_ENTER'
data['typoResult'] ='true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
target = json.loads(html)
print(target)

print(html)