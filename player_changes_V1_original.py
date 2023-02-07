# Imagine a sports team during a game. Only 3 changes are allowed.
# - declare a list with 5 players on the field
# - declare a list with 5 players on the bench
# - declare an empy list which will collect the players removed from the field
# - declare a variable for the changes made (can be any value since you will update it for every run)
# - MAX_CHANGES will be a constant with a value of 3
#
# If the player X is on the field and there are enough changes left:
# 	- The replacement takes place if the player Y is on the bench and cannot be found on the field
# 	- Player X will then be removed from the field and added to the players' removed list
# 	- Player Y will then be added on the field and removed from the bench
# 	- The program prints: "X was replaced by Y on the field. There are N changes left"
# Else if the player we want to replace is not on the field:
# 	- The program prints: "the replacement cannot take place because X is not on the field"
# Else, the program prints: "no more changes left"

players_on_the_field = ['John', 'Tony', 'Alex', 'Greg', 'Bob']
players_on_the_bench = ['Kevin', 'Frank', 'Will', 'Ryan', 'Joe']
players_removed = []
changes_made = 1
MAX_CHANGES = 3

removed_player = input('Choose a player to replace: \n')
added_player = input('Choose a player from the bench: \n')
changes_left = MAX_CHANGES - changes_made

if removed_player in players_on_the_field and added_player in players_on_the_bench and changes_made <= MAX_CHANGES:
    players_on_the_field.remove(removed_player)
    players_on_the_bench.remove(added_player)
    players_removed.append(removed_player)
    players_on_the_field.append(added_player)

    print(f'{added_player} has replaced {removed_player} on the field. There are {changes_left} changes left.')
    print(f'Current players on the field: {players_on_the_field}')
    print(f'Current players on the bench: {players_on_the_bench}')
    print(f'Current players removed: {players_removed}')

elif removed_player not in players_on_the_field and added_player not in players_on_the_bench:
    print(f'The change cannot be fulfilled because the player [{removed_player}] is not on the field and player [{added_player}] is not on the bench')
elif removed_player not in players_on_the_field:
    print(f'The change cannot be fulfilled because the player {removed_player} is not on the field.')
elif added_player not in players_on_the_bench:
    print(f'The change cannot be fulfilled because the player {added_player} is not on the bench.')
else:
    print(f'The limit of changes has been reached.')