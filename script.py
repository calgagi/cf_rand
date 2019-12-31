#!/usr/bin/python3

# Codeforces Random Problem Getter
# Calvin Gagliano
# @calgagi

import os
import sys
import errno
import requests
import json
from random import randint

# Only used for API key and secret for Codeforces. May need in the future.
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
    print("Enter optional problem tags:")
    tags = []
    while True:
        q = input("Enter problem tag (or nothing to stop): ")
        if q == "":
            break
        tags.append(q)
    return tags


def get_problems(lower_bound, upper_bound):
    tags = get_tags()
    url = "https://codeforces.com/api/problemset.problems?tags="
    for tag in tags:
        url += tag + ";"
    if url[len(url)-1] == ';':
        url = url[:-1]
    res = requests.get(url).json()
    if res["status"] == "FAILED":
        print("Request returned with FAILED status. Exiting...")
        quit()
    problems = res["result"]["problems"]
    filtered_problems = []
    for i in range(len(problems)):
        if "rating" not in problems[i]:
            continue
        if problems[i]["rating"] >= lower_bound and problems[i]["rating"] <= upper_bound:
            filtered_problems.append(problems[i])
    return filtered_problems 


def random_problem(problems):
    idx = randint(0, len(problems)-1)
    return "\n" + problems[idx]["name"] + "\nURL: " + "https://codeforces.com/problemset/problem/" + str(problems[idx]["contestId"]) + "/" + problems[idx]["index"]


def main():
    # apiKey = get_api("key", False)
    # apiSecret = get_api("secret", False)
    print("Welcome to Codeforces Random Problem Getter")
    lower_bound = get_number("Enter lower difficulty bound (inclusive): ")
    upper_bound = get_number("Enter upper difficulty bound (inclusive): ")
    problems = get_problems(lower_bound, upper_bound)
    print("Press enter to get random problems, and input anything to quit.")
    while True:
        goagain = input("")
        if goagain != "":
            break
        print("==" + random_problem(problems))


main()
