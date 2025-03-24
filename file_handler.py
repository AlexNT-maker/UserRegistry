import random
import json
from Person import Person

user_1=[] #List to store person objects
codes_list=set() #set to store unique user codes


def code():
    """
    Generate a unique  6-digit user code by multiplying two random numbers.
    Ensures no duplicate code exists in the global codes_list.

   

    """
    global codes_list
    max_attempts=1000
    attempts=0
    while(attempts<max_attempts):
        a=random.randint(1, 999999)
        b=random.randint(1, 999999)
        unique_code=a*b
        unique_code_str=str(unique_code)[:6]
        user_code=int(unique_code_str)
        if user_code not in codes_list:
            codes_list.add(user_code)
            return user_code
    attempts+=1
    
  

      

def user_data(name,surname,city,phone):
    """
   Creates a new user and return their data as a dictionary.
   Validates inputs and assigns a unique code.

    Args:
        name(str): Users first name
        surname(str):Users surname
        city(str): Users city
        phone(str): Users phone number
        
        Returns:
            dict
        raises Value error:
            if inputs are invalid

    """
    global user_1
    if not name.isalpha() or not surname.isalpha() or not city.isalpha():
        raise ValueError("Name/Surname/City must contain letters")
    if not phone.isdigit():
        raise ValueError("Phone must contain only digits")
        
    user_code=code()
    user=Person(name,surname,city,phone,user_code)
    user_1.append(user)
    return user.to_dict()
        
    

                        

def user_access(otp):
    """
    Checks if a given code exists in the codes list

    Args:
        otp(int or str). The code to check 
        
    Returns:
        bool

    """
    return(int(otp)) in codes_list



def save_to_file():
    """Save the current users from user_1 to save.txt and clear the list.
    Also triggers saving of unique codes.
    """
    
    try:
        with open("save.txt",'w') as file:
            for user in user_1:
                file.write(json.dumps(user.to_dict())+'\n')
        save_code()
        print("Users saved to save.txt")
        user_1.clear()
        
        
    except Exception as e:
        print("Eror while saving",e)    
    
    


def print_save():
    """Print all saved user data from save.txt."""
    try:
        with open ("save.txt",'r') as file:
            save_data=file.readlines()
            for lines in save_data:
                user_info=json.loads(lines.strip())
                print(user_info)
    
    except Exception as e:
        print("File not found",type(e).__name__, "-", e)
        
 



def retrieve_data_by_code(otp):
    """Retrieve a user's data from save.txt using their unique code.

   Args:
       otp (str): The unique code to search for

   Returns:
       dict or None: The user info if found, else None
   """
    global user_1
    try:
        with open("save.txt",'r') as file:
            read_data=(file.readlines())
            
            for data in read_data:
               if not data.strip():
                   continue
               user_info=json.loads(data.strip())
               if str(user_info.get("Code"))==otp:
                   return (user_info)
                   
               else:
                   return None 
                   
              
                   
                 
               
               
    except:
        return("the code does not exist in the list")
        


def save_code():
    """Save all unique user codes into code_set.txt.
    Ensures no duplicates by loading and merging existing codes.
    """
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
        
    


def retrieve_codes():
    """Load all unique user codes from code_set.txt into codes_list."""
    global codes_list
    try:
        with open("code_set.txt",'r') as file:
            codes_list={int(line.strip())for line in file if line.strip().isdigit()}
        print("codes succesfully loaded",codes_list)
        
    except FileNotFoundError:
        print("File does not exist")
            
  
       
def load_users_from_file():
    """Load user data from save.txt and store as Person objects in user_1."""
    global user_1
    try:
        with open("save.txt",'r') as file:
            user_1=[Person.from_dict(json.loads(line.strip())) for line in file if line.strip()]
            print("user data succesfully loaded")
    except FileNotFoundError:
        print("No data found")
        

    
        
        
               
   
        
            

    
    

    

        