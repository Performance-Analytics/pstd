import userio

class TrainingSession(object):
    sets: int
    reps_per_set: int
    extra_reps: int
    intensity: float
    training_max: float

    @property
    def e1rm(self):
        return self.training_max / 0.9

    @property
    def load(self):
        return self.intensity * self.e1rm

default_config = {
    "reps per set": 5,
    "inol targets": {
        "small": 0.375,
        "medium": 0.5,
        "large": 0.75
    },
    "intensity targets": {
        "small": 0.6,
        "medium": 0.7,
        "large": 0.8
    },
    "supramaximal inol increment": 0.1
}

class ParametricProgrammingGenerator(object):
    @staticmethod
    def generate_session(config=default_config,
                         load_size="large"):
        def calculate_set_quantity(reps_per_set, intensity, inol):
            """
            Calculates the sets required to accomplish the work desired.

            `extra_reps` is how many repetitions are left over after the
            calculated number of flat (specified repetition quantity) sets. For
            instance, if the user needs to complete 18 repetitions in sets of
            5, `extra_reps` will be 3.

            Returns a tuple comprising `(sets, extra_reps)`.
            """
            total_reps = round(inol * 100 * (1 - intensity))

            extra_reps = round(total_reps % reps_per_set)
            sets = (total_reps - extra_reps) / reps_per_set
            return sets, extra_reps
        
        if load_size == "supramaximal":
            config["inol targets"]["large"] += config[
                "supramaximal inol increment"
            ]
            load_size = "large"

        sets, extra_reps = calculate_set_quantity(
            config["reps per set"],
            config["intensity targets"][load_size],
            config["inol targets"][load_size]
        )
        
        session = TrainingSession()
        session.sets = sets
        session.reps_per_set = config["reps per set"]
        session.extra_reps = extra_reps
        session.intensity = config["intensity targets"][load_size]
        return session

    @staticmethod
    def determine_load_size(fatigue_rating,
                            previous_training_max,
                            current_training_max):
        if current_training_max > previous_training_max: # TM improved.
            if fatigue_rating == "low":
                return "large"
            else:
                return "medium"
        else: # TM stagnated or regressed.
            if fatigue_rating == "low":
                return "supramaximal"
            elif fatigue_rating == "medium":
                return "medium"
            else:
                return "small"


# --------- The following is for demonstrative purposes. ---------

userio.print_training_cycle_config(default_config)

def mainloop(config):
    training_max_previous = 0
    while True:
        fatigue_rating = userio.get_fatigue_rating()
        training_max_current = userio.get_training_max()
        load_size = ParametricProgrammingGenerator.determine_load_size(
            fatigue_rating,
            training_max_previous,
            training_max_current
        )
        session = ParametricProgrammingGenerator.generate_session(
            config=config,
            load_size=load_size
        )
        session.training_max = training_max_current
        userio.print_training_session(session)
        training_max_previous = training_max_current

mainloop(default_config)