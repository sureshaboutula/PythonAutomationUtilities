from utilities.configurations import *

def addBookPayload(isbn):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "927",
        "author": "Johnt Dude"
    }
    return body

def addBookPayload2(isbn, aisle):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Johnt Dude"
    }
    return body

def buildPayloadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody