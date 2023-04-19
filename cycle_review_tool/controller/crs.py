from cycle_review_tool.model.jira import crs as crs_model
from cycle_review_tool.view.frames.crs import crs as crs_view
from cycle_review_tool.model.validator.crs import crs as crs_validator

import re


class CRs:
    def __init__(self, window, dalek_connection, idart_connection):
        self.crs_frame = crs_view.CRs(window)
        self.crs_frame.tp_search_button['command'] = self.search_values
        self.crs_frame.tp_validate_button['command'] = self.validate_data
        self.crs_model = None
        self.cycle_name = None
        self.number_of_failed_tcs = None
        self.number_of_linked_crs = None
        self.tp_id = None
        self.android_version = None
        self.device_labels = None
        self.cr_watchers = None
        self.crs_validator = None
        self.validations = None
        self.dalek_connection = dalek_connection
        self.idart_connection = idart_connection

    def check_tp_id_input(self):
        self.tp_id = self.crs_frame.get_tp_id()
        if self.tp_id == '':
            print('The test plan ID can not be empty!')
            self.crs_frame.show_warning('Empty test plan ID', 'The test plan ID can not be empty!')
            return False
        elif not re.search('^(PRODTEST-)[0-9]*', self.tp_id):
            print('Only issues of Product Test project (aka PRODTEST) are supported!')
            self.crs_frame.show_warning('Wrong issue project', 'Only issues of Product Test project (aka PRODTEST) are '
                                                              'supported!')
            return False
        return True

    def check_android_version_input(self):
        self.android_version = self.crs_frame.get_android_version()
        if self.android_version == '' or self.android_version is None:
            print('The Android Version can\'t be empty!')
            self.crs_frame.show_warning('No Android Version selected', 'One Android Version needs to be selected!')
            return False
        return True

    def check_device_labels_input(self):
        self.device_labels = self.crs_frame.get_devices_labels()
        self.device_labels = self.device_labels.split('\n')
        self.device_labels = list(filter(lambda x: x != '', self.device_labels))
        self.device_labels = [label.replace(' ', '').replace(',', '') for label in self.device_labels]
        if len(self.device_labels) > 0:
            return True
        else:
            print('Device labels can not be empty!')
            self.crs_frame.show_warning('Empty device labels', 'Device labels must be informed!')
            self.device_labels = None
            return False

    def check_watchers_input(self):
        self.cr_watchers = self.crs_frame.get_watchers()
        self.cr_watchers = self.cr_watchers.split('\n')
        self.cr_watchers = list(filter(lambda x: x != '', self.cr_watchers))
        self.cr_watchers = [cr.replace(' ', '').replace(',', '') for cr in self.cr_watchers]
        if len(self.cr_watchers) > 0:
            return True
        else:
            print('CR Watchers can not be empty!')
            self.crs_frame.show_warning('Empty CR Watchers', 'CR Watchers must be informed!')
            self.cr_watchers = None
            return False

    def connect_to_model(self):
        if self.check_tp_id_input():
            self.crs_model = crs_model.CRs(self.dalek_connection, self.idart_connection, self.tp_id)
            if not self.crs_model.tp_issue:
                self.crs_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
            elif self.crs_model.check_if_is_tp():
                return True
            else:
                print('You must inform an ID of a Test Plan issue!')
                self.crs_frame.show_error("Wrong issue type", 'You must inform an ID of a Test Plan issue!')
        self.crs_model = None
        return False

    def search_values(self):
        if self.connect_to_model():
            self.set_cycle_name()
            self.set_number_of_failed_tcs()
            self.set_number_of_linked_crs()
            self.clear_tv_values()
            self.update_tv_values()
            self.crs_frame.enable_validate_button()

    def set_cycle_name(self):
        self.cycle_name = self.crs_model.get_cycle_name()
        self.crs_frame.set_test_cycle_name(self.cycle_name)

    def set_number_of_failed_tcs(self):
        self.number_of_failed_tcs = self.crs_model.number_of_failed_tcs
        self.crs_frame.set_number_of_failed_tcs('Number of TCs: ' + str(self.number_of_failed_tcs))

    def set_number_of_linked_crs(self):
        self.number_of_linked_crs = self.crs_model.number_of_linked_crs
        self.crs_frame.set_number_of_crs('Number of CRs: ' + str(self.number_of_linked_crs))

    def update_tv_values(self):
        for i in range(self.number_of_linked_crs):
            key = self.crs_model.get_key_from_cr(i)
            cr_status = self.crs_model.get_status_from_cr(i)
            self.crs_frame.set_tv_tags(i + 1, 'fetched')
            self.crs_frame.set_tv_value(i + 1, 1, key)
            self.crs_frame.set_tv_value(i + 1, 2, cr_status)

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
            if self.check_android_version_input() and self.check_device_labels_input() and self.check_watchers_input():
                self.crs_validator = crs_validator.CRSValidator(self.crs_model.crs_data, self.android_version,
                                                                self.device_labels, self.cr_watchers)
                self.validations = self.crs_validator.validate_all()
                for i in range(self.number_of_linked_crs):
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
                self.crs_validator.generate_actions_message()
                self.crs_frame.disable_validate_button()
            else:
                print('You can\'t validate data before searching the TP')
