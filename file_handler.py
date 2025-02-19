import random
import json

user_1=[]
codes_list=set()
#Codes_list is established as a set to ensure that every code is unique.

def code():
    global codes_list
    a=random.randint(1, 999999)
    b=random.randint(1, 999999)
    unique_code=a*b
    unique_code_str=str(unique_code)[:6]
    user_code=int(unique_code_str)
    codes_list.add(user_code)
#The function code creates the unique code for each user     

    return user_code    

def user_data():
    while(True):
  
        global user_1
        user_info={}
        name=str(input("\nPlease enter your name:")).capitalize()
        if not name.isalpha():
            print("Name must contain only letters")
            continue
        user_info["Name"]=name
        surname=input("\nPlease enter your surname:").capitalize()
        if not surname.isalpha():
            print("Surname is allowed to contain only letters")
            continue
        user_info["Surname"]=surname
        city=input("\nPlease enter your city of residence:").capitalize()
        if not city.isalpha():
            print("The city of residence is allowed to contain only letters")
            continue
        user_info["City"]=city
        phone=input("\nPlease enter your phone number:")
        if not phone.isdigit():
            print("Phone number can contain only numbers")
            continue
        user_info["Phone"]=phone
        user_info["Code"]=code()
        user_1.append(user_info)
        print(user_1)
        break 
#The function user_data creates a dictionary with users info 

def user_access(password):
    return int(password) in codes_list

#User_access is a fuction which i have create for future improvements

def save_to_file():
    with open("save.txt",'a') as users_data:
        for user in user_1:
            users_data.write(json.dumps(user)+'\n')
    print("Data saved to save.txt")
    
#The save_to_file function saves the new data at the (save.txt) file

def print_save():
    try:
        with open ("save.txt",'r') as file:
            save_data=file.readlines()
            for lines in save_data:
                user_info=json.loads(lines.strip())
                print(user_info)
    
    except Exception as e:
        print("File not found",type(e))
        
#This function gives the user the option to retrieve all the data from (save.txt)      



def retrieve_data_by_code():
    try:
        otp=input("Please type your unique code here:").strip()
        with open("save.txt",'r') as file:
            read_data=(file.readlines())
            found=False
            for data in read_data:
               if not data.strip():
                   continue
               user_info=json.loads(data.strip())
               if str(user_info.get("Code"))==otp:
                   print(user_info)
                   found=True
                   break
               
               
    except:
        print("The code does not exist")
        
#This function gives the user the option to retrieve his data from his unique code.

def save_code():
    global codes_list
    try:
        with open("code_set.txt",'r') as codes_file:
            existing_codes={int(line.strip()) for line in codes_file if line.strip().isdigit()}
    except FileNotFoundError:
        existing_codes=set()
        
        codes_list.update(existing_codes)
        
    with open("code_set.txt",'w') as codes_file:
        for code in sorted(codes_list):
            codes_file.write(f"{code}\n")
        
    
#This function ensures that all unique user codes  are saved in the (code_set.txt) file
#By loading existing codes,added new ones and rewriting the file to avoid duplicate.

def retrieve_codes():
    global codes_list
    try:
        with open("code_set.txt",'r') as file:
            codes_list={int(line.strip())for line in file if line.strip().isdigit()}
        print("codes succesfully loaded",codes_list)
        
    except FileNotFoundError:
        print("File does not exist")
            
#The retrieve codes function give the user the option to retrieve the unique codes    
       
def load_users_from_file():
    global user_1
    try:
        with open("save.txt",'r') as file:
            user_1=[json.loads(line.strip()) for line in file if line.strip()]
            print("user data succesfully loaded")
    except FileNotFoundError:
        print("No user data found")
        
        
               
   
        
            

    
    

    

        