from cycle_review_tool.model.jira import test_cases as test_cases_model
from cycle_review_tool.view.frames.test_cases import test_cases as test_cases_view
from cycle_review_tool.model.validator.test_cases import test_cases as test_cases_validator

import re


class TestCases:
    def __init__(self, window, dalek_connection):
        self.tcs_frame = test_cases_view.TestCases(window)
        self.tcs_frame.tp_search_button['command'] = self.search_values
        self.tcs_frame.tp_validate_button['command'] = self.validate_data
        self.test_cases_model = None
        self.cycle_name = None
        self.number_of_tcs = None
        self.number_of_crs = None
        self.tp_id = None
        self.android_version = None
        self.test_cases_validator = None
        self.validations = None
        self.dalek_connection = dalek_connection

    def search_values(self):
        if self.connect_to_model():
            self.set_cycle_name()
            self.set_number_of_tcs()
            self.set_number_of_crs()
            self.clear_tv_values()
            self.update_tv_values()
            self.tcs_frame.enable_validate_button()

    def check_android_version_input(self):
        self.android_version = self.tcs_frame.get_android_version()
        if self.android_version == '' or self.android_version is None:
            print('The Android Version can\'t be empty!')
            self.tcs_frame.show_warning('No Android Version selected', 'One Android Version needs to be selected!')
            return False
        return True

    def check_tp_id_input(self):
        self.tp_id = self.tcs_frame.get_tp_id()
        if self.tp_id == '':
            print('The test plan ID can not be empty!')
            self.tcs_frame.show_warning('Empty test plan ID', 'The test plan ID can not be empty!')
            return False
        elif not re.search('^(PRODTEST-)[0-9]*', self.tp_id):
            print('Only issues of Product Test project (aka PRODTEST) are supported!')
            self.tcs_frame.show_warning('Wrong issue project', 'Only issues of Product Test project (aka PRODTEST) are '
                                                              'supported!')
            return False
        return True

    def connect_to_model(self):
        if self.check_tp_id_input():
            self.test_cases_model = test_cases_model.TestCases(self.dalek_connection, self.tp_id)
            if not self.test_cases_model.tp_issue:
                self.tcs_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
            elif self.test_cases_model.check_if_is_tp():
                return True
            else:
                self.test_cases_model = None
                print('You must inform an ID of a Test Plan issue!')
                self.tcs_frame.show_error("Wrong issue type", 'You must inform an ID of a Test Plan issue!')
        return False

    def set_cycle_name(self):
        self.cycle_name = self.test_cases_model.get_cycle_name()
        self.tcs_frame.set_test_cycle_name(self.cycle_name)

    def set_number_of_tcs(self):
        self.number_of_tcs = self.test_cases_model.get_number_of_tcs()
        self.tcs_frame.set_number_of_tcs('Number of TCs: ' + str(self.number_of_tcs))

    def set_number_of_crs(self):
        self.number_of_crs = self.test_cases_model.get_number_of_crs()
        self.tcs_frame.set_number_of_crs('Number of CRs: ' + str(self.number_of_crs))

    def update_tv_values(self):
        for i in range(self.number_of_tcs):
            key = self.test_cases_model.get_key_from_tc(i)
            test_results = self.test_cases_model.get_test_results_from_tc(i)
            cr = self.test_cases_model.get_remote_defect_cr_from_tc(i)
            explanation = self.test_cases_model.get_explanation_from_tc(i)
            comments = self.test_cases_model.get_comments_from_tc(i)[0]
            comments = self.format_comments(comments)
            self.tcs_frame.set_tv_tags(i + 1, 'fetched')
            self.tcs_frame.set_tv_value(i + 1, 1, key)
            self.tcs_frame.set_tv_value(i + 1, 2, test_results)
            self.tcs_frame.set_tv_value(i + 1, 3, cr)
            self.tcs_frame.set_tv_value(i + 1, 4, explanation)
            self.tcs_frame.set_tv_value(i + 1, 5, comments)

    @staticmethod
    def format_comments(comment):
        formated_comment = """"""
        lines = comment.split('\r\n')
        for line in lines:
            if line != '':
                formated_comment = formated_comment + line + '\n'
        return formated_comment

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
            if self.check_android_version_input():
                self.test_cases_validator = test_cases_validator.TestCasesValidator(self.test_cases_model.test_cases_data,
                                                                                    self.android_version)
                self.validations = self.test_cases_validator.validate_all()
                for i in range(self.number_of_tcs):
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
            print('You can\'t validate data before searching the TP')
