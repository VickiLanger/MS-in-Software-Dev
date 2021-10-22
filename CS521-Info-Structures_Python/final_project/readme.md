## Seekers

### Purpose
This module implements a basic reverse job board. Job seekers can add to the seeker listing. Recruiters and hirers can search the listing for available seekers.

A Seeker instance can be constructed from a 4-digit user id, desired position, and desired location.
```python
Seeker(5432, "some job", "somewhere")  # example constructor
```

### Running the Code
Run `main.py` via the terminal. You will be prompted to enter a 4-digit user id, a position, then a location. Once you have entered these, they will be added to `seekers.txt`. 

After the seekers file has been populated, `output.txt` will be populated based on the location `"remote"`. If you would like to search for other locations, you are welcome to.
```python
# example call for seekers in a different location
get_seekers(location="raleIgh", input_file="seekers.txt")
```

### Required 3rd party Modules
None. No need to install anything extra.

