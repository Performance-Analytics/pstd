def print_training_session(session):
    volume_notation = "{}x{}".format(int(session.sets),
                                     int(session.reps_per_set))
    if session.extra_reps > 0:
        volume_notation += ", {}".format(session.extra_reps)

    print("Training Max: {}".format(session.training_max))
    print("E1RM: {}".format(session.e1rm))
    print("Intensity Used: {:.2%}".format(session.intensity))
    print("Volume: {}".format(volume_notation))
    print("Load Used: {}".format(session.load))
    print()