from hashlib import sha256

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
    if k == 8:
        bin_data += "00111101"*2
    elif k == 16:
        bin_data += "00111101"
    
    op = ""
    for i in range(0,len(bin_data),6):
        op += enc_di[bin_data[i:i+6]]
    
    return op

def decode_base64(data):
    print('[-] decode....')
    _data = ""
    for i in data:
        _data += dec_di[i]
    op = ""
    for i in range(0,len(_data),8):
        op += chr(int(_data[i:i+8],2))
    return op



header = '{"alg":"HS256","typ":"JWT"}'
payload = '{"token_type":"access","exp":1697620260,"iat":1697584260,"jti":"e7f76280e83f424da3596bd24f53d2ad","user_id":3}'
eh = encode_base64(header)
ep = encode_base64(payload)
signature = sha256((f'{eh}.{ep}').encode('ascii')).hexdigest()
token = f"{eh}.{ep}.{signature}"
print(token)

token_ = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3NjIwNjcxLCJpYXQiOjE2OTc1ODQ2NzEsImp0aSI6IjhmYjQ5MGNmNzk0MzRiMWVhYWVlMTgzNzg2MWE1NjZhIiwidXNlcl9pZCI6Mn0.duclSmI1jB8pA1SNHjBNmi6rUX9GSWVQH24_oTwh0G0'
rt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTEyMDI2MCwiaWF0IjoxNjk3NTg0MjYwLCJqdGkiOiIyMTYxYWY1YzY3NTg0ZDdjOWQ2ZjMyZTEzYmEzNjUwOSIsInVzZXJfaWQiOjJ9.VgASqOmHLnu4Dp9Dqh5TWt2ppocBKSQhYjDUk73Trhs'
print(decode_base64(token_.split('.')[0]))
print(decode_base64(token_.split('.')[1]))