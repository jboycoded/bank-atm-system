"""Design implementation module for the Bank-System"""

__author__ = "Johnson Onoja <johnsononoja60@yahoo.com"

from tkinter import *

def mainDesign(master,self):
        """main Design"""
        
        Frame.__init__(self,master,bg = "blue")
        self.pack(expand = TRUE,fill = BOTH)
        self.master.title("UI BANK")
        self.master.minsize(400,400)
        self.master.maxsize(400,400)
        self.master.protocol("WM_DELETE_WINDOW",self.Cancel)
        
        w = 250; h = 250
        x = (self.master.winfo_screenwidth()-w)/2
        y = (self.master.winfo_screenheight()-h)/2
        self.master.geometry("%dx%d+%d+%d" %(w,h,x,y))
        for c in self.master.winfo_children():
            c.pack_configure(padx = 5,pady = 5)

def mainMenu(master,self):
        """Main Menu design implementation"""
        
        self.mbar = Menu(self)
        self.master.config(menu = self.mbar)
        self.login = Menu(self.mbar,tearoff = 0)
        
        self.mbar.add_cascade(label = "Log-In",menu = self.login)
        self.mbar.add_cascade(label = "Exit",command = self.Cancel)
        
        self.login.add_command(label = "Admin",command=self.AdminStart)
        self.login.add_separator()
        self.login.add_command(label = "User",command = self.UserStart)

def userDesign(master,self,str = "USER ACCOUNT"):
        """User's header design"""
        
        self.destroy()
        mainDesign(master,self)
        Label(self,text = str,fg = "blue",relief = RAISED,bg = "black",borderwidth = 10,height = 2,
              padx = 3,pady = 3,width = 37,font = "ALGERIAN").grid(columnspan = 100)

def userMenu(master,self):
        """User's menu creation"""
        
        self.mbar = Menu(self)
        self.master.config(menu = self.mbar)
        self.option = Menu(self.mbar,tearoff = 0)
        
        self.mbar.add_cascade(label = "User",menu = self.option)
        self.mbar.add_command(label = "Exit",command = self.Cancel)

        self.option.add_command(label = "Deposit Funds",command = self.Deposit)
        self.option.add_separator()
        self.option.add_command(label = "Withdraw cash",command = self.Withdraw)
        self.option.add_separator()
        self.option.add_command(label = "Balance Inquiry",command = self.balance)
        self.option.add_separator()
        self.option.add_command(label = "Transfer Funds",command = self.Transfer)
        self.option.add_separator()
        self.option.add_command(label = "Change Pin",command = self.ChangePin)
        self.option.add_separator()
        self.option.add_command(label = "Delete Account",command = self.DelAccount)

def adminDesign(master,self,str = "ADMIN ACCOUNT"):
        """Admin's header design"""
        
        self.destroy()
        mainDesign(master,self)
        Label(self,text = str,fg = "blue",relief = RAISED,bg = "black",borderwidth = 10,height = 2,
              padx = 3,pady = 3,width = 37,font = "ALGERIAN").grid(columnspan = 100)

def adminMenu(master,self):
        """Admin menu creation"""
        
        self.mbar = Menu(self)
        self.master.config(menu = self.mbar)
        self.option = Menu(self.mbar,tearoff = 0)
        
        self.mbar.add_cascade(label = "Admin",menu = self.option)
        self.mbar.add_command(label = "Exit",command = self.Exit)

        self.option.add_command(label = "Deposit Funds",command = self.AdminDeposit)
        self.option.add_separator()
        self.option.add_command(label = "Balance In ATM",command = self.AdminBalance)
        self.option.add_separator()
        self.option.add_command(label = "Register New User",command = self.register_new_user)
        self.option.add_separator()
        self.option.add_command(label = "Users' Info",command = self.usersInfo)
        self.option.add_separator()
        self.option.add_command(label = "Total Users' Cash",command = self.view_all_cash)
        self.option.add_separator()
        self.option.add_command(label = "Delete User Account",command = self.delete_user_account) 

