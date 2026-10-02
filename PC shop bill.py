line_1 = "=" *100

print (line_1)

shop_name = "                                     Digital Point Computers"
bill_catagoty = "                                           invoice bill"
line_2 = "=" *100
print(shop_name,bill_catagoty,line_2,sep="\n")

name = "customer's name : jake"
date = "                                                             Date : 12/2/2026"
invoice_number = "INVOICE.NO : 17"

print (name,date,"\n")
print(invoice_number)
print ("_"*100)

item = "NAME OF ITEMS"
qty = "                                 QTY" 
rate = "                 RATE" 
amount = "                     AMOUNT" 

print(item,qty,rate,amount)

print ("_"*100)

item_1 = "Assus Laptop, Model no: ASUS Vivobook 16 |"
qty1 = 1
rate1 = 86990
amount1 = 86990


print (item_1,"    ",qty1,"                 ",rate1,"                    ",amount1)

item_2 = "kreo hive 65 keyboard                    |"
qty2 = 5
rate2 = 2500
amount2 = 12500

print (item_2,"    ",qty2,"                 ",rate2,"                  ""   ",qty2*rate2)

item3 = "kreo hawk mouse                          |"
qty3 = 3
rate3 = 1500
amount3 = 4500

print (item3,"    ",qty3,"                 ",rate3,"                     ",qty3*rate3)

print ("_"*100)

Subtotal = amount1+amount2+amount3

gst = (amount1+amount2+amount3) * 10.77 / 100

plus = Subtotal + gst 

print (" "*78,"Total amount :",Subtotal)  

print ("GST : 10.77%"," "*78,round(gst,2))

print ("Plus GST"," "*81,round(plus,2))

print( )

discount_amount = plus * 8.3 /100

final_total = plus - discount_amount

print ("Discount : 8.3%"," "*76,round(discount_amount,2))

print("Final Total"," "*78,round(final_total,2))

print ("_"*100)

print("Authorized signatory"," "*61,"Thanks for visit")

print ("="*100)


