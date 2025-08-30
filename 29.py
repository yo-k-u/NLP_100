import urllib.request
import urllib.parse
import json

filename = 'Flag of the United Kingdom.svg'
encoded_filename = urllib.parse.quote(filename)
url = f'https://www.mediawiki.org/w/api.php?action=query&titles=File:{encoded_filename}&format=json&prop=imageinfo&iiprop=url'

connection = urllib.request.urlopen(urllib.request.Request(url))
response = json.loads(connection.read().decode())
print(response['query']['pages']['-1']['imageinfo'][0]['url'])