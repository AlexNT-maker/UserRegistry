import file_handler #Import functions from file handler.py
import random
from Person import Person
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QLabel, QTextEdit, QColorDialog, QMessageBox
from PyQt5.QtGui import QFont, QColor
import sys

file_handler.retrieve_codes()
file_handler.load_users_from_file()


codes_list=set()

class MainWindow(QMainWindow):
    """
    Main application window for User Registry.
    Handles user input, search, and save functionalities via PyQt5 GUI.
    """
    def __init__(self):
        super().__init__()
        color=QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color:{color.name()}")
        self.setWindowTitle("User-Registry")
        self.setGeometry(500,60,1450,1400)
        
        #label for data input section
        self.label=QLabel(self)
        self.label.setText("Data input:")
        self.label.move(40,20)
        self.label.setFont(QFont("Times",10))
        self.label.setStyleSheet("color:darkred;font-weight:bold")
        self.label.resize(130,130)
        
        #name input
        self.label_name=QLabel(self)
        self.label_name.setText("Name")
        self.label_name.move(50,130)
        self.label_name.setFont(QFont("Times",10))
        self.label_name.setStyleSheet("color:darkred; font-weight:bold;")
        
        
        self.textbox_for_name=QLineEdit(self)
        self.textbox_for_name.move(140,130)
        self.textbox_for_name.setFont(QFont("Times",10))
        
        #surname input
        self.label_surname=QLabel(self)
        self.label_surname.setText("Surname")
        self.label_surname.move(40,190)
        self.label_surname.setFont(QFont("Times",10))
        self.label_surname.setStyleSheet("color:darkred; font-weight:bold;")
        
        
        self.textbox_for_surname=QLineEdit(self)
        self.textbox_for_surname.move(140,190)
        self.textbox_for_surname.setFont(QFont("Times",10))
        
        #city input
        self.label_city=QLabel(self)
        self.label_city.setText("City")
        self.label_city.move(50,250)
        self.label_city.setFont(QFont("Times",10))
        self.label_city.setStyleSheet("color:darkred; font-weight:bold;")
        
        
        self.textbox_for_city=QLineEdit(self)
        self.textbox_for_city.move(140,250)
        self.textbox_for_city.setFont(QFont("Times",10))
        
        #phone number input
        self.label_number=QLabel(self)
        self.label_number.setText("Number")
        self.label_number.move(40,310)
        self.label_number.setFont(QFont("Times",10))
        self.label_number.setStyleSheet("color:darkred; font-weight:bold;")
        
        
        self.textbox_for_number=QLineEdit(self)
        self.textbox_for_number.move(140,310)
        self.textbox_for_number.setFont(QFont("Times",10))
        
        
                
        
        self.addbutton=QPushButton(self,text="add")
        self.addbutton.clicked.connect(self.add_data_to_list)
        self.addbutton.setStyleSheet("color:darkred")
        self.addbutton.move(140,380)
        self.addbutton.setToolTip("Click here to generate your unique code")
        
        self.label_datasearch=QLabel(self)
        self.label_datasearch.setText("Data search")
        self.label_datasearch.move(650,85)
        self.label_datasearch.setFont(QFont("Times",10))
        self.label_datasearch.resize(120,120)
        self.label_datasearch.setStyleSheet("color: darkred; font-weight:bold;")
        
        self.textbox_for_datasearch=QLineEdit(self)
        self.textbox_for_datasearch.move(800,130)
        self.textbox_for_datasearch.setFont(QFont("Times",10))
        
        self.searchbutton=QPushButton(self,text="Search")
        self.searchbutton.clicked.connect(self.retrieve_code_data)
        self.searchbutton.setStyleSheet("color:darkred")
        self.searchbutton.move(920,130)
        
        
        self.savebutton=QPushButton(self,text="Save")
        self.savebutton.clicked.connect(self.save_data)
        self.savebutton.setStyleSheet("color:darkred")
        self.savebutton.move(140,425)
        
    
       
        
        
        
    def add_data_to_list(self):
        """Adds a new user entry to the system and assigns a unique code."""
        name=self.textbox_for_name.text().strip().capitalize()
        surname=self.textbox_for_surname.text().strip().capitalize()
        city=self.textbox_for_city.text().strip().capitalize()
        phone=self.textbox_for_number.text().strip()
        
        
        for user in file_handler.user_1:
            if user.name==name and user.surname==surname and user.phone==phone:
                QMessageBox.warning(self,"Duplicate","User with the following details already exists")
                return
             
        
        
        try:
            user_dict=file_handler.user_data(name, surname, city, phone)
            
            
            QMessageBox.information(self, "Success", f"The user has added in the list.\n unique code: {user_dict['Code']}")
            
        except ValueError as e:
            QMessageBox.warning(self,"error",str(e))
            
    
    def retrieve_code_data(self):
        """Retrieves user data based on a unique code input by the user."""
        code=self.textbox_for_datasearch.text().strip()
        if not code.isdigit():
            QMessageBox.warning(self,"Error","Please fill the code box only with your 6 digit unique code")
            return
        
        if not file_handler.user_access(code):
            QMessageBox.warning(self,"Cancel","Code does not exists")
            
            
        
        user=file_handler.retrieve_data_by_code(code)
        if user:
            QMessageBox.information(self,"The unique code match with user ", str(user))
            
        else:
            QMessageBox.warning(self,"Error","No user match with the input code")

        

    def save_data(self):
        """Saves all current users and codes to their respective files."""
        file_handler.save_to_file()
        QMessageBox.information(self,"Saved","Data saved succesfully")
        
            
        
      


          




        self.show()
        

       
        
        

app=QtWidgets.QApplication(sys.argv)

window=MainWindow()

window.show()
sys.exit(app.exec())