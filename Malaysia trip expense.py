print ("=" *120)
main_title = "INDIA TO MALAYSIA TRIP EXPENSE"
print (" " *40,main_title)
print ("=" *120)

print ("Trip Detail |")
print ()

trip = "TRIP : India to Malaysia"
friends = "FRIENDS : 7"
location = "LOCATION IN MALAYSIA : Kuala Lumpur"
in_kuala_lumpur = "LOCATIONS IN KUALA LUMPUR : KL Tower (Menara KL), Petronas Twin Towers, KL Bird Park, Aquaria KLCC"

print (trip,friends,location,in_kuala_lumpur,"=" *120,sep="\n")

total_days = 10
total_friends = 7
total_budget = 600000
per_person_limit = 70000
misc_buffer = 15000
print ("TOTAL DAYS : ",total_days)
print ("TOTAL FRIENDS : ",total_friends)
print ("TOTAL BUDGET : ",total_budget)
print ("PER PERSON LIMIT : ",per_person_limit)
print ("MISC BUFFER : ",misc_buffer)
print ("_"*120)

print ("Trip Expense in INR"," " *81,"Trip Expense in RM")
print ()

INR_currency = 23.71
five_friends = 5  

per_person_h_to_a_charge = 12.65
total_charge = (per_person_h_to_a_charge*total_friends)

print ("HOME TO AIRPORT :",float(round(total_charge*INR_currency))," "*92,round(total_charge))


airport_bags_wrapping = 116.74
airport_food = 147.62
airport_tickets = 2994.
total_airport_charge = (airport_bags_wrapping+airport_food+airport_tickets)

print("AIRPORT TO FLIGHT ONE WAY :",float(round(total_airport_charge*INR_currency))," "*77,round(total_airport_charge))
print ("_"*120)

print ("SAFELY LAND IN MALAYSIA......")


per_person_taxi_charge = 23
taxi_1_charge = (per_person_taxi_charge*4)
taxi_2_charge = (per_person_taxi_charge*3)
total_taxi_charge = (taxi_1_charge+taxi_2_charge)
print ("KLIA AIRPORT TO HOTEL :",round(total_taxi_charge*INR_currency,2)," "*84,total_taxi_charge)
print("_"*120)

print ("ENTER HOTEL.....")

room_1_rent_per_day = 150
room_2_rent_per_day = 150
plus_2_room_rent = (room_1_rent_per_day+room_2_rent_per_day)
total_10_days_rent = (plus_2_room_rent*total_days)
print ("TOTAL 10 DAYS 2 ROOMS HOTEL RENT :",round(total_10_days_rent*INR_currency,2)," "*72,total_10_days_rent)


breakfast_cost_per_person = 12
lunch_cost_per_person = 20
dinner_cost_per_person = 30
otherfood_cost_per_person = 11


total_friends_breakfast_per_day = (breakfast_cost_per_person*total_friends)
total_friends_lunch_per_day = (lunch_cost_per_person*total_friends)
total_friends_dinner_per_day = (dinner_cost_per_person*total_friends)
total_friends_otherfood_per_day = (otherfood_cost_per_person*total_friends)
total_1_day_food_cost = (total_friends_breakfast_per_day+total_friends_lunch_per_day+total_friends_dinner_per_day+total_friends_otherfood_per_day)
total_10_days_food_cost = (total_1_day_food_cost*total_days)

print("PER DAY BREAKFAST COST : ",round(total_friends_breakfast_per_day*INR_currency,2)," " * 83,breakfast_cost_per_person*total_friends)
print("PER DAY LUNCH COST : ",round(total_friends_lunch_per_day*INR_currency,2)," " *87,lunch_cost_per_person*total_friends)
print("PER DAY DINNER COST : ",round(total_friends_dinner_per_day*INR_currency,2)," " *86,dinner_cost_per_person*total_friends)
print("PER DAY OTHER FOOD COST : ",round(total_friends_otherfood_per_day*INR_currency,2)," " *82,otherfood_cost_per_person*total_friends)
print("TOTAL 10 DAYS FOOD COST : ",round(total_10_days_food_cost*INR_currency,2)," " *79,total_10_days_food_cost)
print("_"*120)

personal_guide_and_car_per_day = 650
total_3_days_guide_and_car_cost = (personal_guide_and_car_per_day*3)
print ("PERSONAL GUIDE AND CAR RENT PER DAY :",round(personal_guide_and_car_per_day*INR_currency,2)," " *70,personal_guide_and_car_per_day,)
print("ONLY 3 DAYS GUIDE AND CAR RENT : ",round(total_3_days_guide_and_car_cost*INR_currency,2)," " *73,total_3_days_guide_and_car_cost,)
print("_"*120)

print ("OK LETS, GO FOR TRIP.....")
print ()

print("FIRST LOCATION, KL Tower")
location_1_ticket_per_person = 80
total_members_tickets1 = (location_1_ticket_per_person*total_friends)
per_person_shopping_amount1 = 28
snacks_amount = 15
photography = 8
souvenir = 5
shopping_items_in_location_1 = 0
shopping_items_in_location_1 += snacks_amount
shopping_items_in_location_1 += photography
shopping_items_in_location_1 += souvenir
shopping_items_in_location_1 *= five_friends

print ("TICKET PER PERSON  : ",round(location_1_ticket_per_person*INR_currency,2)," "*88,location_1_ticket_per_person)
print ("TOTAL TICKETS :",round(total_members_tickets1*INR_currency,2)," " *92,total_members_tickets1)
print ("PER PERSON SHOPPING AMOUNT : ",round(per_person_shopping_amount1*INR_currency,2)," " *79,per_person_shopping_amount1)
print ("5 FRIEND SHOP IN KL TOWER : ",round(shopping_items_in_location_1*INR_currency,2)," " *80,shopping_items_in_location_1)#total_shopping_friends)

print ("_"*120)

print ("SECOND LOCATION, Aquaria KLCC")
location_2_tickets_per_person = 68
total_members_tickets2 = (location_2_tickets_per_person*total_friends)

# Per-person shopping budget at Aquaria (used below)

per_person_shopping_amount2 = 200 
oscar_fish_pair_1 = 81
oscar_fish_pair_2 = 75
fish_big_photo_for_room = 23
mareen_locket = 11
mid_fish_tank = 210

shopping_items_in_location_2 = 0
shopping_items_in_location_2 += oscar_fish_pair_1
shopping_items_in_location_2 += oscar_fish_pair_2
shopping_items_in_location_2 += fish_big_photo_for_room
shopping_items_in_location_2 += mareen_locket
shopping_items_in_location_2 += mid_fish_tank

print ("TICKET PER PERSON :",round(location_2_tickets_per_person*INR_currency,2)," " *89,location_2_tickets_per_person)
print ("TOTAL TICKETS : ",round(total_members_tickets2*INR_currency,2)," " *90,total_members_tickets2)
print ("PER PERSON SHOPPING AMOUNT : ",round(per_person_shopping_amount2*INR_currency,2)," " *78,per_person_shopping_amount2,)
print ("ONLY 2 BROTHERS, FRIENDS SHOP IN Aquaria KLCC, BUT LARGE AMOUNT : ",round(shopping_items_in_location_2*INR_currency,2)," " *41,shopping_items_in_location_2)

print ("_"*120)

print ("THIRD LOCATION, KL Bird Park")
location_3_tickets_per_person = 87
total_members_tickets3 = (location_3_tickets_per_person*total_friends)
per_person_shopping_amount3 = 17
all_friends_take_full_photo = 35
all_friends_take_snacks = 65


    # note: This is a TOTAL amount paid by 4 friends together (24 RM total),
    # NOT per-person. That's why we do NOT multiply by TOTAL_FRIENDS here.

purchase_birds_art_painting_by_4_friends = 24

shopping_items_in_location_3 = 0
shopping_items_in_location_3 += all_friends_take_full_photo
shopping_items_in_location_3 += all_friends_take_snacks
shopping_items_in_location_3 += purchase_birds_art_painting_by_4_friends

print ("TICKETS PER PERSON : ",round(location_3_tickets_per_person*INR_currency,2)," " *87,location_3_tickets_per_person,)
print ("TOTAL TICKETS : ",round(total_members_tickets3*INR_currency,2)," " *90,total_members_tickets3)
print ("PER PERSON SHOPPING AMOUNT : ",round(per_person_shopping_amount3*INR_currency,2)," " *80,per_person_shopping_amount3)
print ("ALL FRIENDS TAKE PHOTO AND SNACKS, 4 FRIENDS BUY PAINTING : ",round(shopping_items_in_location_3*INR_currency,2)," " *47,shopping_items_in_location_3)

print ("_"*120)

print ("FOURTH LOCATION, Petronas Twin Towers")
location_4_tickets_per_person = 132
total_members_tickets4 = (location_4_tickets_per_person*total_friends)
per_person_shopping_amount4 = 24
all_friends_take_memorable_photo = 12
all_friends_purchase_souvenir_items = 84
purchase_famous_food_for_home_5_friends = 76

shopping_items_in_location_4 = 0
shopping_items_in_location_4 += all_friends_take_memorable_photo
shopping_items_in_location_4 += all_friends_purchase_souvenir_items
shopping_items_in_location_4 += purchase_famous_food_for_home_5_friends

#per_person_shopping_amount4 = 0
#per_person_shopping_amount4 *= total_friends
#per_person_shopping_amount4 -= all_friends_take_memorable_photo
#per_person_shopping_amount4 -= all_friends_purchase_souvenir_items
#per_person_shopping_amount4 -= purchase_famous_food_for_home_5_friends

print ("TICKETS PER PERSON : ",round(location_4_tickets_per_person*INR_currency,2)," " *86,location_4_tickets_per_person)
print ("TOTAL TICKETS : ",round(total_members_tickets4*INR_currency,2)," " *90,total_members_tickets4)
print ("PER PERSON SHOPPING AMOUNT : ",round(per_person_shopping_amount4*INR_currency,2)," " *79,per_person_shopping_amount4)
print ("ALL FRIENDS TAKE PHOTO AND SNACKS,5 FRIENDS BUY FAMOUS FOODS : ",round(shopping_items_in_location_4*INR_currency,2)," " *44,shopping_items_in_location_4)

print ("_"*120)

other_general_shopping_budget_per_person = 75
total_general_shopping = (other_general_shopping_budget_per_person*total_friends)
print ("PER PERSON GENERAL SHOPPING : ",round(other_general_shopping_budget_per_person*INR_currency,2)," " *79,other_general_shopping_budget_per_person)
print ("ALL OTHER GENERAL SHOPPING : ",round(total_general_shopping*INR_currency,2)," " *78,total_general_shopping)

print ("_"*120)

print ("TRIP COMPLETED, BAY BAY MALAYSIA.....")
print ("OK, LET'S GO FROM MALAYSIA TO INDIA....")

print ("_"*120)

per_person_taxi_charge_return = 25
taxi_1_charge_return = (per_person_taxi_charge_return*4)
taxi_2_charge_return = (per_person_taxi_charge_return*3)
total_taxi_charge_return = (taxi_1_charge_return+taxi_2_charge_return)
print ("HOTEL TO KLIA AIRPORT : ",round(total_taxi_charge_return*INR_currency,2)," " *83,total_taxi_charge_return)

airport_bags_wrapping_return = 140
airport_food_return = 175
airport_tickets_return = 3150
total_airport_charge_return = (airport_bags_wrapping_return+airport_food_return+airport_tickets_return)
per_person_a_to_h_charge_return = 12
total_charge_return = (per_person_a_to_h_charge_return*total_friends)

print("AIRPORT TO FLIGHT RETURN :",round(total_airport_charge_return*INR_currency,2)," "*79,total_airport_charge_return)
print ("SAFELY LAND IN MY INDIA......")
print ()
print ("AIRPORT TO HOME :",float(round(total_charge_return*INR_currency))," "*92,round(total_charge_return))
print ("_"*120)

subtotal_rm = 0
subtotal_rm += total_charge
subtotal_rm += total_airport_charge
subtotal_rm += total_taxi_charge
subtotal_rm += total_10_days_rent
subtotal_rm += total_10_days_food_cost 
subtotal_rm += total_3_days_guide_and_car_cost
subtotal_rm += total_members_tickets1
subtotal_rm += total_members_tickets2
subtotal_rm += total_members_tickets3
subtotal_rm += total_members_tickets4
subtotal_rm += shopping_items_in_location_1
subtotal_rm += shopping_items_in_location_2
subtotal_rm += shopping_items_in_location_3
subtotal_rm += shopping_items_in_location_4
subtotal_rm += total_general_shopping
subtotal_rm += total_taxi_charge_return
subtotal_rm += total_airport_charge_return
subtotal_rm += total_charge_return
print ("SUBTOTAL IN INR : ",round(subtotal_rm*INR_currency,2)," " *64,"SUBTOTAL IN RM : ",round(subtotal_rm,2))
print ("_" *120)

per_person_expense_inr = round (subtotal_rm*INR_currency,2)

per_person_expense_inr /= total_friends
print ("PER PERSON TOTAL EXPENSE : ",round(per_person_expense_inr,2))

total_all_friends_expense = (round(per_person_expense_inr*total_friends,2))
remaining_budget = (total_budget - total_all_friends_expense)
print ("REMAINING BUDGET : ",round(remaining_budget,2))

per_person_misc_buffer_budget = 1883
misc_buffer_used = (round(per_person_misc_buffer_budget*total_friends,2))
print ("MISC BUFFER USED : ",float(round(misc_buffer_used)))
remaining_misc_buffer_budget = (misc_buffer-misc_buffer_used)
print ("REMAINING MISC BUFFER BUDGET : ",float(round(remaining_misc_buffer_budget)))
print ("_" *120)

within_budget = total_all_friends_expense <= total_budget
within_person_limit = per_person_limit >= per_person_expense_inr	
buffer_covers_overage = misc_buffer_used <= misc_buffer
trip_approved = within_budget and (within_person_limit or buffer_covers_overage)

print ("TRIP COMPLETE WITHIN BUDGET : ",within_budget)
print ("TRIP WITHIN PERSON LIMIT : ",within_person_limit)
print ("BUFFER BUDGET COVERS OVERAGE : ",buffer_covers_overage)
print ("TRIP APPROVED : ",trip_approved," " *70," CALCULATION COMPLETED.....")
print ("=" *120)