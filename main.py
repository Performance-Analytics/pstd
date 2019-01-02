import userio

class load_sizes(object):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    SUPRAMAXIMAL = "supramaximal"

class fatigue_ratings(object):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "HIGH"

# TODO: Implement supramaximal load size functionality (targets grow with each
# use).

defaults = {
    "reps per set": 5,
    "inol targets": {
        load_sizes.SMALL: 0.375,
        load_sizes.MEDIUM: 0.5,
        load_sizes.LARGE: 0.75
    },
    "intensity targets": {
        load_sizes.SMALL: 0.6,
        load_sizes.MEDIUM: 0.7,
        load_sizes.LARGE: 0.8
    }
}

def inol(reps, intensity):
    return reps / (1 - intensity) / 100

class ParametricProgrammingGenerator(object):
    @staticmethod
    def generate_session(inol_targets=defaults["inol targets"],
                         intensity_targets=defaults["intensity targets"],
                         load_size=load_sizes.LARGE,
                         reps_per_set=defaults["reps per set"]):
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
        
        sets, extra_reps = calculate_set_quantity(reps_per_set,
                                                  intensity_targets[load_size],
                                                  inol_targets[load_size])
        
        session = TrainingSession()
        session.sets = sets
        session.reps_per_set = reps_per_set
        session.extra_reps = extra_reps
        session.intensity = intensity_targets[load_size]
        return session

    @staticmethod
    def determine_load_size(fatigue_rating,
                            previous_training_max,
                            current_training_max):
        if current_training_max > previous_training_max: # TM improved.
            if fatigue_rating == fatigue_ratings.LOW:
                return load_sizes.LARGE
            else:
                return load_sizes.MEDIUM
        else: # TM stagnated or regressed.
            if fatigue_rating == fatigue_ratings.LOW:
                return load_sizes.SUPRAMAXIMAL
            elif fatigue_rating == fatigue_ratings.MEDIUM:
                return load_sizes.MEDIUM
            else:
                return load_sizes.SMALL

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

# --------- The following is for demonstrative purposes. ---------

s1 = ParametricProgrammingGenerator.generate_session()
s1.training_max = 200
userio.print_training_session(s1)

s2_training_max = 210
s2_load_size = ParametricProgrammingGenerator.determine_load_size(
    load_sizes.MEDIUM,
    s1.training_max,
    s2_training_max
)
s2 = ParametricProgrammingGenerator.generate_session(
    load_size=s2_load_size
)
s2.training_max = s2_training_max
userio.print_training_session(s2)
