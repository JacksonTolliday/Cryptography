"""
cryptography.py
Author: Jackson Tolliday
Credit: https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associationsn = list(associations)
associationsnu = list(range(len(associationsn)))
letternumzipd = list(zip(associationsnu, associationsn))
ltrnumdictd = dict(letternumzipd)
letternumzipe = list(zip(associationsn, associationsnu))
ltrnumdicte = dict(letternumzipe)

print(ltrnumdicte)

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

def numbs(message): #, key, direction
    message = list(message)
    for c in message:
        for x in ltrnumdict:
            if c in ltrnumdict:
                message.append(letternumzip[x][0])

'                leftover = range(len(message))'
'                del message[0]'

print(numbs('Hello, World!'))

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

