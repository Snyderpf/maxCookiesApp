import sys
from datetime import datetime


def set_command():
    print(f"Command: {sys.argv[0]}  <csv_file> -d \"yyyy-mm-dd\"")


def get_input():
    # accessing through index
    if len(sys.argv) != 4 or sys.argv[2] != "-d":
        set_command()
        sys.exit()


def get_time(times):
    update_time = times.strftime("%Y-%m-%d")
    return update_time


def main():
    get_input()
    # mapping cookies count to appearance in csv file
    cookies_map = {}

    with open(sys.argv[1], "r") as csv_file:
        date_time_input = datetime.strptime(sys.argv[3], "%Y-%m-%d")
        # reading csv line by line
        for line in csv_file.readlines():
            cookie, time_stamp = line.split(",")
            time_stamp = time_stamp.replace("\n", "")

            # converting date to object
            up_keeping_time = datetime.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S%z")

            # checking if cookie already in map
            if get_time(date_time_input) == get_time(up_keeping_time):
                # updating cookies value
                if cookie in cookies_map:
                    cookies_map[cookie] += 1
                else:
                    # assigning first appearance to one
                    cookies_map[cookie] = 1

    # getting the most_active of the values in the cookies_map
    most_active_cookies = max(cookies_map.values(), key=lambda x: x)

    # print all the values that are equal to most_active
    for cookies, appearing in cookies_map.items():
        if appearing == most_active_cookies:
            print(cookies)


if __name__ == "__main__":
    main()
