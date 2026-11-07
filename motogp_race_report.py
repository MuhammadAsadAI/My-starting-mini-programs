print ("============================================================================================")
print ("                               MOTOGP RACE REPORT IN QATAR")
print ("============================================================================================")
print ("RIDER INFO")
print ("____________________________________________________________________________________________")

rider_name = "Toprak Razgatlioglu"
rider_nationality = "Turkey"
rider_team = "Prima Pramac Yamaha MotoGP"
rider_bike = "Yamaha YZR-M1"
rider_number = 7

print ("Rider Name        :",rider_name)
print ("Nationality       :",rider_nationality)
print ("Team              :",rider_team)
print ("Bike              :",rider_bike)
print ("Rider Number      :",rider_number)

print ("____________________________________________________________________________________________")
print ("RIVAL INFO")
print ("____________________________________________________________________________________________")

rival_name = "Marc Marquez"
rival_nationality = "Spain"
rival_team = "Ducati Lenovo Team"
rival_bike = "Ducati Desmosedici GP"

rival_number = 93
print ("Rival Name        :",rival_name)
print ("Nationality       :",rival_nationality)
print ("Team              :",rival_team)
print ("Bike              :",rival_bike)
print ("Rival Number      :",rival_number)

print ("____________________________________________________________________________________________")
print ("LAP TIMES")
print ("____________________________________________________________________________________________")

rider_lap_1 = float(input("Enter Rider LAP 1 : "))
rider_lap_2 = float(input("Enter Rider LAP 2 : "))
rider_lap_3 = float(input("Enter Rider LAP 3 : "))
print ()
rival_lap_1 = float(input("Enter Rival LAP 1 : "))
rival_lap_2 = float(input("Enter Rival LAP 2 : "))
rival_lap_3 = float(input("Enter Rival LAP 3 : "))

print ("____________________________________________________________________________________________")
print ("CALCULATION")

rider_total_time = round((rider_lap_1+rider_lap_2+rider_lap_3),2)
rival_total_time = round((rival_lap_1+rival_lap_2+rival_lap_3),2)
#total_race_time = (rider_total_time+rival_total_time)
avg_rider = round(rider_total_time/3,2)
avg_rival = round(rival_total_time/3,2)

rider_total_minutes = round(rider_total_time // 60,2)
rider_seconds = round(rider_total_time % 60,2)

rival_total_minutes = round(rival_total_time // 60,2)
rival_seconds = round(rival_total_time % 60,2)

gap_to_rival = round(rider_total_time-rival_total_time,2)

rider_best_lap = min(rider_lap_1,rider_lap_2,rider_lap_3)
rider_worst_lap = max(rider_lap_1,rider_lap_2,rider_lap_3)

rival_best_lap = min(rival_lap_1,rival_lap_2,rival_lap_3)
rival_worst_lap = max(rival_lap_1,rival_lap_2,rival_lap_3)

rider_lap_spread = round(rider_worst_lap-rider_best_lap,2)
rival_lap_spread = round(rival_worst_lap-rival_best_lap,2)

rider_is_faster = (rider_total_time<rival_total_time)
rival_is_faster = (rival_total_time<rider_total_time)

rider_is_consistent = (rider_lap_spread<1.0)
rival_is_consistent = (rival_lap_spread<1.0)

rider_is_podium_pace = (avg_rider<100)
rival_is_podium_pace = (avg_rival<100)

rider_need_better_tyres = (rider_lap_spread>1.5)or(avg_rider>=100)
rival_need_better_tyres = (rival_lap_spread>1.5)or(avg_rival>=100)

rider_is_slow = not(rider_is_podium_pace)
rival_is_slow = not(rival_is_podium_pace)

print ("____________________________________________________________________________________________")

print ("RIDER TOTAL RACE TIME :",rider_total_time,"seconds")
print ("RIVAL TOTAL RACE TIME :",rival_total_time,"seconds")
print ()
print ("AVERAGE RIDER TIME :",avg_rider,"seconds")
print ("AVERAGE RIVAL TIME :",avg_rival,"seconds")
print ()
print ("RIDER TOTAL MINUTES :",rider_total_minutes)
print ("RIDER TOTAL SECONDS :",rider_seconds)
print ()
print ("RIVAL TOTAL MINUTES :",rival_total_minutes)
print ("RIVAL TOTAL SECONDS :",rival_seconds)
print ()
print ("RIDER BEST LAP :",rider_best_lap)
print ("RIDER WORST LAP :",rider_worst_lap)
print ()
print ("RIVAL BEST LAP :",rival_best_lap)
print ("RIVAL WORST LAP :",rival_worst_lap)
print ()
print ("RIDER LAP SPREAD :",rider_lap_spread)
print ("RIVAL LAP SPREAD :",rival_lap_spread)

print ("____________________________________________________________________________________________")

print ()
print ("GAP TO RIVAL :",gap_to_rival)

print ("____________________________________________________________________________________________")

print ("RIDER IS FASTER :",rider_is_faster)
print ("RIVAL IS FASTER :",rival_is_faster)
print ()
print ("RIDER IS CONSISTENT :",rider_is_consistent)
print ("RIVAL IS CONSISTENT :",rival_is_consistent)
print ()
print ("RIDER IS PODIUM PACE :",rider_is_podium_pace)
print ("RIVAL IS PODIUM PACE :",rival_is_podium_pace)
print ()
print ("RIDER NEEDS BETTER TYRES :",rider_need_better_tyres)
print ("RIVAL NEEDS BETTER TYRES :",rival_need_better_tyres)
print ()
print ("RIDER IS SLOW :",rider_is_slow)
print ("RIVAL IS SLOW :",rival_is_slow)
print ("___________________________________________________________________________________________")
print ()

print ("Toprak Razgatlioglu WINNER :",rider_is_faster)
print ("Marc Marquez WINNER :",rival_is_faster)

print ("___________________________________________________________________________________________")
print ("Marc Marquez is Champion                                ","Bro Don't Worry Try Next Year.....")
print ("===========================================================================================")