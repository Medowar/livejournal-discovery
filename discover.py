import gzip
import re
import requests
import string
import sys
import time
import random
import os

class FetchError(Exception):
    '''Custom error class when fetching does not meet our expectation.'''

def main():
    # Take the program arguments given to this script
    # Normal programs use 'argparse' but this keeps things simple
    item_value = sys.argv[1]
    item_type = sys.argv[2]
    output_filename = sys.argv[3]  # this should be something like myfile.txt.gz
    start_num, end_num = item_value.split('-')

    if item_type == "profiles":
        profiles = []
        for profileid in range(int(start_num), int(end_num) + 1):
            status_code = str(check_200('http://www.livejournal.com/profile?userid='+str(profileid)))
            print('Received status code ' + status_code + ' for profile ' + str(profileid) + '.')
            sys.stdout.flush()
            profiles.append(status_code)

        with open(output_filename, 'w') as file:
            file.write('\n'.join(profiles))

def check_200(url):
    tries = 0
    while tries <= 5:
        response = requests.get(url)
        status_code = response.status_code
        if response.status_code not in (200, 404, 410):
            tries += 1
        else:
            return status_code
    return status_code

if __name__ == '__main__':
    main()

