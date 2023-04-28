from art.view import login as login_view
from art.model.jira import jira_authenticator


class Login:
    def __init__(self, window=None):
        self.login_view = login_view.Login(window)
        self.core_id = ''
        self.password = ''
        self.project_url = ''
        self.jira_connection = None
        self.zephyr_connection = None
        self.jira_authenticator = None

    def check_inputs(self):
        self.core_id = self.login_view.get_core_id()
        self.password = self.login_view.get_password()
        self.project_url = self.login_view.get_project_url()
        if self.core_id == '' or self.password == '' or self.project_url == '':
            self.login_view.change_message('Core ID, Password, and Project URL can\'t be empty!', '#FEC6BB')
            return False
        return True

    def check_jira_authentication(self):
        if self.check_inputs():
            self.jira_authenticator = jira_authenticator.JiraAuthenticator(self.project_url)
            self.jira_connection = self.jira_authenticator.authenticate_with_jira(self.core_id, self.password)
            self.zephyr_connection = self.jira_authenticator.authenticate_with_zephyr()
            if self.jira_connection and self.zephyr_connection:
                self.login_view.change_message('User successfully autenticated!\nPlease wait a few seconds...',
                                               '#FFFFFF')
            else:
                self.login_view.change_message('Invalid core ID or password!', '#FFFFFF')
        return self.jira_connection, self.zephyr_connection
