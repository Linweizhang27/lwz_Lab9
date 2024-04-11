def decode(input):
    decoded_password = ''
    for char in input:
        decoded_password += str(int(char) - 3)
    return decoded_password