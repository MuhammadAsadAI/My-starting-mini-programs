print ("=================================================================")
print ("                       MOIN KIRANA STORE")
print ( "                   MONTHLY BILL CALCULATOR")         
print ("=================================================================")     

this_month_income = float(input("Enter This Month Total Income: "))
electricity = float(input("Enter Electricity Bill: "))
labour_salary = float(input("Enter Labour Salary: "))
shop_rent = float(input("Enter Shop Rent: "))
material_cost = float(input("Enter Material cost: "))
other_small_expense = float(input("Enter Other Small expense: "))

total_expense = (electricity+labour_salary+shop_rent+material_cost+other_small_expense)

total_profit = (this_month_income-total_expense)

print ()

print ("==========================Bill Summary===========================")
print ("This Month Income: ",this_month_income)
print ("Electricity Bill: ",electricity)
print ("Labour Salary: ",labour_salary)
print ("Shop Rent: ",shop_rent)
print ("Material Cost: ",material_cost)
print ("Other Small Expense: ",other_small_expense)
print ("-----------------------------------------------------------------")
print ("Total monthly expense: ",total_expense)
print ("Total monthly profit: ",total_profit)
print ("=================================================================")

