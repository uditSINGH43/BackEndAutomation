from utilities.configurations import *

def addBookPayload(isbn):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "227",
        "author": "John foe"
    }
    return body




def buildPayLoadfromDB(query):
    addbody = {}
    tp = getQuery(query)
    addbody["name"] = tp[0]
    addbody['isbn'] = tp[1]
    addbody["aisle"] = tp[2]
    addbody["author"] = tp[3]
    return addbody
