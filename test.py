import random
        
def isCoPrime(num1, num2):
    smallest = min(num1, num2)
    for i in range(1, smallest + 1):
        if (num1 % i == 0 and num2 % i == 0):
            gcd = i
    return gcd == 1

def keyGen(seed):
    random.seed(seed)
    return random.randint(1, 1000000) 

def rc4_file(input_file, output_file, key):
    m = keyGen(key)
    b = keyGen(m)

    while not(isCoPrime(m, 26)):
        m += 1

    S = [0 for i in range(256)]
    for i in range(256):
        S[i] = i
        
    j = 0
    for i in range(256):
        p = (j + S[i] + ord(key[i % len(key)])) % 256 
        j = ((m * p) + b ) % 256
        S[i], S[j] = S[j], S[i]

    i = j = count = 0
    fin = open(input_file, "rb") 
    fout = open(output_file, "wb")

    p = fin.read(1)

    while p: 
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] 
        t = (S[i] + S[j]) % 256
        u = S[t]  
        c = chr(ord(p) ^ u)  
        fout.write(c.encode('latin1'))
        p = fin.read(1)


def rc4_text_encrypt(input_text, key):
    m = keyGen(key)
    b = keyGen(m)

    while not(isCoPrime(m, 26)):
        m += 1

    S = [0 for i in range(256)]
    for i in range(256):
        S[i] = i
        
    j = 0
    for i in range(256):
        p = (j + S[i] + ord(key[i % len(key)])) % 256 
        j = ((m * p) + b ) % 256
        S[i], S[j] = S[j], S[i]

    i = j =  0

    output_text = b''

    for count in range (len(input_text)):
        p = input_text[count]
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] 
        t = (S[i] + S[j]) % 256
        u = S[t]  
        c = chr(ord(p) ^ u)  
        output_text += (c.encode('latin1'))

    return output_text.decode('latin1')


if __name__ == "__main__":
    input_file = 'test.txt'
    output_file = 'output.txt'
    output_file_2 = 'output1.txt'
    key = 'ASDASDASDASDASDASD'
    rc4_file(input_file, output_file, key)
    rc4_file(output_file, output_file_2, key)
    ciphertext = rc4_text_encrypt('Haidar Rubah', 'ASDFG')
    print(ciphertext)
    print(rc4_text_encrypt(ciphertext, 'ASDFG'))