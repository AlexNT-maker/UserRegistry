

class Person:
    def __init__(self,name,surname,city,phone,user_code):
        self.name=name
        self.surname=surname
        self.city=city
        self.phone=phone
        self.unique_code=user_code
        
        
    def to_dict(self):
        return{
            "Name":self.name,
            "Surname":self.surname,
            "City":self.city,
            "Phone":self.phone,
            "Code":self.unique_code
            }
    
    def print_the_data(self):
        print(f"name: {self.name}, surname: {self.surname}, city:{self.city}, phone{self.phone}, unique code:{self.unique_code}")
        
    
    @staticmethod 
    def from_dict(data):
        return Person(
            name=data["Name"],
            surname=data["Surname"],
            city=data["City"],
            phone=data["Phone"],
            user_code=data["Code"]
            )

        
        