sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

PASSWORD = input("Set a password(16-characters): ")
iv = [96,116,97,112,45,47,89,23,46,86,75,46,68,56,74,93]

def KeyExpansion(pas):
    round_const = [1,2,4,8,16,32,64,128,27,54]
    rounds = 0
    
    words={}
    words['w0'] = [ord(pas[0]),ord(pas[1]),ord(pas[2]),ord(pas[3])]
    words['w1'] = [ord(pas[4]),ord(pas[5]),ord(pas[6]),ord(pas[7])]
    words['w2'] = [ord(pas[8]),ord(pas[9]),ord(pas[10]),ord(pas[11])]
    words['w3'] = [ord(pas[12]),ord(pas[13]),ord(pas[14]),ord(pas[15])]
    
    for i in range(4,44):
        if (i%4 == 0):
            rotword = [words[f'w{i-1}'][1],words[f'w{i-1}'][2],words[f'w{i-1}'][3],words[f'w{i-1}'][0]]
            sub_bytes = [sbox[rotword[0]],sbox[rotword[1]],sbox[rotword[2]],sbox[rotword[3]]]
            r_con = [round_const[rounds],0,0,0]
            z = [sub_bytes[0]^r_con[0],sub_bytes[1]^r_con[1],sub_bytes[2]^r_con[2],sub_bytes[3]^r_con[3]]
            words[f'w{i}'] = [words[f'w{i-1}'][0]^z[0],words[f'w{i-1}'][1]^z[1],words[f'w{i-1}'][2]^z[2],words[f'w{i-1}'][3]^z[3]]
        else:
            words[f'w{i}'] = [words[f'w{i-1}'][0]^words[f'w{i-4}'][0],words[f'w{i-1}'][1]^words[f'w{i-4}'][1],words[f'w{i-1}'][2]^words[f'w{i-4}'][2],words[f'w{i-1}'][3]^words[f'w{i-4}'][3]]
            
    return words

def cypher(text):
    global PASSWORD
    input_array = [text[0],text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[10],text[11],text[12],text[13],text[14],text[15]]
    
    words = KeyExpansion(PASSWORD)
    #print(input_array)
    
    round_0 = []
    k=0
    j=0
    for i in range(16):
        if (i==4 or i==8 or i==12):
            k += 1
            j = 0
        round_0.append(input_array[i]^words[f'w{k}'][j])
        j += 1
         
    def Round(val):
        
        #SUB_BYTE
        
        sub_bytes = [sbox[val[0]],sbox[val[1]],sbox[val[2]],sbox[val[3]],sbox[val[4]],sbox[val[5]],sbox[val[6]],sbox[val[7]],sbox[val[8]],sbox[val[9]],sbox[val[10]],sbox[val[11]],sbox[val[12]],sbox[val[13]],sbox[val[14]],sbox[val[15]]]
        
        #SHIFT_ROWS
        
        shift_rows = [sub_bytes[0],sub_bytes[1],sub_bytes[2],sub_bytes[3],sub_bytes[5],sub_bytes[6],sub_bytes[7],sub_bytes[4],sub_bytes[10],sub_bytes[11],sub_bytes[8],sub_bytes[9],sub_bytes[15],sub_bytes[12],sub_bytes[13],sub_bytes[14]]
        
        #MIX_COLUMNS
        
        arr1,arr2,arr3,arr4 = [],[],[],[]
        for i in range(4):
            arr1.append(shift_rows[i])
        for i in range(4,8):
            arr2.append(shift_rows[i])
        for i in range(8,12):
            arr3.append(shift_rows[i])
        for i in range(12,16):
            arr4.append(shift_rows[i])
        
        def Mult(a, b):
            p = 0
            hiBitSet = 0
            for i in range(8):
                if b & 1 == 1:
                    p ^= a
                hiBitSet = a & 0x80
                a <<= 1
                if hiBitSet == 0x80:
                    a ^= 0x1b
                b >>= 1
            return p % 256

        def mixColumn(column):
            temp = column.copy()
            column[0] = Mult(temp[0],2) ^ Mult(temp[3],1) ^ \
                        Mult(temp[2],1) ^ Mult(temp[1],3)
            column[1] = Mult(temp[1],2) ^ Mult(temp[0],1) ^ \
                        Mult(temp[3],1) ^ Mult(temp[2],3)
            column[2] = Mult(temp[2],2) ^ Mult(temp[1],1) ^ \
                        Mult(temp[0],1) ^ Mult(temp[3],3)
            column[3] = Mult(temp[3],2) ^ Mult(temp[2],1) ^ \
                        Mult(temp[1],1) ^ Mult(temp[0],3)

            return column[0],column[1],column[2],column[3]
        
        r1,r2,r3,r4 = mixColumn(arr1)
        r5,r6,r7,r8 = mixColumn(arr2)
        r9,r10,r11,r12 = mixColumn(arr3)
        r13,r14,r15,r16 = mixColumn(arr4)
        
        mix_col = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16]
        
        return mix_col
    
    #ROUND 1-9
    value = round_0
    
    k=4
    j=0
    for i in range(1,10):
        value = Round(value)
        round_sub = []
        for l in range(16):
            if (l==4 or l==8 or l==12):
                k += 1
                j = 0
            round_sub.append(value[l]^words[f'w{k}'][j])  
            j += 1
        k += 1
        j=0
            
        value = round_sub
      
    # ROUND 10
    val = value
    
    sub_bytes = [sbox[val[0]],sbox[val[1]],sbox[val[2]],sbox[val[3]],sbox[val[4]],sbox[val[5]],sbox[val[6]],sbox[val[7]],sbox[val[8]],sbox[val[9]],sbox[val[10]],sbox[val[11]],sbox[val[12]],sbox[val[13]],sbox[val[14]],sbox[val[15]]]
      
    shift_rows = [sub_bytes[0],sub_bytes[1],sub_bytes[2],sub_bytes[3],sub_bytes[5],sub_bytes[6],sub_bytes[7],sub_bytes[4],sub_bytes[10],sub_bytes[11],sub_bytes[8],sub_bytes[9],sub_bytes[15],sub_bytes[12],sub_bytes[13],sub_bytes[14]]
        
    round_10 = []
    k=40
    j=0
    for i in range(16):
        if (i==4 or i==8 or i==12):
            k += 1
            j = 0
        round_10.append(shift_rows[i]^words[f'w{k}'][j])
        j += 1
    
    hexa = ''
    for i in round_10:
        hexa += str(hex(i)) + ' '
    
    return hexa
        
text = input("Enter the text message(16 characters): ")
initial_array = [ord(text[0]),ord(text[1]),ord(text[2]),ord(text[3]),ord(text[4]),ord(text[5]),ord(text[6]),ord(text[7]),ord(text[8]),ord(text[9]),ord(text[10]),ord(text[11]),ord(text[12]),ord(text[13]),ord(text[14]),ord(text[15])]

result = []
for i in range(16):
    result.append(iv[i]^initial_array[i])
final = cypher(result)

print("Cyphered text: ",final)
