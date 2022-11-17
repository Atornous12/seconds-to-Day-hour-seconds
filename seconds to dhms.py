import math

#trying = int(Given_sec) % 60        # % = rem
#trying2 = int(Given_sec) / 60                 # / = simple divide
#floor_division = int(Given_sec) // 60      #  // = quotenets        


#print(trying) #gave me 10 wen typed 70.. (70-60??) so, 70/60 = 1.66667, 1 is quo and 10 is rem, so, % = rem.
#print(trying2) #gave me 1.6667, as expected... how to only get 1....
#print(floor_division) #gave me 1, cool



#so, 70 // 60 = 1
#jati sec cha, teti divide by 60 or 360 or 86400 or 2592000 or 31104000
#divide given by these, < 1 = break

#A = 70
#B = int(A) / 60
#print(B)
#C = int(A) // 60
#print(C)
#D = float(B) - float(C)
#print(D)
#print(D * 60)


#frac, whole = math.modf(5000/60)
#print (f"fraction: {frac}")
#print (f"whole: {int(whole)}")

#what if I want 0.6667? B = int(A) / 60, C = int(A) // 60  ... D = int(B) - int(C)




#day = int(Given_sec) // 60 

#if int(day) <= 1440 and int(day) >= 60: #hours condition
#    hr_a_min = int(Given_sec)/60 
#    a_Frac, a_whole = math.modf(hr_a_min)


Given_sec = input("Enter the seconds: ")


if int(Given_sec) > 86400:

    day_1f, day_1w = math.modf(float(Given_sec)/86400) #in day

    hour_1f, hour_1w = math.modf(day_1f * 24) #in hour 

    min_1f, min_1w = math.modf(hour_1f * 60) #in min

    sec_1w = min_1f * 60 #in sec

    print(f"{int(day_1w)} day, {int(hour_1w)} hours, {int(min_1w)} minutes and {math.ceil(sec_1w)} seconds")



if int(Given_sec) == 86400:

    print("1 day")



if int(Given_sec) < 86400:

    hour_2f, hour_2w = math.modf(float(Given_sec) / 3600) #in hour 

    min_2f, min_2w = math.modf(hour_2f * 60) #in min

    sec_2w = min_2f * 60 #in sec

    print(f"{int(hour_2w)} hours, {int(min_2w)} minutes and {math.ceil(sec_2w)} seconds")