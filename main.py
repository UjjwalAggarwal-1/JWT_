from hashlib import sha256
from hmac import new as hmac_new
import base64

enc_di = {
        "000000": "A",	
        "000001": "B",
        "000010": "C",	
        "000011": "D",	
        "000100": "E",	
        "000101": "F",	
        "000110": "G",	
        "000111": "H",	
        "001000": "I",	
        "001001": "J",	
        "001010": "K",	
        "001011": "L",	
        "001100": "M",	
        "001101": "N",	
        "001110": "O",	
        "001111": "P",	
        "010000": "Q",
        "010001": "R",
        "010010": "S",
        "010011": "T",
        "010100": "U",
        "010101": "V",
        "010110": "W",
        "010111": "X",
        "011000": "Y",
        "011001": "Z",
        "011010": "a",
        "011011": "b",
        "011100": "c",
        "011101": "d",
        "011110": "e",
        "011111": "f",
        "100000": "g",
        "100001": "h",
        "100010": "i",
        "100011": "j",
        "100100": "k",
        "100101": "l",
        "100110": "m",
        "100111": "n",
        "101000": "o",
        "101001": "p",
        "101010": "q",
        "101011": "r",
        "101100": "s",
        "101101": "t",
        "101110": "u",
        "101111": "v",
        "110000": "w",
        "110001": "x",
        "110010": "y",
        "110011": "z",
        "110100": "0",
        "110101": "1",
        "110110": "2",
        "110111": "3",
        "111000": "4",
        "111001": "5",
        "111010": "6",
        "111011": "7",
        "111100": "8",
        "111101": "9",
        "111110": "+",
        "111111": "/",
    }

dec_di = {v: k for k, v in enc_di.items()}

def encode_base64(data):
    print('[-] encode....')
    bin_data = ''.join(format(format(ord(x), 'b'),"0>8") for x in data)
    
    k = (len(bin_data)%24)
    if k == 16:
        bin_data += "00"
    elif k == 8:
        bin_data += "0000"
    
    op = ""
    for i in range(0,len(bin_data),6):
        op += enc_di[bin_data[i:i+6]]
    
    ## padding
    # if k == 16:
    #     op += "="
    # elif k == 8:
    #     op += "=="
    
    return op

def decode_base64(data):
    print('[-] decode....')
    
    ## padding
    # if data[-2:] == "==":
    #     data = data[:-2]
    # elif data[-1] == "=":
    #     data = data[:-1]
    
    _data = "".join(dec_di[i] for i in data)

    op = ""
    for i in range(0,len(_data)-len(_data)%8,8):
        op += chr(int(_data[i:i+8],2))
    
    return op


# print(encode_base64("light work."), decode_base64(encode_base64("light work.")))
# print(encode_base64("light work"), decode_base64(encode_base64("light work")))
# print(encode_base64("light wor"), decode_base64(encode_base64("light wor")))
# print(encode_base64("light wo"), decode_base64(encode_base64("light wo")))
# print(encode_base64("light w"), decode_base64(encode_base64("light w")))
# print(encode_base64("Ma"), decode_base64(encode_base64("Ma")))


def print_comp(a,b):
    print(a)
    print(b)

    for i in range(len(a)):
        if a[i] != b[i]:
            break
        else:
            print(f"\033[92m{a[i]}\033[0m",end="")
    
    print()


header = '{"alg":"HS256","typ":"JWT"}'
payload = '{"sub":"1234567890","name":"John Doe","iat":1516239022}'
eh = encode_base64(header)
ep = encode_base64(payload)

key = b''
signature = (hmac_new(key, f"{eh}.{ep}".encode('ascii'), sha256).digest())
signature = base64.b64encode(signature).decode('ascii')
if signature[-1] == "=":
    signature = signature[:-1]
if signature[-1] == "=":
    signature = signature[:-1]
signature = signature.replace("/", "_")
token = f"{eh}.{ep}.{signature}"
comp = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.he0ErCNloe4J7Id0Ry2SEDg09lKkZkfsRiGsdX_vgEg"
print_comp(token, comp)

print(decode_base64(token.split('.')[1]))
print(decode_base64(comp.split('.')[1]))
