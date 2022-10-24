def encrypt(pwd,offset):
    new_pwd=''
    for char in pwd:
        if char==' ':
            new_pwd=new_pwd+char
        elif char.islower():
            new_pwd = new_pwd + chr(97+((ord(char)-97+offset)%26))
        else:
            new_pwd = new_pwd + chr(65+((ord(char)-65+offset)%26))
    return new_pwd

def decrypt(word,offset):
    txt=""
    for char in word:
        if char==' ':
            txt=txt+char
        elif char.islower():
            txt  =txt + chr(97+((ord(char)-97-offset)%26))
        else:
            txt= txt + chr(65+((ord(char)-65-offset)%26))
    return txt
        
        
pwd = input("enter string:")
offset = int(input("enter offset:"))
print("encrypted string:",encrypt(pwd,offset))
word=input("enter the encrypted word:")
print("decrypted string:",decrypt(word,offset))
