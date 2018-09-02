from collections import Counter
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    dList = []
    for key in aDict:
       if list(aDict.values()).count(aDict[key]) == 1:
           dList.append(key)
        
    
    return sorted(dList)





aDict = {1: 1, 2: 1, 3: 1}
print(uniqueValues(aDict))