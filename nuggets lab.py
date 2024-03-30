#hard coded dict
denver_nuggets = {27:'Jamal Murray', 15:'Nikola Jokic', 50:'Aaron Gordon', 1:'Michael Porter Jr.', 5:'Kentavious Caldwell-Pope'}
#input jersy and name

new_number = input("Enter the new player's number:")
new_name = input("Enter the new player's new name:")

#add one more player to the nuggets
denver_nuggets [new_number] = new_name

#input number to look up
look_up = input("Enter a player number to look up:")
#output: player "wears" number
print(f'Denver Nuggets player {denver_nuggets[look_up]} wears #{look_up}')