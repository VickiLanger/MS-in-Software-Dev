"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 14 Oct 2021
Final Project
job seekers class module
"""

# TODO: 1 mangled and 2 public self attributes
# TODO: 1 mangled and 1 public method that take arguments and return values
# TODO: magic redefined method


class Seeker():
    '''a class to represent a job seeker'''

    def __init__(self, user_id, desired_position, desired_location="any",
                 open_to_work="True"):
        '''build constructor with attributes for seeker object'''
        self.id = user_id
        self.position = desired_position
        self.location = desired_location
        self.__available = True  # private name mangled attribute

    def __repr__(self):
        '''representation of Seeker class'''
        return (f'{self.__class__.__name__}('
                f'{self.id}, {self.position}, {self.location})')

    def __str__(self):
        '''output for end user'''
        return (f'user# {self.id} is looking for {self.position} in {self.location}')

    def __get_seeker_info(self):  # getter / private method
        '''tbd'''
        return self.id, self.position, self.location  # returns a tuple

    def __get_availability(self, open_to_work: bool):
        '''given boolean, return seeker listing with willingness to move'''
        if open_to_work is True:
            openness = " (currently open to work)"
        else:
            openness = " (not open to work)"
        availability = openness
        return availability

    def get_job_request(self, willing_to_relocate: bool):
        '''given boolean, return seeker listing with willingness to move'''
        if willing_to_relocate is True:
            relocation = " (willing to move? Yes)"
        else:
            relocation = " (willing to move? No)"
        seeker_listing = (self.__str__()
                          + relocation
                          + self.__get_availability(True))
        return seeker_listing


if __name__:
    # instantiate seeker object
    person_one = Seeker(3452, "technical support engineer", "remote")
    person_two = Seeker(8702, "business analyst", "houston")
    seeker_listing = person_one.get_job_request(False)

    # Assert tests

    # Testing magic method

    # print("Seeker Class Tests Passed")
