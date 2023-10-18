"""
Ingredient_Adjuster.py: Ask's user number of cookies they want to make. Calculates and displays each amount of ingredient needed to make the user's number of cookies.

By: V. Miranda-Calleja

Date: 10/25/2021
"""
#ask's user number of cookies they want to make
user_cookies = int(input("Enter number of cookies: "))

#Calculates and adjust's cookie recipe
divide_cookies = float(user_cookies) / 48

user_sugar = 1.5 * divide_cookies

user_butter = 1 * divide_cookies

user_flour = 2.75 * divide_cookies

#Displays new recipe
print("Cookie recipe for" , user_cookies , " cookies:")

print("Cups of sugar: " , user_sugar)

print("Cups of butter: " , user_butter)

print("Cups of flour: " , user_flour)
