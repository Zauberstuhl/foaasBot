#!/usr/bin/env python

import re
import urllib2
import config

def foaas(command):
  mention = "\n\n#foaas "
  m = re.search("([^@\/\s]+@[^@]+\.[^@\/\s]+)", command, re.I)
  if hasattr(m, 'group'):
    mention += "@{"+m.group(1)+" ; "+m.group(1)+"}"
    command = re.sub("([^@\/\s]+)@[^@]+\.[^@\/\s]+", r'\1', command)

  request = urllib2.Request(
    config.apiurl+command.replace(' ', '__'),
    headers={"Accept" : "text/plain",
    "User-Agent": "diasporaBot/1.0.0"}
  )
  contents = urllib2.urlopen(request).read()
  return contents.replace('__', ' ') + mention
