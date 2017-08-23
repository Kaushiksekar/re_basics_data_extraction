#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import urllib2

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  
  year=filename.split("//")[-1].split(".")[0].strip("baby")
  html_response=urllib2.urlopen(filename)
  html_string=html_response.read()
  list1=re.findall(r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",html_string)
  list2=[]
  list2.append(year)
  for a in range(len(list1)):
	list2.append(str(list1[a][1])+" "+str(list1[a][0]))
	list2.append(str(list1[a][2])+" "+str(list1[a][0]))
  list2.sort()
  return list2


def main():
  args = sys.argv[1:]
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  list1=list(set(extract_names(args[0])))
  list1.sort()
  year=args[0].split("//")[-1].split(".")[0].strip("baby")
  f=open("baby_names_"+year+"_ranking.txt","a")
  f.seek(0)
  f.truncate()
  for a in list1:
	if summary:
	  f.write(a+"\n")
	else:
	  print a
  f.close()
if __name__ == '__main__':
  main()