import os
import time


print('Welcome to WiFiFi version 1.0')

name =  input('Enter the name of the network:\n')
password = input('Enter Your password:\n')

cmd="netsh wlan set hostednetwork mode = allow ssid = {} key= {}".format(name, password)

#os.system(cmd)
#os.system('netsh wlan start hostednetwork')

#used time.sleep so the user can read the output before the console closes
time.sleep(8)
