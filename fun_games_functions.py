ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def shift_letter(letter, n):
    index = ALPHABET.find(letter)
    shifting =(index + n)%26
    lett = ALPHABET[shifting] 
    return lett
    
def encode(message, n):
    code =""
    for char in message:
        if char in ALPHABET:
         code+=shift_letter(char,n)
        else:
            code+=char
    return code

def decode(message, n):
    return encode( message , -n )
def crack(message):
     n=1
     while n<=25:
        decode(message,n)
        print(f"Shift {n}: {decode(message,n)}")
        n+=1
def main():
    print("Welcome to the Code Machine!")
    message =input("Enter a message: ")
    no = int(input ("enter the no shifts :"))
    encode_message =encode(message,no)
    print("enocoded message :",encode_message)
if __name__ == "__main__":
    main()

#FUN GAME