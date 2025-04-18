def players_by_country_and_position(squads_list):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    players = [dict(zip(keys, player)) for player in squads_list]

    grouped = {}

    for player in players:
        country = player['country']
        position = player['position']

        if country not in grouped:
            grouped[country] = {}

        position_dict = grouped[country]

        if position not in position_dict:
            position_dict[position] = []

        position_dict[position].append(player)

    return grouped
