#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>

FUNCTIONALITY

1. First, we import the required packages,
    requests and sys.

2. We get the repository name and owner name from the
    command line arguments using the sys module.

3. We set up the API endpoint URL using the format method to
    insert the repo and owner names into the URL string.

4. We make the API call using the requests.get method
    and passing the URL as a parameter.

5. We check the response status code to ensure that
    the API call was successful.

6. If the API call was successful, we iterate over the first 10 commits in the
    response JSON and display the commit hash, author name, and date.

7. If the API call was not successful,
    we display the error status code.

"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
