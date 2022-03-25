"""Issues data extractor."""

import requests
import pickle
import http
import math
import json

EXPORT_FILE_PATH = 'data/raw_data.pickle'
BASE_URL = "https://api.github.com"
RESULTS_PER_PAGE = 100 # max value allowed


def extract(owner:str="rails", repo:str="rails", nb:int=500) -> list:
    """Extract latest issues from a public github repository.
    
    Params
    ======
        `owner` (str): Repository owner's name. Defaults to "rails".
        `repo` (str): Repository's name. Defaults to "rails".
        `nb` (int): Number of latest issues number to extract.

    Returns
    =======
        (list): List of JSON representation of the latest `limit` issues on `owner`/`rails` project.
    """
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    headers = {'accept': 'application/vnd.github.v3+json'}
    # nb of pages to request
    pages = math.ceil(nb/RESULTS_PER_PAGE)
    # results array.
    issues = []

    for page in range(1, pages+1):
        query = {
            'per_page': RESULTS_PER_PAGE,
            'page': page
        }
        result = requests.get(url, headers=headers, data=json.dumps(query))
        # raise exception on result error
        if result.status_code != http.HTTPStatus.OK:
            result.raise_for_status()
        # append response content to issues
        issues.append(json.loads(result.text))
    
    with open(EXPORT_FILE_PATH, 'wb') as f:
        pickle.dump(issues, f, protocol=pickle.HIGHEST_PROTOCOL)
    return issues


if __name__ == '__main__':
    extract(nb=600)