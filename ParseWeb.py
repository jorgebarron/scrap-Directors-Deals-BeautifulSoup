
#--------------------import--------------------
from bs4 import BeautifulSoup
import urllib.request
import time
import os

#----------------------------------------------
# variables used to locate the relevant data in the source code

# string from the source code located before the relevant data
topSplit = 'Data provided by Directors Holdings'
# string from the source code used to locate the last item
bottomSplit = '<< Previous page Next page >>'

#----------------------------------------------

def ParseWeb(numberPages):
    
    # returns just the director's deals from the source code
    def textSelection (soup, topSplit, bottomSplit):
        WebContent = soup.body.text

        topIndex = WebContent.index(topSplit) + len(topSplit)
        buttonIndex = WebContent.index(bottomSplit)

        TotalLen = len(WebContent)
        DirectorsDealsList = (WebContent[topIndex:buttonIndex])
        DirectorsDealsList = ("".join([s for s in DirectorsDealsList.strip().splitlines(True) if s.strip("\r\n").strip()]))

        return DirectorsDealsList

    # use today's date in ddmmyy format for txt file name
    todaysDate = str(time.strftime("%d%b%y"))
    
    numberPages = int(numberPages)
    counterPages = 0

    #open website. read. apply formatting. 
    for x in range (1, numberPages + 1):
        response = urllib.request.urlopen('http://www.moneyam.com/director-deals/index/page/%d' % x)
        html = response.read()
        soup = BeautifulSoup(html)
        DirectorsDeals = (textSelection (soup, topSplit, bottomSplit))
        # create txt file for each page
        outfile = open('WebContent%sCleanDeals%d.txt' % (todaysDate,x),'w')
        outfile.write(DirectorsDeals)
        outfile.close()
        print ('Page', x ,'has been processed')


numberPages = int(input("enter number of pages you want to parse: "))
ParseWeb(numberPages)

    
