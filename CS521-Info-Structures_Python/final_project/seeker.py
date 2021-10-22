"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 14 Oct 2021
Final Project
job seekers class module
"""


class Seeker():
    '''a class to represent a job seeker'''

    def __init__(self, user_id, desired_position, desired_location="any",
                 __available="True"):
        '''build constructor with attributes for seeker object'''
        self.id = user_id
        self.position = desired_position
        self.location = desired_location
        self.__available = True  # private name mangled attribute

    def __repr__(self):
        '''representation of Seeker class'''
        return (f'{self.__class__.__name__}('
                f'{self.id}, {self.position}, {self.location})')

    def __get_seeker_info(self):  # getter / private method
        '''return Seeker ID#, position, and location'''
        return self.id, self.position, self.location  # returns a tuple

    def __str__(self):
        '''output for end user'''
        info = self.__get_seeker_info()
        return (f'user# {info[0]} is looking for {info[1]} in {info[2]}')

    def __get_availability(self, open_to_work: bool):  # private method
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

    def _update_desired_position(self, desired_position: str):
        '''given a desired position, update desired position'''
        self.position = desired_position
        return (f'user# {self.id} desired position updated')

    def __add__(self, additional_location: str):
        '''given an additional location, add location to seeker object'''
        location = self.location
        new_location = location[:]
        new_location = new_location + " and " + additional_location
        return Seeker(self.id, self.position, new_location)


if __name__:
    # instantiate seeker object
    person_one = Seeker(3452, "technical support engineer", "remote")
    person_two = Seeker(8702, "business analyst", "houston")
    seeker_listing = person_one.get_job_request(False)

    # Assert tests
    start_position = person_one.position
    new_position = "fake job title"
    person_one._update_desired_position(new_position)
    assert person_one.position == new_position, 'Position not updated'

    # Testing magic method
    start_location = person_two.location
    new_location = "fake location"
    person_two = person_two + new_location
    print(person_two)
    assert new_location in person_two.location, 'Location not updated'

    print("Seeker Class Tests Passed")
