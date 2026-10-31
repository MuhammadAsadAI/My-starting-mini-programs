print("=" *100)
print (" "*35,"PETER JOHN COMPUTER SHOP")
print ("=" *100)

print ("customer's name: Harry Curture"," "*53,"date :12/3/2025")
print ()

print ("INVOICE NO: 10")

print ("_" *100)

print ()

item_1 = (input("Item name 1: "))
qty_item_1 = int(input("Qty item 1: "))
rate_item_1 = float(input("Rate item 1: "))
amount_item_1 = (qty_item_1*rate_item_1)
print ("_" *100)

print ()

item_2 = (input("Item name 2: "))
qty_item_2 = int(input("Qty item 2: "))
rate_item_2 = float(input("Rate item 2: "))
amount_item_2 = (qty_item_2*rate_item_2)
print ("_" *100)

print ()

item_3 = (input("Item name 3: "))
qty_item_3 = int(input("Qty item 3: "))
rate_item_3 = float(input("Rate item 3: "))
amount_item_3 = (qty_item_3*rate_item_3)
print ("_" *100)

print ()

print ("NAME OF ITEMS"," " *28,"QTY"," " *20,"RATE"," "*20,"AMOUNT")
print ("_" *100)

print (item_1," "*19,qty_item_1," "*20,rate_item_1," "*16,amount_item_1)

print (item_2," "*24,qty_item_2," "*22,rate_item_2," "*18,amount_item_2)

print (item_3," "*25,qty_item_3," "*21,rate_item_3," "*18,amount_item_3)

print ("_" *100)

total_amount = (amount_item_1+amount_item_2+amount_item_3)
print (" " *76,"Total Amount :",total_amount)

gst = (total_amount) * 8.65 / 100
print ("GST : 8.65%"," "*79,round(gst,2))

plus_gst = (total_amount+gst)
print ("Plus GST"," " *81,round(plus_gst,2))

print ()

discount_amount = plus_gst * 4.11 /100
final_total = (plus_gst-discount_amount)

print ("Discount Amount : 4.11%"," " *67,round(discount_amount,2))
print ("Final Total"," " *78,round(final_total,2))
print ("_" *100)

print ("Thank you!"," " *73,"Visit again....")
print ("_" *100)