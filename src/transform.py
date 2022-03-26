"""Issues data parser."""

import pickle
from typing import Dict, List
from src.core.config import settings


def transform():
    """Transform issues raw data into readable structure for our analysis.
    """
    issues: List[Dict] = []
    #Read raw data
    with open(settings.RAW_DATA_FILE_PATH, 'rb') as f:
        raw_issues: List[Dict] = pickle.load(f)

    for raw_issue in raw_issues:
        # flatten labels as list of str instead of list of dict
        labels: List[str] = []
        for raw_label in raw_issue['labels']:
            labels.append(raw_label['name'])
        # create parsed issue dict
        issue = {
            'id': raw_issue['id'],
            'title': raw_issue['title'],
            'user': raw_issue['user']['login'],
            'user': raw_issue['user']['login'],
            'comments': raw_issue['comments'],
            'state': raw_issue['state'],
            'labels': labels,
            'created_at': raw_issue['created_at'],
            'updated_at': raw_issue['updated_at'],
            'closed_at': raw_issue['closed_at']
        }
        issues.append(issue)

    # saved transformed data
    with open(settings.DATA_FILE_PATH, 'wb') as f:
        pickle.dump(issues, f, protocol=pickle.HIGHEST_PROTOCOL)
    print('Done!')
    return issues

if __name__ == '__main__':
    transform()