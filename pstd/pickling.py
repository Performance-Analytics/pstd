import pickle

def load_state(trainee_name, training_cycle_id=""):
    try:
        with open(
            "{} - {}.pickle".format(trainee_name, training_cycle_id),
            "rb"
        ) as file:
            return pickle.load(file)
    except FileNotFoundError:
        return False

def save_state(iter, trainee_name, training_cycle_id=""):
    with open(
        "{}{}.pickle".format(trainee_name, training_cycle_id),
        "wb"
    ) as file:
        pickle.dump(iter, file)