from utilities.configurations import *

def addBookPayload(isbn,aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
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
