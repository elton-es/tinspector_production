from jira import JIRA, JIRAError
from zephyr import ZephyrScale
from pathlib import Path


class JiraAuthenticator:
    def __init__(self, project_url):
        self.project_url = project_url
        self.jira_authentication = None
        self.zephyr_authentication = None

    def authenticate_with_jira(self, core_id, password):
        try:
            self.jira_authentication = JIRA(server=self.project_url, basic_auth=(core_id, password))
            return self.jira_authentication
        except JIRAError as e:
            print('Invalid core ID or password\n' + str(e))
            return None
        except Exception as e:
            print('Unable to connect to jira, please check your VPN connection' + str(e))
            return None

    def authenticate_with_zephyr(self):
        try:
            path = Path(__file__).parent / './../../resources/secret.txt'
            with path.open() as f:
                token = f.readline()
                self.zephyr_authentication = ZephyrScale(token=token)
                return self.zephyr_authentication
        except Exception as e:
            print('Unable to connect to Zephyr' + str(e))
            return None
