from cycle_review_tool.view import login as login_view
from cycle_review_tool.model.jira import jira_autenticator


class Login:
    def __init__(self, window=None):
        self.login_view = login_view.Login(window)
        self.core_id = ''
        self.password = ''
        self.dalek_connection = None
        self.idart_connection = None
        self.jira_autenticator = jira_autenticator.JiraAutenticator()

    def check_inputs(self):
        self.core_id = self.login_view.get_core_id()
        self.password = self.login_view.get_password()
        if self.core_id == '' or self.password == '':
            self.login_view.change_message('Core ID and Password can\'t be empty!', '#FEC6BB')
            return False
        return True

    def check_dalek_autentication(self):
        if self.check_inputs():
            self.dalek_connection = self.jira_autenticator.autenticate_with_dalek(self.core_id, self.password)
            if self.dalek_connection:
                self.login_view.change_message('User successfully autenticated!\nPlease wait a few seconds...',
                                               '#FFFFFF')
            else:
                self.login_view.change_message('Invalid core ID or password!', '#FFFFFF')
        return self.dalek_connection

    def check_idart_autentication(self):
        if self.check_inputs():
            self.idart_connection = self.jira_autenticator.autenticate_with_idart(self.core_id, self.password)
            if self.idart_connection:
                self.login_view.change_message('User successfully autenticated!\nPlease wait a few seconds...',
                                               '#FFFFFF')
            else:
                self.login_view.change_message('Invalid core ID or password!', '#FFFFFF')
        return self.idart_connection
