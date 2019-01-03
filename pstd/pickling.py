import pickle

def load_state(trainee_name, training_cycle_id=""):
    try:
        return pickle.load(open(
            "{} - {}.pickle".format(trainee_name, training_cycle_id),
            "rb"
        ))
    except FileNotFoundError:
        return False

def save_state(iter, trainee_name, training_cycle_id=""):
    pickle.dump(iter, open(
        "{} - {}.pickle".format(trainee_name, training_cycle_id),
        "wb"
    ))