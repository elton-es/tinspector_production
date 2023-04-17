from jira import JIRA, JIRAError


class JiraAutenticator:
    def __init__(self):
        self.dalek_connection = None
        self.idart_connection = None

    def autenticate_with_dalek(self, core_id, password):
        try:
            self.dalek_connection = JIRA(server='https://dalek.mot.com', basic_auth=(core_id, password))
            return self.dalek_connection
        except JIRAError as e:
            print('Invalid core ID or password\n' + str(e))
            return None
        except Exception as e:
            print('Unable to connect to jira, please check your VPN connection' + str(e))
            return None

    def autenticate_with_idart(self, core_id, password):
        try:
            self.idart_connection = JIRA(server='https://idart.mot.com', basic_auth=(core_id, password))
            return self.idart_connection
        except JIRAError as e:
            print('Invalid core ID or password\n' + str(e))
            return None
        except Exception as e:
            print('Unable to connect to jira, please check your VPN connection' + str(e))
            return None
