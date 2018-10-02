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
letternumzip = list(zip(associationsnu, associationsn))
print(letternumzip)

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


