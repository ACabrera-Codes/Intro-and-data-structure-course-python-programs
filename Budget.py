#The goal is to solve the problem of: creating a budget so that you can start building up your savings.
#You want to have all of your money accounted for , meaning that each $ has a job
#so that you can work towards increasing your savings and paying off your debts each month. 

#This program lets you add your income and expenses with an end result showing: the totals , if your expenses
#are more than your income ( meaning you over spent) , or if you were smart about where you put your money
#making you one step closer to being debt free and having an emergency savings.

#Your savings and debt would be considered an expense ( place you are putting your money from your income)
# You would put how much each month you are budgeting for your debt and savings, along with your other monthly living expenses
#Data structures used are : lists and dictionaries.

import sys

class BudgetProject:
    def __init__(self, amount): # The variables that will track the amount budgeted and spent in empty dictionarys
        self.remaining = amount
        self.budgets = {} 
        self.spending = {} 
 # expense method: takes name of the expense and amount of money to be budgeted for it
    def add_expense(self, name, amount):                
        if name in self.budgets:  
            print("This expense is already accounted for.")
        self.budgets[name] = amount # this stores the budgeted amount in the budgets dict. 
        self.spending[name] = [] # empty list to store each amount spent in the spending dict. 
        self.remaining -= amount # subtracts the budgeted amount from money available
        return self.remaining    
            
    def spend_income(self, name, amount): # method to show $ spent and name of expense you will track against
        if name not in self.spending: # error if the expense name is not a key in the spent dict. 
            print("This expense is not listed.")
        self.spending[name].append(amount) #adds each expense to the spending list  
        budgeted = self.budgets[name]
        spent = sum(self.spending[name])
        return budgeted - spent   
    
    def print_summary(self): # method to show summary 
        income = int(input(" What is your total income for the month? "))
        print("")
        print("Expenses         Allocated    Spent       Remaining")
        print("---------------| -----------| ----------| ----------|")
        totalBudgeted = 0
        totalSpent = 0
        totalRemain = 0 
        for name in self.budgets: #loops through keys in the budget dict. 
            budgeted = self.budgets[name] # gets the budgeted/allocated amount for the name key 
            spent = sum(self.spending[name]) #amount spent for each expense
            remaining = budgeted - spent # calcs the remaining $ after subtracting the budgeted from spent 
            
            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} '
                  f'{remaining:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemain += remaining
        print("---------------| ----------| ----------| ----------|")
        print(f'{"Total":15s} {totalBudgeted:10.2f} {totalSpent:10.2f} '
              f'{totalBudgeted - totalSpent:10.2f}')
        print("")
        MoneyLeft = income - totalSpent
        if MoneyLeft < 0:
            print('You have over drafted, you have a deficit of ' + '$' + str(MoneyLeft))
        
        if MoneyLeft == 0:
            print('You have sucessfully completed a zero dollar budegt, congrats every dollar is accounted for!')
        
        if MoneyLeft > 0:
            print('You should assign this extra money to savings, debt, or something fun. You have a surplus of ' + '$' + str(MoneyLeft))
        
    def close_program(self): 
        print("Congrats, you finished budgeting! See you later! ")
        sys.exit(0)
        
 
        
          
       
        
