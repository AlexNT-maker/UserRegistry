import file_handler #Import functions from file handler.py

file_handler.retrieve_codes()
file_handler.load_users_from_file()
#Load saved user codes and user data from files 
user_1=[]
#Temporary list to store user data during execution
codes_list=set()
#set to store unique user codes
while(True):
    choice=input("""
                 Menu:
To add new data please type:new data
to retrieve old data:please type retrieve old data
to exit from the program please type exit
Type your choice here:""").lower().strip()

    if(choice=="new data"):
        file_handler.user_data()
        file_handler.save_code()
        
    if(choice=="retrieve old data"):
        choice_2=input('''If you want to print all the data type 1
if you want specific data please type 2:''').strip()
        if(choice_2=="1"):
            file_handler.retrieve_codes()
            
        elif(choice_2=="2"):
            file_handler.retrieve_data_by_code()
            
            
        else:
            print("Type a valid option")
    
    if(choice=="exit"):
        file_handler.save_to_file()
        print("Thank you for using our program")
        break
    
    else:
        print("Please choose a valid option")
          
