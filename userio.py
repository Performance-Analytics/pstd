def print_training_cycle_config(config):
    for key in config:
        print("{}: {}".format(key, config[key]))
    print()

def print_training_session(session):
    volume_notation = "{}x{}".format(int(session.sets),
                                     int(session.reps_per_set))
    if session.extra_reps > 0:
        volume_notation += ", {}".format(session.extra_reps)

    print("Training Max:", session.training_max)
    print("E1RM:", session.e1rm)
    print("Intensity Used: {:.2%}".format(session.intensity))
    print("Volume:", volume_notation)
    print("Load Used:", session.load)
    print()

def get_fatigue_rating():
    while True:
        fr = input("Subjective Fatigue Rating [low/medium/high]: ")
        if fr in ["low", "medium", "high"]:
            print()
        return fr

def get_training_max():
    tm = float(input("Training Max: "))
    print()
    return tm
