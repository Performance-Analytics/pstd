import pickling
import sessions
import userio

debug = False

if debug:
    userio.print_training_cycle_config(sessions.default_config)

def mainloop(config, trainee_name, debug=False):
    iterator = pickling.load_state(trainee_name)
    if iterator is None:
        iterator = sessions.SessionBuilderCallbackIterator(config, debug)
    while True:
        session_builder = next(iterator)
        session = session_builder(userio.get_fatigue_rating(),
                                  userio.get_training_max())
        userio.print_training_session(session)
        pickling.save_state(iterator, trainee_name)

mainloop(sessions.default_config, "John Hancock", debug)