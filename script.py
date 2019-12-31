#!/usr/bin/python3

# Codeforces Random Problem
# Calvin Gagliano
# @calgagi

import os
import sys
import errno

def get_api(item, force_get):
    res = ""
    home = os.path.expanduser("~")
    filepath = home + "/.codeforces_random_problem/" + item + ".txt"
    if not os.path.exists(home + "/.codeforces_random_problem"):
        try:
            os.makedir(home + "/.codeforces_random_problem")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    if not os.path.exists(filepath) or force_get == True:
        print("It appears that you don't have an API " + item + ". Please go to codeforces.com/settings/api to generate or copy yours.")
        res = input("Please enter your API " + item + " for Codeforces: ")
        file_obj = open(filepath, "w")
        file_obj.write(res)
        file_obj.close()
    else:
        file_obj = open(filepath, "r")
        res = file_obj.read()
        file_obj.close()
    return res


def get_number(query):
    res = input(query)
    while True:
        try:
            res = int(res)
            # Check if it is valid difficulty (multiple of 100)
            if (res % 10) != 0 or ((res / 10) % 10 != 0):
                raise Exception
            break
        except:
            res = input("Not a valid number. Make sure it is a multiple of 100. " + query)
    return res

        
def get_tags():
    tags = []
    lower_bound = get_number("Enter lower difficulty bound (inclusive): ")
    upper_bound = get_number("Enter upper difficulty bound (inclusive): ")
    for tag in range(lower_bound, upper_bound+1, 100):
        tags.append(str(tag))
    while True:
        q = input("Enter another tag (or $ to stop): ")
        if q == "$":
            break
        tags.append(q)
    return tags


def query_for_problems(key, secret, tags):
    print("Querying for problems...")
    # TODO

        
def main():
    apiKey = get_api("key", False)
    apiSecret = get_api("secret", False)
    # TODO: Test API key + secrets
    tags = get_tags()
    problems = query_for_problems(key, secret, tags)

main()
