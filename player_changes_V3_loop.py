players_on_the_field = ['John', 'Tony', 'Alex', 'Greg', 'Bob']
players_on_the_bench = ['Kevin', 'Frank', 'Will', 'Ryan', 'Joe']
players_removed = []
changes_made = 0
MAX_CHANGES = 3

while len(players_removed) < MAX_CHANGES:
    removed_player = input('Choose a player to replace: \n')
    added_player = input('Choose a player from the bench: \n')

    if removed_player in players_on_the_field and added_player in players_on_the_bench:
        players_on_the_field.remove(removed_player)
        players_on_the_bench.remove(added_player)
        players_removed.append(removed_player)
        players_on_the_field.append(added_player)

        changes_made += 1
        changes_left = MAX_CHANGES - changes_made

        print(f'[{added_player}] has replaced [{removed_player}] on the field. There are [{changes_left}] changes left.')
        print(f'Current players on the field: {players_on_the_field}')
        print(f'Current players on the bench: {players_on_the_bench}')
        print(f'Current players removed: {players_removed}')

    elif removed_player not in players_on_the_field and added_player not in players_on_the_bench:
        print(f'The change cannot be fulfilled because the player [{removed_player}] is not on the field and player [{added_player}] is not on the bench')
    elif removed_player not in players_on_the_field:
        print(f'The change cannot be fulfilled because the player [{removed_player}] is not on the field.')
    elif added_player not in players_on_the_bench:
        print(f'The change cannot be fulfilled because the player [{added_player}] is not on the bench.')
    else:
        print(f'The limit of changes has been reached.')