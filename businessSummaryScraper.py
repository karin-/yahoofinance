"""
The following will iterate through each stock ticker (as listed in stockList)
and throw into the variable "text" each of the business sumarries for each stock
as provided by Yahoo Finance.
"""

import urllib2

def getSummaries(stockList):
    text = []
    for stock in stockList:
        url = "http://finance.yahoo.com/q/pr?s=" + stock
        html = urllib2.urlopen(url).read()
        counter = 0
        pStart = 0
        while counter < 2:
            pStart += html[pStart:].find("Business Summary")
            counter += 1
        pEnd = html.find("</p>", pStart)
        text += [html[pStart + 73 : pEnd]]
    return text

### Example
stockList = ["aapl", "goog", "msft", "fb"]
text = getSummaries(stockList)
text[0]; text[1]; text[2]; text[3]

