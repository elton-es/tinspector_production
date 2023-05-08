from art.model.jira import issues as crs_model
from art.view.frames.crs import crs as crs_view
from art.model.validator.issues import issues as issues_validator

import re


class Issues:
    def __init__(self, window, zephyr_connection, jira_connection):
        self.crs_frame = crs_view.CRs(window)
        self.crs_frame.tp_search_button['command'] = self.search_values
        self.crs_frame.tp_validate_button['command'] = self.validate_data
        self.crs_model = None
        self.cycle_name = None
        self.number_of_failed_test_executions = None
        self.number_of_linked_issues = None
        self.test_cycle_id = None
        self.android_version = None
        self.labels = None
        self.issue_watchers = None
        self.issues_validator = None
        self.validations = None
        self.zephyr_connection = zephyr_connection
        self.jira_connection = jira_connection

    def check_test_cycle_id_input(self):
        self.test_cycle_id = self.crs_frame.get_tp_id()
        if self.test_cycle_id == '':
            print('The Test Cycle ID can not be empty!')
            self.crs_frame.show_warning('Empty Test Cycle ID', 'The Test Cycle ID can not be empty!')
            return False
        elif not re.search('^(UN-)[0-9]*', self.test_cycle_id):
            print('Only issues of UX Nator project (aka UN) are supported!')
            self.crs_frame.show_warning('Wrong issue project', 'Only issues of UX Nator project (aka UN) are '
                                                               'supported!')
            return False
        return True

    def check_labels_input(self):
        self.labels = self.crs_frame.get_labels()
        self.labels = self.labels.split('\n')
        self.labels = list(filter(lambda x: x != '', self.labels))
        self.labels = [label.replace(' ', '').replace(',', '') for label in self.labels]
        if len(self.labels) > 0:
            return True
        else:
            print('Device labels can not be empty!')
            self.crs_frame.show_warning('Empty device labels', 'Device labels must be informed!')
            self.labels = None
            return False

    def check_watchers_input(self):
        self.issue_watchers = self.crs_frame.get_watchers()
        self.issue_watchers = self.issue_watchers.split('\n')
        self.issue_watchers = list(filter(lambda x: x != '', self.issue_watchers))
        self.issue_watchers = [issue.replace(',', '') for issue in self.issue_watchers]
        if len(self.issue_watchers) > 0:
            return True
        else:
            print('CR Watchers can not be empty!')
            self.crs_frame.show_warning('Empty CR Watchers', 'CR Watchers must be informed!')
            self.issue_watchers = None
            return False

    def connect_to_model(self):
        if self.check_test_cycle_id_input():
            self.crs_model = crs_model.Issues(self.zephyr_connection, self.jira_connection, self.test_cycle_id)
            if not self.crs_model.test_cycle_issue:
                self.crs_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
                self.crs_model = None
                return False
        return True

    def search_values(self):
        if self.connect_to_model():
            self.set_number_of_failed_test_executions()
            self.set_number_of_linked_issues()
            self.clear_tv_values()
            self.update_tv_values()
            self.crs_frame.enable_validate_button()

    def set_number_of_failed_test_executions(self):
        self.number_of_failed_test_executions = self.crs_model.number_of_failed_test_executions
        self.crs_frame.set_number_of_failed_test_executions('Number of Test Executions: ' +
                                                            str(self.number_of_failed_test_executions))

    def set_number_of_linked_issues(self):
        self.number_of_linked_issues = self.crs_model.number_of_linked_issues
        self.crs_frame.set_number_of_issues('Number of Issues: ' + str(self.number_of_linked_issues))

    def update_tv_values(self):
        for i in range(self.number_of_linked_issues):
            key = self.crs_model.get_key_from_issue(i)
            issue_status = self.crs_model.get_status_from_issue(i)
            if self.crs_model.get_comments_from_issue(i):
                comment = self.crs_model.get_comments_from_issue(i)[0].body
                comment = comment.replace('<br>', '\n')
            else:
                comment = None
            self.crs_frame.set_tv_tags(i + 1, 'fetched')
            self.crs_frame.set_tv_value(i + 1, 1, key)
            self.crs_frame.set_tv_value(i + 1, 2, issue_status)
            self.crs_frame.set_tv_value(i + 1, 5, comment)

    def clear_tv_values(self):
        for i in range(50):
            self.crs_frame.set_tv_value(i + 1, 1, '')
            self.crs_frame.set_tv_value(i + 1, 2, '')
            self.crs_frame.set_tv_value(i + 1, 3, '')
            self.crs_frame.set_tv_value(i + 1, 4, '')
            self.crs_frame.set_tv_value(i + 1, 5, '')
            self.crs_frame.set_tv_value(i + 1, 6, '')
            self.crs_frame.set_tv_value(i + 1, 7, '')

    def validate_data(self):
        if self.crs_model:
            if self.check_labels_input() and self.check_watchers_input():
                self.issues_validator = issues_validator.IssuesValidator(self.crs_model.issues_data, self.labels,
                                                                         self.issue_watchers)
                self.validations = self.issues_validator.validate_all()
                for i in range(self.number_of_linked_issues):
                    notes = self.validations[i][1]
                    validation = self.validations[i][2]
                    if any('Label' in item for item in notes):
                        self.crs_frame.set_tv_value(i + 1, 3, 'Not OK')
                    else:
                        self.crs_frame.set_tv_value(i + 1, 3, 'OK')
                    if any('Watcher' in item for item in notes):
                        self.crs_frame.set_tv_value(i + 1, 4, 'Not OK')
                    else:
                        self.crs_frame.set_tv_value(i + 1, 4, 'OK')
                    if validation:
                        self.crs_frame.set_tv_tags(i + 1, 'ok')
                        self.crs_frame.set_tv_value(i + 1, 6, 'OK')
                    else:
                        self.crs_frame.set_tv_tags(i + 1, 'not_ok')
                        self.crs_frame.set_tv_value(i + 1, 6, 'Not OK')
                        actions = ''
                        for note in notes:
                            actions += note + '\n'
                        if actions != '':
                            self.crs_frame.set_tv_value(i + 1, 7, actions)
                self.issues_validator.generate_actions_message()
                self.crs_frame.disable_validate_button()
            else:
                print('You can\'t validate data before searching the TP')
