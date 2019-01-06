import errno, os, pickle

storage_path = "training_cycles"

def load_state(trainee_name, training_cycle_id=""):
    try:
        with open(
            "{}/{}{}.pickle".format(storage_path,
                                   trainee_name,
                                   training_cycle_id),
            "rb"
        ) as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

def save_state(iter, trainee_name, training_cycle_id=""):
    try: # Try to create directory to store training cycle.
        os.makedirs(storage_path)
    except OSError as e:
        # If error is not that the directory already exists...
        if e.errno != errno.EEXIST:
            raise
        # Else, carry on as if nothing happened.
    with open(
        "{}/{}{}.pickle".format(storage_path, trainee_name, training_cycle_id),
        "wb"
    ) as file:
        pickle.dump(iter, file)