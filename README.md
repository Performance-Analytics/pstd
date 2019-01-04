# PSTD

Procedural Strength Training Director

PSTD is based upon Mike Tuchscherer's daily training max practice as well as
[this gist](https://gist.github.com/kvazau/456e903c01bb977a898f3d177ea3988c).

## Usage

Each training cycle is applicable to only one exercise. PSTD includes a
default training cycle configuration in `main.py`. Simply execute
`python3 main.py`, report your subjective fatigue rating as prompted, and work
up to and report an RPE 8 (2 repetitions left in reserve) single repetition of
the exercise.

PSTD will respond with an according volume and load prescription. The volume
notation used is `AxB, C` where `A` is the quantity of sets, `B` is the
quantity of repetitions per set, and `C` is the quantity of extra repetitions
to be completed afterward.

The program will then prompt again for the next training session's information.
`main.py` automatically saves and loads training data in the local directory so
that the user can exit the application without worrying about losing data.

## Acknowledgements

* [Gavin Frazar](https://github.com/gavinfrazar)