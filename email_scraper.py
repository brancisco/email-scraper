import numpy as np
import re
import requests

urls_fname = 'websites.txt'
out_fname  = 'results.txt'
log_fname  = 'err.log'

urls = []
with open(urls_fname, 'r') as file:
  for line in file:
    if not re.match(r'http', line):
      line = 'http://www.'+line
    urls.append(line.strip('\n').lower())

def fout(fname, url, message):
  with open(fname, 'a') as lfile:
    lfile.write('{} - {}\n'.format(url, message))

def print_status(i, size, activity):
  each_step = size/10
  done = int(i/each_step)
  left = 10 - done
  loader = ''
  if i%2 == 0:
    loader = '%'
  if i%2 == 1:
    loader = '&'
  print('|{}{}| {} {}{}\n'.format(''.join(['*']*done), ''.join(['-']*left), loader, activity, ''.join([' ']*10)), end='')

def linked(url, link):
  if not re.match(r'http', link) and not re.findall(r'www', link):
    if link[0] == '/':
      link = link[1:]
    add = ''
    if url[-1] != '/':
      add = '/'
    link = url + add + link
    
  return link

with open(out_fname, 'w') as foo: pass

i = 0
size = len(urls)
for url in urls:
  print_status(i, size, 'requesting {}'.format(url))
  emails = []
  try:
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
      emails += re.findall(r'(?:[a-zA-Z0-9_\-\.]+)@(?:[a-zA-Z0-9_\-\.]+)\.(?:[a-zA-Z]{2,5})', r.text)
      links = re.findall(r"<a href=(?:\"|')((?:http(?:s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#\[\]@!\$&'\(\)\*\+,;=.]+)(?:\"|')>(.+)<\/a>", r.text)
      links += re.findall(r"<a[\s]+href=(?:'|\")([^>]+)(?:'|\")[\s]+>((?:.(?!\<\/a\>))*.)<\/a>", r.text)
      j = 0
      lsize = len(links)
      for link in links:
        if re.search(r'contact', link[1].lower()):
          dalink = linked(url, link[0])
          print(dalink)
          print_status(j, lsize, 'link {}'.format(dalink))
          r_link = requests.get(dalink)
          emails += re.findall(r'(?:[a-zA-Z0-9_\-\.]+)@(?:[a-zA-Z0-9_\-\.]+)\.(?:[a-zA-Z]{2,5})', r_link.text)
        j += 1
      fout(out_fname, url, list(set(emails)))
    else:
      fout(out_fname, url, r.status_code)
  except Exception as e:
    fout(out_fname, url, 'err logged')
    fout(log_fname, url, e)
  i += 1

