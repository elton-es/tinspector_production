from generate_report_pt.model.jira import test_plan as test_plan_model
from generate_report_pt.view.frames.test_plan import test_plan as test_plan_view

import re


class TestPlan:
    def __init__(self, window, dalek_connection):
        self.tp_frame = test_plan_view.TestPlan(window)
        self.tp_frame.tp_search_button['command'] = self.search_tp_values
        self.tp_id = None
        self.test_plan_model = None
        self.dalek_connection = dalek_connection
        self.data = dict({
            'status': '',
            'build': '',
            'hw_revision': '',
            'carrier': '',
            'sn': '',
            'sim': '',
            'sd': '',
            'hw_version': ''
        })

    def check_input(self):
        self.tp_id = self.tp_frame.get_tp_id()
        if self.tp_id == '':
            print('The test plan ID can not be empty!')
            self.tp_frame.show_warning('Empty test plan ID', 'The test plan ID can not be empty!')
            return False
        elif not re.search('^(PRODTEST-)[0-9]*', self.tp_id):
            print('Only issues of Product Test project (aka PRODTEST) are supported!')
            self.tp_frame.show_warning('Wrong issue project', 'Only issues of Product Test project (aka PRODTEST) are '
                                                              'supported!')
            return False
        return True

    def connect_to_model(self):
        if self.check_input():
            self.test_plan_model = test_plan_model.TestPlan(self.dalek_connection, self.tp_id)
            if not self.test_plan_model.tp_issue:
                self.tp_frame.show_error("Invalid issue", 'The issue ID is invalid or does not exist!')
            elif self.test_plan_model.check_if_is_tp():
                return True
            else:
                self.test_plan_model = None
                print('You must inform an ID of a Test Plan issue!')
                self.tp_frame.show_error("Wrong issue type", 'You must inform an ID of a Test Plan issue!')
        return False

    def search_tp_values(self):
        if self.connect_to_model():
            summary = self.test_plan_model.get_tp_field('summary')
            self.select_test_cycle(summary)
            self.data['status'] = self.test_plan_model.get_tp_field('status')
            self.data['build'] = self.test_plan_model.get_tp_field('build')
            self.data['hw_revision'] = self.test_plan_model.get_tp_field('hw_revision')
            configuration = self.test_plan_model.get_tp_field('configuration')
            configuration = configuration.split('\r\n')
            self.tp_frame.set_tv_value(1, 3, summary)
            self.tp_frame.set_tv_value(2, 3, self.data['status'])
            self.tp_frame.set_tv_value(3, 3, self.data['build'])
            self.tp_frame.set_tv_value(4, 3, self.data['hw_revision'])
            for value in configuration:
                if any([expected in value.lower() for expected in ['ret', 'open', 'amx', 'carrier']]):
                    self.data['carrier'] = value
                    self.tp_frame.set_tv_value(5, 3, value)
                elif 'serial' in value.lower():
                    self.data['sn'] = value
                    self.tp_frame.set_tv_value(6, 3, value)
                elif 'sim' in value.lower():
                    self.data['sim'] = value
                    self.tp_frame.set_tv_value(7, 3, value)
                elif 'sd' in value.lower():
                    self.data['sd'] = value
                    self.tp_frame.set_tv_value(8, 3, value)
                elif 'hw' in value.lower():
                    self.data['hw_version'] = value
                    self.tp_frame.set_tv_value(9, 3, value)
            for i in range(1, 10):
                self.tp_frame.set_tv_tags(i, 'fetched')

    def select_test_cycle(self, summary):
        if 'Quick' in summary:
            self.tp_frame.set_test_cycle_name('Quick Validation')
        elif 'Boiler' in summary:
            self.tp_frame.set_test_cycle_name('Boiler room')
        elif 'Background' in summary:
            self.tp_frame.set_test_cycle_name('Background 25h')
        elif '3GPP' in summary:
            self.tp_frame.set_test_cycle_name('3GPP Emergency Numbers')
        elif 'TTY' in summary:
            self.tp_frame.set_test_cycle_name('PTCV TTY')
