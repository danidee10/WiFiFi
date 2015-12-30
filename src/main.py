import subprocess
import sys
from hotspot import Hotspot

def main():

    #function to check if exit was entered anywhere, exit the program with 0 as the exit status
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
        # capture the username and password from the user
        elif yes == "no":
            name = input("Enter the Name of the New network:\n")
            check_exit(name)
            while True:
                password = input("""Enter the password for the network
hint: password must be at least eight characters: """)
                check_exit(password)
                if len(password) >= 8:
                    hotspot = Hotspot(name, password)
                    hotspot.initialize_hotspot()
                    hotspot.start()
                    break
                else:
                    continue

                    while True:
                        stop = input("type stop to stop the wireless network")
                        stop.lower()
                        if stop == "stop":
                            hotspot.stop()
                            break
                        else:
                            print('invalid option type stop to stop the wireless network')
                            continue

                    input("Press Enter to exit")

        else:
            print("Invalid option please enter Yes or No:\n")
            continue


if __name__ == "__main__": main()