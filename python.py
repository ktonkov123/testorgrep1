import requests

from requests import Response

from jira import auth
from config import default_jira_user_email, default_jira_site, default_descriptor

PATH = '/rest/plugins/1.0/'

params: dict = {'os_authType': 'basic'}


def get_upm_token(email: str = default_jira_user_email(), jira_site: str = default_jira_site()) -> str:
    res: Response = requests.get(jira_site + PATH,
                                 params={'os_authType': 'basic'},
                                 headers={'Authorization': auth.basic(email),
                                          'Accept': 'application/vnd.atl.plugins.installed+json'})
    return res.headers['upm-token']




if __name__ == '__main__':
    print(get_upm_token())
