import numpy as nu
import urllib.request
import re

filename = 'websites.txt'
output_filename   = 'results.txt'

websites = []
with open(filename, 'r') as file:
  for line in file:
    line = line.strip().lower()
    if not re.match(r'http', line):
      line = 'http://www.'+line
    websites.append(line)

size = len(websites)

with open(output_filename, 'w') as file:
  for url, i in zip(websites, range(size)):
    print('{}/{} - {}'.format(i, size, url))
    try:
      response = urllib.request.urlopen(url)
      html = str(response.read())
      match = re.findall(r'(?:[a-zA-Z0-9_\-\.]+)@(?:[a-zA-Z0-9_\-\.]+)\.(?:[a-zA-Z]{2,5})', html)
      if match == None:
        file.write('{}\t{}\t{}\n'.format(i, url, 'None'))
      else:
        file.write('{}\t{}\t{}\n'.format(i, url, match))
    except:
      file.write('{}\t{}\t{}\n'.format(i, url, 'ERR'))
  

