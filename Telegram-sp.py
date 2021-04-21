from telethon.sync import TelegramClient, events
import random
import time
import os 


print("""
     Afshin Ataei 
""")

print("""
 ____                                            
/ ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 ___) | |_) | (_| | | | | | | | | | | |  __/ |   
|____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
      |_|                                        

""")

print("enter your custom text for spam")
time.sleep(1)
print("for end text enter [ST]")



while True:
    cuslist = input("your text for spam :  ")
    is_spam = False
    with open("list.txt","a") as file :
        file.write(str(cuslist + "\n"))
        if "ST" in cuslist: 
            id_input = input("enter target id withuot @ :")
            for_theard = input("enter theard number :  ")
            print("\033[95m------------------------Afshin------------------------")
            
            api_id = 
            api_hash = ""
            with TelegramClient('session_name', api_id, api_hash) as client:
                for i in range(int(for_theard)):
                    fileo = open("list.txt").read().splitlines()
                    filek = random.choices(fileo)[0]
                    print("\033[95m")
                    print(filek + "\033[95m SUCSSES")
                    client.send_message(f"{id_input}", f"{filek}")
                    is_spam = True
    if is_spam == True:
        os.system("rm list.txt")
        print("Create by Afshin Ataei") 
        break
