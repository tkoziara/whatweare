# -*- coding: iso-8859-13
import os

def replace_style (filename, style1):
  with open(filename) as f: s = f.read()
  style0 = s[s.find('<style>')+8:s.find('\n</style>')]
  s = s.replace(style0, style1)
  with open(filename, 'w') as f: f.write(s)

matches = []

for root, dirnames, filenames in os.walk('en'):
    for filename in filenames:
      if filename.endswith('.html'):
	matches.append(os.path.join(root, filename))

for root, dirnames, filenames in os.walk('pl'):
    for filename in filenames:
      if filename.endswith('.html'):
	matches.append(os.path.join(root, filename))

with open('style.html') as f: style = f.read()
style = style[style.find('<style>')+8:style.find('\n</style>')]
for filename in matches:
  n = filename.count('/')
  x = y = '../'
  for j in range(1,n): y += x
  style1 = style.replace(x, y)
  replace_style (filename, style1)
