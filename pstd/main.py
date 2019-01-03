import sessions
import userio

debug = False

if debug:
    userio.print_training_cycle_config(sessions.default_config)

def mainloop(config, debug=False):
    iterator = sessions.SessionBuilderCallbackIterator(config, debug)
    while True:
        session_builder = next(iterator)
        session = session_builder(userio.get_fatigue_rating(),
                                  userio.get_training_max())
        userio.print_training_session(session)

mainloop(sessions.default_config, debug)