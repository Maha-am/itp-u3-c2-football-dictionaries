from itertools import groupby
def players_by_position(squads_list):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    players = [dict(zip(keys, player)) for player in squads_list]
    sorted_player = sorted(players, key=lambda p: p['position'])
    grouped = {}
    for position, group in groupby(sorted_player, key=lambda p: p['position']):
        grouped[position] = list(group)
    return grouped


