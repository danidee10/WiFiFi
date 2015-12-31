import subprocess
import sys
from hotspot import Hotspot

def main():

    # method to check if exit was entered anywhere, exit the program with 0 as the exit status
    def check_exit(input_to_check):
        if input_to_check == "exit":
            sys.exit(0)

    print('Welcome to WiFiFi a small windows hotspot application, Type exit to close the program at anytime')

    # ask for existing profile and create a new one if none exists
    while True:
        yes = input('Do you have an existing profile?, Enter Yes to proceed or No to create a new one\n')
        yes.lower()

        check_exit(yes)

        if yes == "yes":
            hotspot = Hotspot()
            hotspot.start()
            break
        # capture the username and password from the user
        elif yes == "no":
            name = input("Enter the Name of the New network:\n")
            password = ""
            check_exit(name)
            while len(password) < 8:
                password = input("""Enter the password for the network
hint: password must be at least eight characters: """)
            hotspot = Hotspot(name, password)
            hotspot.initialize_hotspot()
            hotspot.start()
            break
        else:
            print("Invalid option please enter Yes or No:\n")
            continue


    # prompt the user to end the active hotspot session
    while True:
        stop = input("type stop to stop the wireless network:\n")
        stop.lower()
        if stop == "stop":
            hotspot.stop()
            # should modify the check_exit function to accept an optional argument instead of using sys
            sys.exit(0)
        else:
            print('invalid option type stop to stop the wireless network:\n')
            continue



if __name__ == "__main__": main()
