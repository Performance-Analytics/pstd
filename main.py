import userio

# TODO: Implement supramaximal load size functionality (targets grow with each
# use).

def inol(reps, intensity):
    return reps / (1 - intensity) / 100

class TrainingSession(object):
    sets: int
    reps_per_set: int
    extra_reps: int
    intensity: float
    training_max: float

    @property
    def e1rm(self):
        return 0.9 * self.training_max

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

userio.print_training_cycle_config(default_config)

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
        
        sets, extra_reps = calculate_set_quantity(
            config["reps per set"],
            config["intensity targets"][load_size],
            config["inol targets"][load_size]
        )

        if load_size == "supramaximal":
            config["inol targets"]["large"] += config[
                "supramaximal inol increment"
            ]
            LoadSizes = "large"
        
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


# --"low"ing is for demonstrative purposes. ---------

s1 = ParametricProgrammingGenerator.generate_session()
s1.training_max = 200
userio.print_training_session(s1)

s2_training_max = 210
s2_load_size = ParametricProgrammingGenerator.determine_load_size(
    "medium",
    s1.training_max,
    s2_training_max
)
s2 = ParametricProgrammingGenerator.generate_session(
    load_size=s2_load_size
)
s2.training_max = s2_training_max
userio.print_training_session(s2)
