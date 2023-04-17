from generate_report_pt.model.jira import crs as crs_model
from generate_report_pt.view.frames.crs import crs as crs_view
from generate_report_pt.model.validator.crs import crs as crs_validator

import re


class CRs:
    def __init__(self, window, dalek_connection, idart_connection):
        self.crs_frame = crs_view.CRs(window)
        self.crs_frame.tp_search_button['command'] = self.search_values
        self.crs_frame.tp_validate_button['command'] = ''
        self.crs_model = None
        self.cycle_name = None
        self.number_of_failed_tcs = None
        self.number_of_linked_crs = None
        self.tp_id = None
        self.android_version = None
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
        if self.android_version == '':
            print('The Android Version can\'t be empty!')
            return False
        return True

    def search_values(self):
        if self.connect_to_model():
            # self.set_cycle_name()
            self.set_number_of_failed_tcs()
            self.set_number_of_linked_crs()
            self.clear_tv_values()
            self.update_tv_values()

    def connect_to_model(self):
        if self.check_tp_id_input():
            self.crs_model = crs_model.CRs(self.dalek_connection, self.idart_connection, self.tp_id)
            if not self.crs_model.tp_issue:
                self.crs_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
            elif self.crs_model.check_if_is_tp():
                return True
            else:
                self.crs_model = None
                print('You must inform an ID of a Test Plan issue!')
                self.crs_frame.show_error("Wrong issue type", 'You must inform an ID of a Test Plan issue!')
        return False

    # def set_cycle_name(self):
        # self.cycle_name = self.crs_model.get_cycle_name()
        # self.crs_frame.set_test_cycle_name(self.cycle_name)

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
