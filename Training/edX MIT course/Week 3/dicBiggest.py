def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
  
    max_length = max(map(len,aDict.values()))
    for key in aDict:
        if len(aDict[key]) == max_length:
            return key
      
    
    
    
#another one :
def biggest(aDict):
    freq, freq_max = None, 0
    for el in aDict.keys():
        if len(aDict[el]) > freq_max:
            freq, freq_max = el, len(aDict[el])
    return freq
#The listcomp, functional version looks like

return max((len(v), k) for k, v in aDict.items())[1]