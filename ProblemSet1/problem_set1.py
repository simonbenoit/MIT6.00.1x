# Problem 1 
# Counting vowels

list = ('a','e','i','o','u')
vowel = 0

for char in s:
    if char in list:
        vowel += 1
        
print ('Number of vowels :' +str(vowel))

# Problem 2
# Counting bobs

count = 0
idx = 0
while True:
    idx = s.find('bob', idx)
    if idx >=0:
        count += 1
        idx +=1
    else:
        break
print ('Number of times bob occurs is:' +str(count))

#Problem 3
# Alphabetical substrings

def longest_alpha_sub(string):
    '''
    string = string receive in argument
    sub = substring containing the longest substring in alphabetical
    cur = current sequence
    '''
    string = string.lower() 

    sub = cur = string[0] 
    
    for char in string[1:]:
        if char >= cur[-1]:
            cur += char
        else:
            cur = char
            
        if len(cur) > len(sub):
            sub = cur

    return sub
