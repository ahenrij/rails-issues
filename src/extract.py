"""Issues data extractor."""

import time
import http
import math
import json
import pickle
import requests
from src.core.config import settings


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
    url = f"{settings.BASE_URL}/repos/{owner}/{repo}/issues"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {settings.GITHUB_OAUTH_TOKEN}'
    }
    # nb of pages to request
    pages = math.ceil(nb/RESULTS_PER_PAGE)
    # results array.
    issues = []

    for page in range(1, pages+1):
        params = {
            'per_page': RESULTS_PER_PAGE,
            'page': page
        }
        time.sleep(1)
        result = requests.get(url, headers=headers, params=params)
        # raise exception on result error
        if result.status_code != http.HTTPStatus.OK:
            print(result.text)
            result.raise_for_status()
        # concatenate response content to issues
        res = json.loads(result.text)
        print(f"Downloaded {len(res)} on page {page}")
        issues += res
    
    with open(settings.RAW_DATA_FILE_PATH, 'wb') as f:
        pickle.dump(issues, f, protocol=pickle.HIGHEST_PROTOCOL)
    print('Done!')
    return issues


if __name__ == '__main__':
    extract()