players_on_the_field = ['John', 'Tony', 'Alex', 'Greg', 'Bob']
players_on_the_bench = ['Kevin', 'Frank', 'Will', 'Ryan', 'Joe']
players_removed = []
changes_made = 0
MAX_CHANGES = 3

changes_at_a_time = input('How many players you wish to replace at a time? 1 or 2? \n')

if changes_at_a_time == '1':
    changes_at_a_time = int(changes_at_a_time)
    while len(players_removed) < MAX_CHANGES:
        removed_player1 = input('Choose one player to replace: \n')
        added_player1 = input('Choose one player from the bench: \n')

        if removed_player1 in players_on_the_field and added_player1 in players_on_the_bench:
            players_on_the_field.remove(removed_player1)
            players_on_the_bench.remove(added_player1)
            players_removed.append(removed_player1)
            players_on_the_field.append(added_player1)

            changes_made += 1
            changes_left = MAX_CHANGES - changes_made

            print(f'[{added_player1}] has replaced [{removed_player1}] on the field. There are [{changes_left}] changes left.')
            print(f'Current players on the field: {players_on_the_field}')
            print(f'Current players on the bench: {players_on_the_bench}')
            print(f'Current players removed: {players_removed}')

        elif removed_player1 not in players_on_the_field and added_player1 not in players_on_the_bench:
            print(f'The change cannot be fulfilled because the player [{removed_player1}] is not on the field\nand player [{added_player1}] is not on the bench')
        elif removed_player1 not in players_on_the_field:
            print(f'The change cannot be fulfilled because the player [{removed_player1}] is not on the field.')
        elif added_player1 not in players_on_the_bench:
            print(f'The change cannot be fulfilled because the player [{added_player1}] is not on the bench.')
        else:
            print(f'The limit of changes has been reached.')

elif changes_at_a_time == '2':
    changes_at_a_time = int(changes_at_a_time)
    while len(players_removed) < MAX_CHANGES:
        removed_player1 = input('Choose the first player to replace: \n')
        removed_player2 = input('Choose the second player to replace: \n')
        added_player1 = input('Choose the first player from the bench: \n')
        added_player2 = input('Choose the second from the bench: \n')

        if removed_player1 in players_on_the_field and added_player1 in players_on_the_bench and removed_player2 in players_on_the_field and added_player2 in players_on_the_bench:
            players_on_the_field.remove(removed_player1)
            players_on_the_bench.remove(added_player1)
            players_removed.append(removed_player1)
            players_on_the_field.append(added_player1)

            players_on_the_field.remove(removed_player2)
            players_on_the_bench.remove(added_player2)
            players_removed.append(removed_player2)
            players_on_the_field.append(added_player2)

            changes_made += 2
            changes_left = MAX_CHANGES - changes_made

            print(f'[{added_player1}] and [{added_player2}] have replaced [{removed_player1}] and [{removed_player2}] on the field. There are [{changes_left}] changes left.')
            print(f'Current players on the field: {players_on_the_field}')
            print(f'Current players on the bench: {players_on_the_bench}')
            print(f'Current players removed: {players_removed}')

        elif removed_player1 not in players_on_the_field and added_player1 not in players_on_the_bench or removed_player2 not in players_on_the_field and added_player2 not in players_on_the_bench:
            print(f'The change cannot be fulfilled because either [{removed_player1}] or [{removed_player2}] is not on the field\nand [{added_player1}] or [{added_player2}] is not on the bench')
        elif removed_player1 or removed_player2 not in players_on_the_field:
            print(f'The change cannot be fulfilled because [{removed_player1}] or [{removed_player2}] is not on the field.')
        elif added_player1 or added_player2 not in players_on_the_bench:
            print(f'The change cannot be fulfilled because [{added_player1}] or [{added_player2}] is not on the bench.')
        else:
            print(f'The limit of changes has been reached.')

else:
    print('Only the following numbers can be selected: 1 or 2. Please re-run the program and try again!')