"""
cryptography.py
Author: Jackson Tolliday
Credit: https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters, https://stackoverflow.com/questions/31175223/append-a-tuple-to-a-list-whats-the-difference-between-two-ways

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associationsn = list(associations)
associationsnu = list(range(len(associationsn)))
letternumzip = list(zip(associationsn, associationsnu))
ltrnumdict = dict(letternumzip)

print(ltrnumdict)

'''
def scramble(message): #, key, direction
    for x,y in letternumzip:
        c = 0
        if c in list(message) == y:
            leftover = range(len(message))
            message.append(x)
            c = c+1
print(scramble('Hello, World!'))
'''

def numbs(message, key): # direction
    alist = []
    blist = []
    message = list(message)
    key = list(key)
    tkey = len(message)/ len(key)
    zipmsgkey = list(zip(message, key))
    print(tkey)
    
'''
    for c in message:
        for a in key:
            alist.append(tuple([c, a]))
            length = list(range(len(message) * (len(key))))
            print(alist)
            prep = ((len(key))*2 + 3)
            blist.append((alist[0]))
                                #pattern for key 3: leave 1, then del 3, leave 1, del 3, leave 1. total var; 9
                                #pattern for key 2: leave 1, then del 2, leave 1, del 2, leave 1. total var; 7
'''

numbs('hello world!', 'hill')

'''
dore = input(str('Enter e to encrypt, d to decrypt, or q to quit: '))
run = True
rerun = False
while run == True:
    if rerun == False:
        if dore == 'e' or dore == 'd':
            basemsg = input(str('Message: '))
            key = input(str('Key: '))
            if dore == 'e':
                print('eeeeeee')
                rerun = True
            if dore == 'd':
                print('ddddddd')
                rerun = True
        elif dore == 'q':
            print('Goodbye!')
            run = False
        else:
            print('Did not understand command, try again.')
            rerun = True
    if rerun == True:
        dore = None
        dore = input(str('Enter e to encrypt, d to decrypt, or q to quit: '))
        rerun = False
'''

