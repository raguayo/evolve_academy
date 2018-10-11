import datetime;

current_age = int(raw_input("What is your current age?/n"));
#print(type(current_age));

now = datetime.datetime.now();
years_until_2035 = 2035 - now.year;
age_in_2035 = current_age + years_until_2035;
print("You will be " + str(age_in_2035) + " in the year 2035.");
