player_name= input("What is your player name?")
player_name= player_name.rstrip();

#Getting into the use of questions

print("Welcome "+player_name)
print("How are you?")

string_looks_like_num = input("What is your height "+player_name+"?")
height = int(string_looks_like_num)

#print(string_looks_like_num+2) Will not work

print(height+2)