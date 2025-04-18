def players_as_dictionaries(squads_list):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    return [dict(zip(keys, player)) for player in squads_list]






