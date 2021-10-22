"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 10 Oct 2021
Final Project
job seekers listing with output of seekers by location
"""

from seeker import Seeker


def get_user_id(input_file: str):
    '''given a whole number, make sure it isn't used already'''
    user_id_set = set()
    # pull user id's from seekers.txt
    file = open(input_file, "r")  # open seekers.txt for reading
    file_list = file.readlines()  # read the file, return list
    for line in file_list:
        # grab current id nums and add to user_id_set
        id = line[6:10]  # slice user id from line
        user_id_set.add(id)
    while True:
        try:
            user_id = int(input("Give an 4 digit ID number: "))
        except ValueError:
            print(f"Error: Oops, try again with numbers only and no decimals")
        if len(str(user_id)) == 4:
            if str(user_id) not in user_id_set:  # check id not in use
                user_id_set.add(str(user_id))
                print(f"success: your user ID is {user_id}")
                return user_id
            else:
                print("ID already in use. Try something different")
        else:
            print(f"Error: Oops, try again with a 4-digit number")


def add_seeker(output_file: str):
    '''given an output file, add seeker values to seekers.txt'''
    position = input("What position are you looking for? ")
    location = input("Where would you like to work? ")
    seeker = Seeker(get_user_id(output_file), position, location)
    listing = seeker.get_job_request(False)
    file = open(output_file, "a")  # open to append
    file.write("\n" + str(listing))  # write  to file
    print(f"Added. You're looking for {position} in {location} 😸")
    file.close()  # close file


def get_seekers(location: str, input_file: str, output_file="output.txt"):
    '''given a desired location and input data, write seekers to output.txt'''
    total_seekers = {"seekers": 0}
    file = open(input_file, "r")
    file_list = file.readlines()  # read the file, return list

    # write seekers to file
    out_file = open(output_file, "w")
    for line in file_list:
        if location.upper() in line.upper():
            out_file.write(line)  # write line to output.txt
            total_seekers["seekers"] += 1
    for k, v in total_seekers.items():
        out_file.write(f'Total {k} for {location}: {v}')
    print("Output file has been updated 😸")
    file.close()  # close file after writing

    # open file to verify if there were any seekers for location
    end_file = open(output_file, "r")
    end_file_list = end_file.readlines()  # read the file, return list
    if len(end_file_list) == 0:  # if no seekers
        end_file = open(output_file, "w")
        end_file.write("no job seekers for this location yet 😿")
    end_file.close()  # close file


if __name__:
    # instantiate  class
    person = Seeker(5432, "some job", "somewhere")

    add_seeker("seekers.txt")
    get_seekers(location="remote", input_file="seekers.txt")
