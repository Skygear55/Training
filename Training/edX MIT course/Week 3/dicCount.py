animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    dList = []
    num = 0
    for value in aDict.values():
        dList.extend(value)
        
    for element in dList:
        num +=1
    return num


print(how_many({'B': [15], 'u': [10, 15, 5, 2, 6]}))

superheroes = (
    ('deadpool', 'regeneration and bad judgement'),
    ('superman', 'everything but Kyptonite'),
('tick', 'daft as a brush but pretty much invincible, bulletproof, superstrong and blue'),
    ('spiderman', 'athletic but poor sense of humour'),
)