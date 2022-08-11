import math
#this function takes the xor of two bit-strings, meaning in each binary position it outputs 1 if the values are different and 0 if the values are the same
def xor(b, c):
    bit1=str(b)
    bit2=str(c)
    if len(bit1) == len(bit2):
        x = ''        
        for i in range(len(bit1)):
            if bit1[i] == bit2[i]:
                xnew = x + '0'
                x=xnew
            else:
                xnew = x+'1'
                x=xnew
        return str(x)
    else:
        print('Strings not the same length')

#this is the definition of the S-box, transforming a bit string of length 6 into one of length 4 in a non-linear way
#S-boxes are public knowledge in DES
def box(b):
    bit=str(b)
    if len(bit)==6:
        k=int(bit[1:5],2)
        if bit[0]=='0' and bit[5]=='0':
            if k==0:
                return '0010'
            elif k==1:
                return '1100'
            elif k==2:
                return '0100'
            elif k==3:
                return '0001'
            elif k==4:
                return '0111'
            elif k==5:
                return '1010'
            elif k==6:
                return '1011'
            elif k==7:
                return '0110'
            elif k==8:
                return '1000'
            elif k==9:
                return '0101'
            elif k==10:
                return '0011'
            elif k==11:
                return '1111'
            elif k==12:
                return '1101'
            elif k==13:
                return '0000'
            elif k==14:
                return '1110'
            elif k==15:
                return '1001'
            else:
                print('Error on S-box')
        elif bit[0]=='0' and bit[5]=='1':
            if k==0:
                return '1110'
            elif k==1:
                return '1011'
            elif k==2:
                return '0010'
            elif k==3:
                return '1100'
            elif k==4:
                return '0100'
            elif k==5:
                return '0111'
            elif k==6:
                return '1101'
            elif k==7:
                return '0001'
            elif k==8:
                return '0101'
            elif k==9:
                return '0000'
            elif k==10:
                return '1111'
            elif k==11:
                return '1010'
            elif k==12:
                return '0011'
            elif k==13:
                return '1001'
            elif k==14:
                return '1000'
            elif k==15:
                return '0110'
            else:
                print('Error on S-box')
        elif bit[0]=='1' and bit[5]=='0':
            if k==0:
                return '0100'
            elif k==1:
                return '0010'
            elif k==2:
                return '0001'
            elif k==3:
                return '1011'
            elif k==4:
                return '1010'
            elif k==5:
                return '1101'
            elif k==6:
                return '0111'
            elif k==7:
                return '1000'
            elif k==8:
                return '1111'
            elif k==9:
                return '1001'
            elif k==10:
                return '1100'
            elif k==11:
                return '0101'
            elif k==12:
                return '0110'
            elif k==13:
                return '0011'
            elif k==14:
                return '0000'
            elif k==15:
                return '1110'
            else:
                print('Error on S-box')
        elif bit[0]=='1' and bit[5]=='1':
            if k==0:
                return '1011'
            elif k==1:
                return '1000'
            elif k==2:
                return '1100'
            elif k==3:
                return '0111'
            elif k==4:
                return '0001'
            elif k==5:
                return '1110'
            elif k==6:
                return '0010'
            elif k==7:
                return '1101'
            elif k==8:
                return '0110'
            elif k==9:
                return '1111'
            elif k==10:
                return '0000'
            elif k==11:
                return '1001'
            elif k==12:
                return '1010'
            elif k==13:
                return '0100'
            elif k==14:
                return '0101'
            elif k==15:
                return '0011'
            else:
                print('Error on S-box')         
        else:
            print('Input was not a bit string')
    else:
        print('Input must be a 6-bit string')
        
#DES has the same encryption/decryption procedure (just reversing the set of private keys)        
setting=input('Please choose encrypt or decrypt: ')
#encyrption procedure
if setting == 'encrypt':
    m=input('Input a string of 8 bits string to encrypt: ')
    #keys are here, these are private and can be changed. We do a 3-round DES here, since this would be feasible for a student to do by hand. In the future, we can program a larger key, subkey generation procedure to obviate the need for this and allow for a full 16-round Feistel cipher 
    k0='110100'
    k1='010011'
    k2='001110'
    if len(m) < 8:
        print('You need to enter 8 bits.')
    elif len(m)>8:
        print('That is too long of a message.')
    else:
        for i in range(7):
            if m[i]!='0' and m[i]!='1':
                print('Each bit must be a 0 or a 1. Try again')
                break
        for j in range(3):
            if j==0:
                key = k0
            elif j==1:
                key=k1
            elif j==2:
                key=k2        
            L=m[:4]
            R=m[4:]
            print('L={0}'.format(L))
            print('R={0}'.format(R))
            print('k{0}={1}'.format(j,key))
            S=R+R[1]+R[3]
            print('S={0}'.format(S))
            T=xor(S,key)
            print('T={0}'.format(T))
            U=box(T)
            print('U={0}'.format(U))
            Rnew=xor(L,U)
            L=R
            R=Rnew
            m=L+R
        c=R+L
        print(c)
        
#decryption algorithm        
if setting == 'decrypt':
    m=input('Input a string of 8 bits string to decrypt: ')
    #this key schedule is reverse to the encyrption key schedule
    k0='110100'
    k1='010011'
    k2='001110'
    if len(m) < 8:
        print('You need to enter 8 bits.')
    elif len(m)>8:
        print('That is too long of a message.')
    else:
        for i in range(7):
            if m[i]!='0' and m[i]!='1':
                print('Each bit must be a 0 or a 1. Try again')
                break
        for j in range(3):
            if j==0:
                key = k2
            elif j==1:
                key=k1
            elif j==2:
                key=k0        
            L=m[:4]
            R=m[4:]
            print('L={0}'.format(L))
            print('R={0}'.format(R))
            print('k{0}={1}'.format(j,key))
            S=R+R[1]+R[3]
            print('S={0}'.format(S))
            T=xor(S,key)
            print('T={0}'.format(T))
            U=box(T)
            print('U={0}'.format(U))
            Rnew=xor(L,U)
            L=R
            R=Rnew
            m=L+R
        c=R+L
        print(c)
