
import urllib.request,urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
serviceurl='http://py4e-data.dr-chuck.net/comments_21997.xml?'

address = serviceurl#input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print('Count:', len(results))
    # lat = results[0].find('name').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
sum=0
counts=tree.findall('.//count')
for item in counts:
    count=item.text

    count=int(count)
    sum=sum+count
#
print('Sum:',sum)
