"""
cryptography.py
Author: Jackson Tolliday
Credit: https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters, https://stackoverflow.com/questions/31175223/append-a-tuple-to-a-list-whats-the-difference-between-two-ways, https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string, https://stackoverflow.com/questions/4918425/subtract-a-value-from-every-number-in-a-list-in-python

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associationsn = list(associations)
somemore = associationsn*2
associationsnu = list(range(len(associationsn)))
whynot = list(range(len(somemore)))
letternumzip = list(zip(associationsn, associationsnu))
numletterzip = list(zip(whynot, somemore))
ltrnumdict = dict(letternumzip)
numltrdict = dict(numletterzip)
subractfornumltrdict = associationsnu
subractfornumltrdict[:] = [x - len(associationsnu) for x in subractfornumltrdict]
print(subractfornumltrdict)

def encdecrypt(message, key, direction):
    a = 0
    c = 0
    d = 0
    message = list(message)
    key = list(key)
    tkey = int(len(message)/ len(key))
    thkey = key*tkey
    for c in range(len(message)):
        message[c] = ltrnumdict[message[c]]
        thkey[c] = ltrnumdict[thkey[c]]
    zipmsgkey = list(zip(message, thkey))
    fullnumlist = []
    for a in zipmsgkey:
        if direction == 1:
            b = a[0] + a[1]
            fullnumlist.append(b)
        if direction == -1:
            b = a[0] - a[1]
            fullnumlist.append(b)
    completion = []
    for d in range(len(fullnumlist)):
        completion.append(numltrdict[fullnumlist[d]])
    done = ''.join(completion)
    print(done)

'''
dore = input(str('Enter e to encrypt, d to decrypt, or q to quit: '))
run = True
rerun = False
while run == True:
    if rerun == False:
        if dore == 'e' or dore == 'd':
            basemsg = input(str('Message: '))
            kee = input(str('Key: '))
            if dore == 'e':
                encdecrypt(basemsg, kee, 1)
                rerun = True
            if dore == 'd':
                encdecrypt(basemsg, kee, -1)
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

