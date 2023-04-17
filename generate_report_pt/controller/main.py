from generate_report_pt.model.validator.test_plan import validator

from generate_report_pt.view import main

from generate_report_pt.controller import login as login_controller
from generate_report_pt.controller import test_plan as test_plan_controller
from generate_report_pt.controller import test_cases as test_cases_controller
from generate_report_pt.controller import crs as crs_controller

from tkinter import *


class Controller:
    def __init__(self, window=None):

        # Setting up the login controller
        self.login_controller = login_controller.Login(window)
        self.login_controller.login_view.log_in['command'] = self.set_up_main_window

        # Setting up the test plan controller
        self.test_plan_controller = None

        # Setting up the test cases controller
        self.test_cases_controller = None

        # Setting up the crs controller
        self.crs_controller = None

        self.root = window
        self.main_window = None
        self.dalek_connection = None
        self.idart_connection = None

    def set_up_main_window(self):
        self.dalek_connection = self.login_controller.check_dalek_autentication()
        self.idart_connection = self.login_controller.check_idart_autentication()
        if self.dalek_connection and self.idart_connection:
            self.create_main_window()
            self.show_tp_frame()
            self.root.after(2000, self.root.destroy())

    def create_main_window(self):
        self.main_window = main.Main(Tk())
        self.test_plan_controller = test_plan_controller.TestPlan(self.main_window.window, self.dalek_connection)
        self.test_plan_controller.tp_frame.set_core_id('Core ID: ' + self.login_controller.core_id)
        self.test_plan_controller.tp_frame.tp_validate_button['command'] = self.validate_data
        self.test_cases_controller = test_cases_controller.TestCases(self.main_window.window, self.dalek_connection)
        self.test_cases_controller.tcs_frame.set_core_id('Core ID: ' + self.login_controller.core_id)
        self.crs_controller = crs_controller.CRs(self.main_window.window, self.dalek_connection, self.idart_connection)
        self.crs_controller.crs_frame.set_core_id('Core ID: ' + self.login_controller.core_id)
        self.main_window.show_menu.entryconfig(0, command=self.show_tp_frame)
        self.main_window.show_menu.entryconfig(1, command=self.show_tc_frame)
        self.main_window.show_menu.entryconfig(3, command=self.show_crs_frame)

    def show_tp_frame(self):
        self.hide_all_frames()
        self.test_plan_controller.tp_frame.frame.pack(fill='both', expand=1)

    def show_tc_frame(self):
        self.hide_all_frames()
        self.test_cases_controller.tcs_frame.frame.pack(fill='both', expand=1)

    def show_crs_frame(self):
        self.hide_all_frames()
        self.crs_controller.crs_frame.frame.pack(fill='both', expand=1)

    def hide_all_frames(self):
        self.test_plan_controller.tp_frame.frame.pack_forget()
        self.test_cases_controller.tcs_frame.frame.pack_forget()
        self.crs_controller.crs_frame.frame.pack_forget()

    def validate_data(self):
        validation = validator.Validator(self.test_plan_controller.data)
        if validation.validate_status():
            self.test_plan_controller.tp_frame.set_tv_value(2, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(2, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(2, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(2, 'not_ok')
        if validation.validate_primary_sw():
            self.test_plan_controller.tp_frame.set_tv_value(3, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(3, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(3, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(3, 'not_ok')
        if validation.validate_hw_revision():
            self.test_plan_controller.tp_frame.set_tv_value(4, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(4, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(4, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(4, 'not_ok')
        if validation.validate_carrier():
            self.test_plan_controller.tp_frame.set_tv_value(5, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(5, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(5, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(5, 'not_ok')
        if validation.validate_sn():
            self.test_plan_controller.tp_frame.set_tv_value(6, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(6, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(6, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(6, 'not_ok')
        if validation.validate_sim_card():
            self.test_plan_controller.tp_frame.set_tv_value(7, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(7, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(7, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(7, 'not_ok')
        if validation.validate_sd_card():
            self.test_plan_controller.tp_frame.set_tv_value(8, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(8, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(8, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(8, 'not_ok')
        if validation.validate_hw_version():
            self.test_plan_controller.tp_frame.set_tv_value(9, 4, 'OK')
            self.test_plan_controller.tp_frame.set_tv_tags(9, 'ok')
        else:
            self.test_plan_controller.tp_frame.set_tv_value(9, 4, 'Not OK')
            self.test_plan_controller.tp_frame.set_tv_tags(9, 'not_ok')
