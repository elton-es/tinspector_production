from art.model.jira import test_cases as test_cases_model
from art.view.frames.test_cases import test_cases as test_cases_view
from art.model.validator.test_cases import test_cases as test_cases_validator

import re


class TestCases:
    def __init__(self, window, zephyr_connection, jira_connection):
        self.tcs_frame = test_cases_view.TestCases(window)
        self.tcs_frame.tp_search_button['command'] = self.search_values
        self.tcs_frame.tp_validate_button['command'] = self.validate_data
        self.test_cases_model = None
        self.cycle_name = None
        self.number_of_test_executions = None
        self.number_of_issues = None
        self.test_cycle_id = None
        self.test_cases_validator = None
        self.validations = None
        self.zephyr_connection = zephyr_connection
        self.jira_connection = jira_connection

    def search_values(self):
        if self.connect_to_model():
            self.set_number_of_test_case_executions()
            self.set_number_of_issues()
            self.clear_tv_values()
            self.update_tv_values()
            self.tcs_frame.enable_validate_button()

    def check_tp_id_input(self):
        self.test_cycle_id = self.tcs_frame.get_test_cycle_id()
        if self.test_cycle_id == '':
            print('The test plan ID can not be empty!')
            self.tcs_frame.show_warning('Empty test plan ID', 'The test plan ID can not be empty!')
            return False
        elif not re.search('^(UN-)[0-9]*', self.test_cycle_id):
            print('Only issues of UX Nator project (aka UN) are supported!')
            self.tcs_frame.show_warning('Wrong issue project', 'Only issues of UX Nator project (aka UN) are '
                                                               'supported!')
            return False
        return True

    def connect_to_model(self):
        if self.check_tp_id_input():
            self.test_cases_model = test_cases_model.TestCases(self.zephyr_connection, self.jira_connection,
                                                               self.test_cycle_id)
            if not self.test_cases_model.test_cycle_issue:
                self.tcs_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
                self.test_cases_model = None
                return False
        return True

    def set_number_of_test_case_executions(self):
        self.number_of_test_executions = self.test_cases_model.number_of_test_executions
        self.tcs_frame.set_number_of_tcs('Number of Test Case Executions: ' + str(self.number_of_test_executions))

    def set_number_of_issues(self):
        self.number_of_issues = self.test_cases_model.number_of_issues
        self.tcs_frame.set_number_of_issues('Number of CRs: ' + str(self.number_of_issues))

    def update_tv_values(self):
        for i in range(self.number_of_test_executions):
            key = self.test_cases_model.get_test_execution_key(i)
            environment = self.test_cases_model.get_environment(i)
            test_results = self.test_cases_model.get_test_result(i)
            issues = self.test_cases_model.get_issues_keys(i)
            issues = self.format_issues_keys(issues)
            comment = self.test_cases_model.get_comment(i)
            comment = self.format_comments(comment)
            self.tcs_frame.set_tv_tags(i + 1, 'fetched')
            self.tcs_frame.set_tv_value(i + 1, 1, key)
            self.tcs_frame.set_tv_value(i + 1, 2, environment)
            self.tcs_frame.set_tv_value(i + 1, 3, test_results)
            self.tcs_frame.set_tv_value(i + 1, 4, comment)
            self.tcs_frame.set_tv_value(i + 1, 5, issues)

    @staticmethod
    def format_comments(comment):
        formatted_comment = """"""
        lines = comment.split('<br>')
        for line in lines:
            if line != '':
                formatted_comment += line + '\n'
        return formatted_comment

    @staticmethod
    def format_issues_keys(issues_keys):
        formatted_issues_keys = """"""
        for issue_key in issues_keys:
            formatted_issues_keys += issue_key + '\n'
        return formatted_issues_keys

    def clear_tv_values(self):
        for i in range(400):
            self.tcs_frame.set_tv_value(i + 1, 1, '')
            self.tcs_frame.set_tv_value(i + 1, 2, '')
            self.tcs_frame.set_tv_value(i + 1, 3, '')
            self.tcs_frame.set_tv_value(i + 1, 4, '')
            self.tcs_frame.set_tv_value(i + 1, 5, '')
            self.tcs_frame.set_tv_value(i + 1, 6, '')
            self.tcs_frame.set_tv_value(i + 1, 7, '')

    def validate_data(self):
        if self.test_cases_model:
            self.test_cases_validator = test_cases_validator.TestCasesValidator(
                self.test_cases_model.test_executions_data)
            self.validations = self.test_cases_validator.validate_all()
            for i in range(self.number_of_test_executions):
                notes = self.validations[i][1]
                validation = self.validations[i][2]
                if validation:
                    self.tcs_frame.set_tv_tags(i + 1, 'ok')
                    self.tcs_frame.set_tv_value(i + 1, 6, 'OK')
                else:
                    self.tcs_frame.set_tv_tags(i + 1, 'not_ok')
                    self.tcs_frame.set_tv_value(i + 1, 6, 'Not OK')
                    actions = ''
                    for note in notes:
                        actions += note + '\n'
                    if actions != '':
                        self.tcs_frame.set_tv_value(i + 1, 7, actions)
            self.test_cases_validator.generate_actions_message()
            self.tcs_frame.disable_validate_button()
        else:
            print('You can\'t validate data before searching the Test Cycle')
