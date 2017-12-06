import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_21998.json?'


# address = input('Enter location: ')
# if len(address) < 1: break

# url = serviceurl + urllib.parse.urlencode({'address': address})
url=serviceurl
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
# tree = ET.fromstring(data)
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print('lat', lat, 'lng', lng)
#     print(location)
#
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Chuck"
#   }
# ]'''

info = json.loads(data)
comments=info['comments']
# print(comments)
# print('Count:', len(info))
sum=0
for item in comments:
    count=item['count']
    count=int(count)
    sum=sum+count

print("Count:",len(comments))
print("Sum:",sum)
    #
    # print('Name', item['name'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])
