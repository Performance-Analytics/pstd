import pstd.pickling, pstd.sessions, pstd.userio

debug = False

if debug:
    pstd.userio.print_training_cycle_config(pstd.sessions.default_config)

def mainloop(config, trainee_name, debug=False):
    iterator = pstd.pickling.load_state(trainee_name)
    if iterator is None:
        iterator = pstd.sessions.SessionBuilderCallbackIterator(config, debug)
    while True:
        session_builder = next(iterator)
        session = session_builder(pstd.userio.get_fatigue_rating(),
                                  pstd.userio.get_training_max())
        pstd.userio.print_training_session(session)
        pstd.pickling.save_state(iterator, trainee_name)

mainloop(pstd.sessions.default_config, "John Hancock", debug)