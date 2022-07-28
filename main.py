from blessed import Terminal
t = Terminal()

# print(t.red("Red"))
# print(t.orange("Orange"))
# print(t.yellow("Yellow"))
# print(t.green("Green"))
#press a key, use the == "a"

#introductory paragraph explaining the quiz
print("Hello, and welcome to our quiz! You'll answer 5 questions and we'll tell you the color of your aura!")

# tried to make quiz start after key press ¯\_(ツ)_/¯

# start_key = input("Hello, and welcome to our quiz! You'll answer 5 questions and we'll tell you the color of your aura! Press the space bar when you're ready to start.")

# if start_key == " ":
#   asking_questions()
# if keyboard.is_pressed("enter"):
#   return "You pressed a key"

# DO THIS LATER!!!

'''Questions'''

# in order of white, yellow, red, blue, black

# def asking_questions():

# Favorite weather: Sunny (yellow), cloudy (white), rainy (blue), foggy (black), windy (red) 
Question_1 = "\nWhat is your favorite type of weather?\n\t1) Cloudy\n\t2) Sunny\n\t3) Windy\n\t4) Rainy\n\t5) Foggy\n"
print(Question_1)
input_1 = int(input("Type in the number only for your answer: "))

# Where you want to travel to: Paris (blue), Milan (white), Tokyo (red), Malibu (yellow), London (black)
Question_2 = "\nWhere to you want to travel to?\n\t1) Milan\n\t2) Malibu\n\t3) Tokyo\n\t4) Paris\n\t5) London\n"
print(Question_2)
input_2 = int(input("Type in the number only for your answer: "))


# Favorite color: Purple (blue), Green (white), Pink (red), Orange (yellow), Other (black)
Question_3 = "\nWhat is your favorite color?\n\t1) Green\n\t2) Orange\n\t3) Pink\n\t4) Purple\n\t5) Other\n"
print(Question_3)
input_3 = int(input("Type in the number only for your answer: "))


# Favorite book genre: Fantasy (yellow), Romance (white), Thriller (red), Non-fiction (black), YA (blue)
Question_4 = "\nWhat is your favorite book genre?\n\t1) Romance\n\t2) Fantasy\n\t3) Thriller\n\t4) Young Adult\n\t5) Non-fiction\n"
print(Question_4)
input_4 = int(input("Type in the number only for your answer: "))


# Favorite subject: STEM (yellow), Art & Music (red), English & Literature (white), Gym (blue), Business and Finance (black)
Question_5 = "\nWhat is your favorite subject?\n\t1) English & Literature\n\t2) STEM\n\t3) Art & Music\n\t4) Gym\n\t5) Business & Finance\n"
print(Question_5)
input_5 = int(input("Type in the number only for your answer: "))


'''Results'''
# print the result with a description

# White: 1-5; peaceful, calm, kind
# Yellow: 6-10; happy, energetic, optimistic
# Red: 11-15; passionate, confident, ambitious 
# Blue: 16-20; compassionate, imaginative, reliable
# Black: 21-25; serious, determined, mysterious
result_black = t.grey("\nYour aura is black! You are serious, determined, and mysterious.")
result_white = "\nYour aura is white! You are peaceful, calm, and kind."
result_yellow = t.yellow("\nYour aura is yellow! You are happy, energetic, and optimistic.") 
result_blue = t.blue("\nYour aura is blue! You are compassionate, imaginative, and reliable.")
result_red = t.red("\nYour aura is red! You are passionate, confident, and ambitious.")

# calculate results 
def calculate_results():
  total_points = input_1 + input_2 + input_3 + input_4 + input_5
  if total_points <= 5:
    #white
    return result_white
  elif total_points >= 6 and total_points <= 10:
    #yellow
    return result_yellow
  elif total_points >= 11 and total_points <= 15:
    #red
    return result_red
  elif total_points >=16 and total_points <= 20:
    #blue
    return result_blue
  elif total_points >= 21 and total_points <= 25:
    #black
    return result_black

print(calculate_results())
