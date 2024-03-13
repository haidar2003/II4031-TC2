def rc4_file(input_file, output_file, key):
    m = 1 # PLACEHOLDER, koprima dengan 256
    b = 1 # PLACEHOLDER, pergeseran

    S = [0 for i in range(256)]
    for i in range(256):
        S[i] = i
        
    j = 0
    for i in range(256):
        p = (j + S[i] + ord(key[i % len(key)])) % 256 # Awalnya j
        j = (m * p + b ) % 256
        S[i], S[j] = S[j], S[i]

    print(S)

    i = j = count = 0
    fin = open(input_file, "rb") 
    fout = open(output_file, "wb")

    p = fin.read(1)

    while p: 
        print(p)
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] 
        t = (S[i] + S[j]) % 256
        u = S[t]  
        print(u)
        print(ord(p))
        c = chr(ord(p) ^ u)  
        print(ord(p) ^ u)
        print(c.encode('latin1'))
        fout.write(c.encode('latin1'))
        p = fin.read(1)




if __name__ == "__main__":
    input_file = 'test.txt'
    output_file = 'output.txt'
    output_file_2 = 'output1.txt'
    key = 'ASDASDASDASDASDASD'
    rc4_file(input_file, output_file, key)
    rc4_file(output_file, output_file_2, key)
                

