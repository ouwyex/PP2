import pickle

def serialize_game(state):
    return pickle.dumps(state)

def deserialize_game(state_bytes):
    return pickle.loads(state_bytes)

def get_level_data(level):
    levels = {
        1: {"speed": 10, "walls": []},
        2: {"speed": 15, "walls": [(100, 100, 20, 300)]},
        3: {"speed": 20, "walls": [(150, 150, 300, 20), (300, 200, 20, 200)]}
    }
    return levels.get(level, levels[1])
