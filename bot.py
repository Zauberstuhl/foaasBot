#! /usr/bin/env python

from time import gmtime, strftime
from foaas import foaas
from diaspy_client import Client

import re

def log_write(text):
  f = open('bot.log', 'a')
  f.write(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()))
  f.write(text)
  f.write('\n')
  f.close()

client=Client()
notify = client.notifications()
for n in notify:
  if not n.unread: continue
  m = re.search('has\smentioned.*post\s([^\/]+)\s([\@\/\w\-\_\.]+)\.+', str(n))
  if hasattr(m, 'group'):
    client.post(foaas(m.group(2)))
  # finally mark as read
  n.mark()
