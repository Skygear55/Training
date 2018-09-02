 
s = 'hdbobbbobobobobobobooboobobobob'
 

count = i = 0
while True:
    j = s.find('bob', i)
    if j == -1 :
        break
    count += 1 
    i = j + 1
        
    

print('Number of times bob occurs is: '+str(count))       