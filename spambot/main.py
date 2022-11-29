# ________  ___      ________      ___    ___ ________  ________     
#|\   ____\|\  \    |\_____  \    |\  \  /  /|\_____  \|\   __  \    
#\ \  \___|\ \  \   \|____|\ /_   \ \  \/  / ||____|\ /\ \  \|\  \   
# \ \_____  \ \  \        \|\  \   \ \    / /      \|\  \ \   _  _\  
#  \|____|\  \ \  \____  __\_\  \   \/  /  /      __\_\  \ \  \\  \| 
#    ____\_\  \ \_______\\_______\__/  / /       |\_______\ \__\\ _\ 
#   |\_________\|_______\|_______|\___/ /        \|_______|\|__|\|__|
#   \|_________|                 \|___|/                             
                                                                    

from keyboard import press
from time import sleep
import pyautogui, os

def end(): #Exit function with a message
    print('\nTool By\n5l3y3r')
    exit(0)

def main(): #main function
    os.system('cls')
    print('''
 _________                   __________        __    __________          .________.__  ________        ________        
 /   _____/__________    _____\______   \ _____/  |_  \______   \___.__.  |   ____/|  | \_____  \___.__.\_____  \______ 
 \_____  \\____ \__  \  /     \|    |  _//  _ \   __\  |    |  _<   |  |  |____  \ |  |   _(__  <   |  |  _(__  <_  __ \
 /        \  |_> > __ \|  Y Y  \    |   (  <_> )  |    |    |   \\___  |  /       \|  |__/       \___  | /       \  | \/
/_______  /   __(____  /__|_|  /______  /\____/|__|    |______  // ____| /______  /|____/______  / ____|/______  /__|   
        \/|__|       \/      \/       \/                      \/ \/             \/             \/\/            \/       
''')

    spam = input("Enter your spam text:\n-> ") #Gets the input from the user and stores it as the spam text 
    num = input("\nNumber of times to spam (Leave it for if you want it to spam forever):\n-> ") #sets number of time to spam
    if num == "": #if num is blank sets num to 999999... you won't let this loop that many times would you ?
        num = 999999

    print('\nThe spam will begin in 10 seconds... BRACE YOURSELF !!!\n')#BRACE YOURSELF !!!!
    print("Return to this window and press 'ctrl/cmd + c' to stop the spam anytime\n\n")#how to stop the chaos
    sleep(10)#gives time for lazy users to point towards the input box

    for _ in range(int(num)):
        sleep(0.3)#stop the spam for 0.3 seconds every loop
        pyautogui.typewrite(spam) #types the spam text in the input box
        press('enter') # hits enter
    
    end()#calls the end function

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping the script')
        end()
