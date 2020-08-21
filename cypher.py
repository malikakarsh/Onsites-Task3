#ENTER YOUR MESSAGE IN line 242
#ENTER YOUR PASSWORD IN line 67


s_box = [[99 ,124 ,119 ,123 ,242 ,107 ,111 ,197 ,48 ,1 ,103 ,43 ,254 ,215 ,171 ,118],
            [202 ,130 ,201 ,125 ,250 ,89 ,71 ,240 ,173 ,212 ,162 ,175 ,156 ,164 ,114 ,192],
            [183 ,253 ,147 ,38 ,54 ,63 ,247 ,204 ,52 ,165 ,229 ,241 ,113 ,216 ,49 ,21],
            [4 ,199 ,35 ,195 ,24 ,150 ,5 ,154 ,7 ,18 ,128 ,226 ,235 ,39 ,178 ,117],
            [9 ,131 ,44 ,26 ,27 ,110 ,90 ,160 ,82 ,59 ,214 ,179 ,41 ,227 ,47 ,132],
            [83 ,209 ,0 ,237 ,32 ,252 ,177 ,91 ,106 ,203 ,190 ,57 ,74 ,76 ,88 ,207],
            [208 ,239 ,170 ,251 ,67 ,77 ,51 ,133 ,69 ,249 ,2 ,127 ,80 ,60 ,159 ,168],
            [81 ,163 ,64 ,143 ,146 ,157 ,56 ,245 ,188 ,182 ,218 ,33 ,16 ,255 ,243 ,210],
            [205 ,12 ,19 ,236 ,95 ,151 ,68 ,23 ,196 ,167 ,126 ,61 ,100 ,93 ,25 ,115],
            [96 ,129 ,79 ,220 ,34 ,42 ,144 ,136 ,70 ,238 ,184 ,20 ,222 ,94 ,11 ,219],
            [224 ,50 ,58 ,10 ,73 ,6 ,36 ,92 ,194 ,211 ,172 ,98 ,145 ,149 ,228 ,121],
            [231 ,200 ,55 ,109 ,141 ,213 ,78 ,169 ,108 ,86 ,244 ,234 ,101 ,122 ,174 ,8],
            [186 ,120 ,37 ,46 ,28 ,166 ,180 ,198 ,232 ,221 ,116 ,31 ,75 ,189 ,139 ,138],
            [112 ,62 ,181 ,102 ,72 ,3 ,246 ,14 ,97 ,53 ,87 ,185 ,134 ,193 ,29 ,158],
            [225 ,248 ,152 ,17 ,105 ,217 ,142 ,148 ,155 ,30 ,135 ,233 ,206 ,85 ,40 ,223],
            [140 ,161 ,137 ,13 ,191 ,230 ,66 ,104 ,65 ,153 ,45 ,15 ,176 ,84 ,187 ,22]]

def KeyExpansion(pas):
   
    
    round_const = [1,2,4,8,16,32,64,128,27,54]
    rounds = 0
    #print(s_box[2][0])
    
    words = {}
    words['w0'] = list([int(ord(pas[0])),int(ord(pas[1])),int(ord(pas[2])),int(ord(pas[3]))])  
    words['w1'] = list([int(ord(pas[4])),int(ord(pas[5])),int(ord(pas[6])),int(ord(pas[7]))]) 
    words['w2'] = list([int(ord(pas[8])),int(ord(pas[9])),int(ord(pas[10])),int(ord(pas[11]))])
    words['w3'] = list([int(ord(pas[12])),int(ord(pas[13])),int(ord(pas[14])),int(ord(pas[15]))])  
   

    for i in range(4,44):
        if (i%4 == 0):
            rotword = list([words[f"w{i-1}"][1],words[f"w{i-1}"][2],words[f"w{i-1}"][3],words[f"w{i-1}"][0]])
            sub_bytes = list([s_box[int('0'*(6 - len(format(rotword[0],'b'))) + format(rotword[0],'b')[-1:-5:-1][-1::-1],2)][int('0'*(6 - len(format(rotword[0],'b'))) + format(rotword[0],'b')[-5::-1][-1::-1],2)],
                            s_box[int('0'*(6 - len(format(rotword[1],'b'))) + format(rotword[1],'b')[-1:-5:-1][-1::-1],2)][int('0'*(6 - len(format(rotword[1],'b'))) + format(rotword[1],'b')[-5::-1][-1::-1],2)],
                            s_box[int('0'*(6 - len(format(rotword[2],'b'))) + format(rotword[2],'b')[-1:-5:-1][-1::-1],2)][int('0'*(6 - len(format(rotword[2],'b'))) + format(rotword[2],'b')[-5::-1][-1::-1],2)],
                            s_box[int('0'*(6 - len(format(rotword[3],'b'))) + format(rotword[3],'b')[-1:-5:-1][-1::-1],2)][int('0'*(6 - len(format(rotword[3],'b'))) + format(rotword[3],'b')[-5::-1][-1::-1],2)]])
            
                
            r_con = [round_const[rounds],0,0,0]
            rounds += 1
            z = list([r_con[0]^sub_bytes[0],r_con[1]^sub_bytes[1],r_con[2]^sub_bytes[2],r_con[3]^sub_bytes[3]])
            words[f'w{i}'] = list([(words[f'w{i-1}'][0])^(z[0]),(words[f'w{i-1}'][1])^(z[1]),(words[f'w{i-1}'][2])^(z[2]),(words[f'w{i-1}'][3])^(z[3])])
            

        else:
            words[f'w{i}'] = list([(words[f'w{i-1}'][0])^(words[f'w{i-4}'][0]),(words[f'w{i-1}'][1])^(words[f'w{i-4}'][1]),(words[f'w{i-1}'][2])^(words[f'w{i-4}'][2]),(words[f'w{i-1}'][3])^(words[f'w{i-4}'][3])])
            
  
    return words

def cypher(text):
    input_array = []
    row1 = list([int(ord(text[0])),int(ord(text[1])),int(ord(text[2])),int(ord(text[3]))])  
    row2 = list([int(ord(text[4])),int(ord(text[5])),int(ord(text[6])),int(ord(text[7]))]) 
    row3 = list([int(ord(text[8])),int(ord(text[9])),int(ord(text[10])),int(ord(text[11]))])
    row4 = list([int(ord(text[12])),int(ord(text[13])),int(ord(text[14])),int(ord(text[15]))])  
    input_array.append(row1)
    input_array.append(row2)
    input_array.append(row3)
    input_array.append(row4)
    words=KeyExpansion("helloworld123456") #PASSWORD
    
    
    round_0 = []
    for i in range(4):
        rounded=[]
        for j in range(4):
            fig = input_array[i][j]^words[f'w{i}'][j]
            rounded.append(fig)
        round_0.append(rounded)
        
    
    def Rounds(val): 
        #Substitute-bytes
            
        sub_bytes = list([[s_box[int('0'*(15 - len(format(int(val[0][0]),'b'))) + str(abs(int(format(int(val[0][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][0]),'b'))) + str(abs(int(format(int(val[0][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[0][1]),'b'))) + str(abs(int(format(int(val[0][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][1]),'b'))) + str(abs(int(format(int(val[0][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[0][2]),'b'))) + str(abs(int(format(int(val[0][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][2]),'b'))) + str(abs(int(format(int(val[0][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[0][3]),'b'))) + str(abs(int(format(int(val[0][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][3]),'b'))) + str(abs(int(format(int(val[0][3]),'b'))))[-5::-1][-1::-1],2)]],
                             [s_box[int('0'*(15 - len(format(int(val[1][0]),'b'))) + str(abs(int(format(int(val[1][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][0]),'b'))) + str(abs(int(format(int(val[1][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[1][1]),'b'))) + str(abs(int(format(int(val[1][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][1]),'b'))) + str(abs(int(format(int(val[1][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[1][2]),'b'))) + str(abs(int(format(int(val[1][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][2]),'b'))) + str(abs(int(format(int(val[1][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[1][3]),'b'))) + str(abs(int(format(int(val[1][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][3]),'b'))) + str(abs(int(format(int(val[1][3]),'b'))))[-5::-1][-1::-1],2)]],
                             [s_box[int('0'*(15 - len(format(int(val[2][0]),'b'))) + str(abs(int(format(int(val[2][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][0]),'b'))) + str(abs(int(format(int(val[2][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[2][1]),'b'))) + str(abs(int(format(int(val[2][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][1]),'b'))) + str(abs(int(format(int(val[2][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[2][2]),'b'))) + str(abs(int(format(int(val[2][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][2]),'b'))) + str(abs(int(format(int(val[2][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[2][3]),'b'))) + str(abs(int(format(int(val[2][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][3]),'b'))) + str(abs(int(format(int(val[2][3]),'b'))))[-5::-1][-1::-1],2)]],
                             [s_box[int('0'*(15 - len(format(int(val[3][0]),'b'))) + str(abs(int(format(int(val[3][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][0]),'b'))) + str(abs(int(format(int(val[3][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[3][1]),'b'))) + str(abs(int(format(int(val[3][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][1]),'b'))) + str(abs(int(format(int(val[3][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[3][2]),'b'))) + str(abs(int(format(int(val[3][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][2]),'b'))) + str(abs(int(format(int(val[3][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[3][3]),'b'))) + str(abs(int(format(int(val[3][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][3]),'b'))) + str(abs(int(format(int(val[3][3]),'b'))))[-5::-1][-1::-1],2)]]])
        
        
        
        # Shift-rows
        
        shift_rows = list([[sub_bytes[0][0],sub_bytes[1][1],sub_bytes[2][2],sub_bytes[3][3]],
                            [sub_bytes[0][1],sub_bytes[1][2],sub_bytes[2][3],sub_bytes[3][0]],
                            [sub_bytes[0][2],sub_bytes[1][3],sub_bytes[2][0],sub_bytes[3][1]],
                            [sub_bytes[0][3],sub_bytes[1][0],sub_bytes[2][1],sub_bytes[3][2]]])
            
        
        
        arr1,arr2,arr3,arr4 = [],[],[],[]
        for i in range(4):
            arr1.append(shift_rows[0][i])
        for i in range(4):
            arr2.append(shift_rows[1][i])
        for i in range(4):
            arr3.append(shift_rows[2][i])
        for i in range(4):
            arr4.append(shift_rows[3][i])
            
        
        
        # Mix_Columns
        mix_col = []
        
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
        
        def mixColumn(row):
            temp = row.copy()
            row[0] = Mult(temp[0],2) ^ Mult(temp[3],1) ^ \
                        Mult(temp[2],1) ^ Mult(temp[1],3)
            row[1] = Mult(temp[1],2) ^ Mult(temp[0],1) ^ \
                        Mult(temp[3],1) ^ Mult(temp[2],3)
            row[2] = Mult(temp[2],2) ^ Mult(temp[1],1) ^ \
                        Mult(temp[0],1) ^ Mult(temp[3],3)
            row[3] = Mult(temp[3],2) ^ Mult(temp[2],1) ^ \
                        Mult(temp[1],1) ^ Mult(temp[0],3)
            col = []
            col.append(row[0])
            col.append(row[1])
            col.append(row[2])
            col.append(row[3])
            
            
            return col
        
        col1 = mixColumn(arr1)
        col2 = mixColumn(arr2)
        col3 = mixColumn(arr3)
        col4 = mixColumn(arr4)
        
        
        mix_col.append(col1)
        mix_col.append(col2)
        mix_col.append(col3)
        mix_col.append(col4)
            
            
        #print(mix_col)
        return mix_col
    
        
        
    #COMPLEtiNG ROUND1-9

    k = 4
    value = round_0
    while (k<40):
        value = Rounds(value)
        round_sub = []
        for i in range(4):
            rounded=[]
            for j in range(4):
                fig = input_array[i][j]^words[f'w{k}'][j]
                rounded.append(fig)
            k +=1
            round_sub.append(rounded)
        value = round_sub
    
        
        
        
        
    
        
        
        
 
    
        
    
    #Round-10
    val = value

    
    sub_bytes = list([[s_box[int('0'*(15 - len(format(int(val[0][0]),'b'))) + str(abs(int(format(int(val[0][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][0]),'b'))) + str(abs(int(format(int(val[0][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[0][1]),'b'))) + str(abs(int(format(int(val[0][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][1]),'b'))) + str(abs(int(format(int(val[0][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[0][2]),'b'))) + str(abs(int(format(int(val[0][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][2]),'b'))) + str(abs(int(format(int(val[0][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[0][3]),'b'))) + str(abs(int(format(int(val[0][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[0][3]),'b'))) + str(abs(int(format(int(val[0][3]),'b'))))[-5::-1][-1::-1],2)]],
                             [s_box[int('0'*(15 - len(format(int(val[1][0]),'b'))) + str(abs(int(format(int(val[1][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][0]),'b'))) + str(abs(int(format(int(val[1][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[1][1]),'b'))) + str(abs(int(format(int(val[1][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][1]),'b'))) + str(abs(int(format(int(val[1][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[1][2]),'b'))) + str(abs(int(format(int(val[1][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][2]),'b'))) + str(abs(int(format(int(val[1][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[1][3]),'b'))) + str(abs(int(format(int(val[1][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[1][3]),'b'))) + str(abs(int(format(int(val[1][3]),'b'))))[-5::-1][-1::-1],2)]],
                             [s_box[int('0'*(15 - len(format(int(val[2][0]),'b'))) + str(abs(int(format(int(val[2][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][0]),'b'))) + str(abs(int(format(int(val[2][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[2][1]),'b'))) + str(abs(int(format(int(val[2][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][1]),'b'))) + str(abs(int(format(int(val[2][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[2][2]),'b'))) + str(abs(int(format(int(val[2][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][2]),'b'))) + str(abs(int(format(int(val[2][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[2][3]),'b'))) + str(abs(int(format(int(val[2][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[2][3]),'b'))) + str(abs(int(format(int(val[2][3]),'b'))))[-5::-1][-1::-1],2)]],
                             [s_box[int('0'*(15 - len(format(int(val[3][0]),'b'))) + str(abs(int(format(int(val[3][0]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][0]),'b'))) + str(abs(int(format(int(val[3][0]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[3][1]),'b'))) + str(abs(int(format(int(val[3][1]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][1]),'b'))) + str(abs(int(format(int(val[3][1]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[3][2]),'b'))) + str(abs(int(format(int(val[3][2]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][2]),'b'))) + str(abs(int(format(int(val[3][2]),'b'))))[-5::-1][-1::-1],2)],
                            s_box[int('0'*(15 - len(format(int(val[3][3]),'b'))) + str(abs(int(format(int(val[3][3]),'b'))))[-1:-5:-1][-1::-1],2)][int('0'*(15 - len(format(int(val[3][3]),'b'))) + str(abs(int(format(int(val[3][3]),'b'))))[-5::-1][-1::-1],2)]]])
    
    shift_rows = list([[sub_bytes[0][0],sub_bytes[1][1],sub_bytes[2][2],sub_bytes[3][3]],
                            [sub_bytes[0][1],sub_bytes[1][2],sub_bytes[2][3],sub_bytes[3][0]],
                            [sub_bytes[0][2],sub_bytes[1][3],sub_bytes[2][0],sub_bytes[3][1]],
                            [sub_bytes[0][3],sub_bytes[1][0],sub_bytes[2][1],sub_bytes[3][2]]])
    
    
    round_10 = []
    for i in range(4):
        rounded=[]
        for j in range(4):
            fig = shift_rows[i][j]^words[f'w{i}'][j]
            rounded.append(fig)
        round_10.append(rounded)
        
    print("Cyphered text: ",round_10)
    
    


cypher("ABCDPQRSXYZWMNOP") #MESSAGE











