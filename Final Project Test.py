def Testing(): # output variables are instances of the budget project class so we can test 
    import Budget # import the module so we can test our budget instances below 
    output = Budget.BudgetProject(3000) # enter your total income for the month
    #Housing includes rent, utilities, and cable
    output.add_expense("Housing", 1421.54) # enter the name and cost of each expense 
    output.add_expense("Car Maintenence", 288.47)
    output.add_expense("Food", 250)
    output.add_expense("Personal", 300)
    output.add_expense("Insurance", 171.66)
    output.add_expense("Debt", 350.75)
    output.add_expense("Savings", 200)
    
    output.spend_income("Savings", 300) # enter amount spent towards the expense
    output.spend_income("Housing", 1421.54)
    output.spend_income("Food", 150)
    output.spend_income("Personal", 200)
    output.spend_income("Debt", 350.75)
    output.spend_income("Car Maintenence", 288.47)
    output.spend_income("Insurance", 171.66)
    output.print_summary()
    print("")
    output.close_program()     

Testing()
