from art.model.jira import test_plan as test_plan_model
from art.view.frames.test_plan import test_plan as test_plan_view

import re


class TestPlan:
    def __init__(self, window, zephyr_connection):
        self.tp_frame = test_plan_view.TestPlan(window)
        self.tp_frame.tp_search_button['command'] = self.search_tp_values
        self.test_cycle_id = None
        self.test_plan_model = None
        self.zephyr_connection = zephyr_connection
        self.data = dict({'status': ''})

    def check_input(self):
        self.test_cycle_id = self.tp_frame.get_tp_id()
        if self.test_cycle_id == '':
            print('The test plan ID can not be empty!')
            self.tp_frame.show_warning('Empty test plan ID', 'The test plan ID can not be empty!')
            return False
        elif not re.search('^(UN-R)[0-9]*', self.test_cycle_id):
            print('Only issues of UX Nator project (aka UN) are supported!')
            self.tp_frame.show_warning('Wrong issue project', 'Only issues of UX Nator project (aka UN) are '
                                                              'supported!')
            return False
        return True

    def connect_to_model(self):
        if self.check_input():
            self.test_plan_model = test_plan_model.TestPlan(self.zephyr_connection, self.test_cycle_id)
            if not self.test_plan_model.test_cycle_issue:
                self.tp_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
                return False
            return True


    def search_tp_values(self):
        if self.connect_to_model():
            name = self.test_plan_model.get_name()
            description = self.test_plan_model.get_description()
            status = self.test_plan_model.get_status()
            self.tp_frame.set_tv_value(1, 1, name)
            self.tp_frame.set_tv_value(1, 2, description)
            self.tp_frame.set_tv_value(1, 3, status)
            self.tp_frame.set_tv_tags(1, 'fetched')
            self.tp_frame.enable_validate_button()
