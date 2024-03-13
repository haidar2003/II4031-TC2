import random

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getOrder(alphabet):
    for i in range(len(lowerCase)):
        if alphabet.lower() == lowerCase[i]:
            return i
        
def isCoPrime(num1, num2):
    smallest = min(num1, num2)
    for i in range(1, smallest + 1):
        if (num1 % i == 0 and num2 % i == 0):
            gcd = i
    return gcd == 1

def keyGen(seed):
    random.seed(seed)
    return random.randint(1, 1000000) 

def affine_encrypt(plaintext, key):
    cyphertext = ''

    m = keyGen(key)
    b = keyGen(m)

    while not(isCoPrime(m, 26)):
        m += 1
    
    for i in range(len(plaintext)):
        if (plaintext[i].isalpha()):
            encryptedChar = ((m * getOrder(plaintext[i])) + b) % 26

            if plaintext[i].islower():
                cyphertext += lowerCase[encryptedChar]
            else:
                cyphertext += upperCase[encryptedChar]

        # else:
        #     cyphertext += plaintext[i]

    return cyphertext

def affine_decrypt(cyphertext, key):
    plaintext = ''

    m = keyGen(key)
    b = keyGen(m)

    while not(isCoPrime(m, 26)):
        m += 1

    inverse_m = 0

    while (m * inverse_m) % 26 != 1:
        inverse_m += 1
    
    for i in range(len(cyphertext)):
        if (cyphertext[i].isalpha()):
            encryptedChar = (inverse_m * (getOrder(cyphertext[i]) - b)) % 26

            if cyphertext[i].islower():
                plaintext += lowerCase[encryptedChar]
            else:
                plaintext += upperCase[encryptedChar]

        # else:
        #     plaintext += cyphertext[i]

    return plaintext


def main():
    plaintext = str(input("Plaintext: "))
    key = str(input("Key: "))
    cyphertext = affine_encrypt(plaintext, key)
    decryption = affine_decrypt(cyphertext, key)

    print(f'\nEncryption: {cyphertext}\nDecryption: {decryption}')

if __name__ == '__main__':
    main()