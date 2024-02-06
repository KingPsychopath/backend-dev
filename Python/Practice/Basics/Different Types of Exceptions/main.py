def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return 'index is too high'
    except Exception as e:
        return e

# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
