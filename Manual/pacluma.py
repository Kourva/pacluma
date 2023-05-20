#!/usr/bin/env python3

# Libraries
import sys, os


# Function to check root access
def check_root():
    return not os.geteuid()


# Main function
def main_func():
    # Taking arguments
    queries = " ".join(sys.argv[1:])

    # Getting Pacman search result and store it in temporary file in /tmp
    os.system(f"sudo pacman -Ss {queries} > /tmp/pacluma_history")
    with open("/tmp/pacluma_history") as output_file:
        search_results = output_file.readlines()

    # Creating copy of result for editing
    temp_result = list()

    # Splitting the title and description
    cleaned_results = list()
    for i in range(0, len(search_results), 2):
        cleaned_results.append(
            (search_results[i].split("\n")[0], search_results[i + 1].strip())
        )

    # Making Search form
    form = "{0}\n    {1}\n\n"

    # Beautifying output
    for title, decription in cleaned_results:
        # Making output darker if the package is installed
        if "installed" in title:
            temp_result.append(
                form.format(
                    "\033[2;37;40m" + title,
                    decription + "\033[m",
                )
            )

        # Making the repo name 'red' and others white
        else:
            title_repo, title_name = title.split("/")
            colortitle = "\033[1;31;40m" + title_repo + "\033[m" + "/" + title_name
            temp_result.append(form.format(colortitle, decription))

    # Printing final result
    print(*temp_result, end="\n")
    os.remove("/tmp/pacluma_history")


# Run the main function
if __name__ == "__main__" and check_root():
    main_func()

# Raise error if script is not running by root
else:
    raise sys.exit("error: you cannot perform this operation unless you are root.")
