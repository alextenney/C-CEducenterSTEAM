
# Encrypts the given string using a Caesar cipher and returns the result.
def encrypt(message):
    pass
# Decrypts a string that was previously encrypted using a Caesar cipher and returns the result.
def decrypt(message):
    pass

# main program
method = input("Type 'E' if you would like to encode a message, 'D' if you would like to decode a message.")

if (method == 'E'):
	# wants to encrypt
    msg = input("Your message to encode? ")
    shift = input("How much would you like to shift the message?")
    secret = encrypt(msg)
    print("The encoded message is:", secret)
elif (method == 'D'):
    #wants to decrypt
    secret = input("Your message to decode?")
    shift = input("How much was your message shifted?")
    msg = decrypt(secret)
    print("The decoded message is:", msg)
