s = 'Аз съъм куммааррдд'
temp = s[0]   #temporary variable I use to change longest
longest = ''   
for i in range(len(s)-1):
    if s[i] <= s[i+1]:  #checks if it's in alphabetical order
        temp+=s[i+1]
        if len(longest) < len(temp):
           longest  = temp       
    else: 
        temp = s[i+1]     #reset temp after every substring
    if len(longest) < len(temp):
        longest  += temp    #update longest if the new substring is longer
    if longest == 'y':
        longest = 'z'

    

print('Longest substring in alphabetical order is:', longest)