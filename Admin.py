"""Controls Admin,Bank System And ATM Data"""

__author__ = "Johnson Onoja <johnsononoja60@yahoo.com"

from tkinter import messagebox

class Admin(object):
    """Admin's class __init__ method takes a pin as only argument and if pin
    is verified to be admin's pin,initialises it and sets the details.
    Admin's Account Balance Is The Totalcash in The ATM at any specific time,
    if admin's balance is empty, it means no cash in the atm again.
    """
    
    def __init__(self,pin):
        self.__name = "admin"
        self.__pin = pin
        self.__DataBase = open("database.txt","r")
        self.__dbm = self.__DataBase.read().replace("\n","")
        self.DataBase = eval(self.__dbm)
        self.__DataBase.close()
        
        """Searches the database for admin's pin"""
        for key,value in self.DataBase.items():
            if ("admin" in value and self.__pin in value):
                self.AcctNo = key
                self.__bal = value[2]
                break

    @staticmethod
    def register_user(username):
        database = open("database.txt","r")
        last_acct_no = None
        db = database.read().replace("\n","")
        del database
        
        DataBase = eval(db)
        for key in DataBase:
            last_acct_no = key
            
        new_acct_no = last_acct_no + 1
        new_acct_details = [username,1234,0.00]
        DataBase[new_acct_no] = new_acct_details

        db = "{\n"
        for key in DataBase:
            db += str(key)+": "+str(DataBase[key])+",\n"
        db += "}"

        try:
            with open("database.txt","w") as database:
                database.write(db)
            return True
        except BaseException as e:
            logging.error(e)
            del database
            return False
        
            
    def CheckPin(self):
            """ Verifies If User's Pin Exists"""
            
            for key,value in self.DataBase.items():
              if ("admin" in value and self.__pin in value):
                return True
            else: return False

    def UserInfo(self):
        return self.DataBase

    def GetBalance(self):
        return self.__bal

    def delete_user_account(self,number,name):
        for key in self.DataBase:
            if (key == number and name in self.DataBase[key]):
                del self.DataBase[key]
                self.db = "{\n"
                for item in self.DataBase:
                    self.db += str(item)+": "+str(self.DataBase[item])+",\n"
                self.db += "}"
                try:
                    with open("database.txt","w") as database:
                        database.write(self.db)
                    return True
                except BaseException as e:
                    logging.error(e)
                    messagebox.showerror("ERROR","An Error Occurred,Check Errors.txt To View It")
                    return False
        else:
            messagebox.showerror("ERROR","Invalid Credentials!!")
            return False

    def Deposit(self,amnt):
        self.__bal += amnt
        self.DataBase[self.AcctNo][2] = self.__bal

        self.db = "{\n"
        for key in self.DataBase:
            self.db += str(key)+": "+str(self.DataBase[key])+",\n"
        self.db += "}"
        
        try:
            self.__DataBase = open("DataBase.txt","w")
            self.__DataBase.write(self.db)
        except BaseException as e:
            self.__DataBase.close()
            logging.error(e)
            messagebox.showerror("ERROR","There was an error !!\nCheck errors.txt to view the error")            
            return False
        else:
            self.__DataBase.close()
            return (True,self.__bal)
