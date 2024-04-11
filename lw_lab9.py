#Linwei Zhang
from agt_decode import decode

def encode(password):
    encoded_password = ""
    for each_number in password:
        encoded_password += (str(int(each_number)+3))
    return encoded_password



def main():
    while True:
        print("""Menu:
        -------------
        1. Encode
        2. Decode
        3. Quit""")

        option = int(input("Please enter an option: "))

        if option == 1:
            my_password = input("Please enter your password to encode: ")
            encoded_password = encode(my_password)
            print("Your password has been encoded and stored!")
            continue

        if option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        if option == 3:
            break


if __name__ == "__main__":
    main()


