from art.model.validator.test_plan import validator

from art.view import main

from art.controller import login as login_controller
from art.controller import test_plan as test_plan_controller
from art.controller import test_cases as test_cases_controller
from art.controller import issues as crs_controller

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

        # Setting up the issues controller
        self.crs_controller = None

        self.root = window
        self.main_window = None
        self.jira_connection = None
        self.zephyr_connection = None

    def set_up_main_window(self):
        self.jira_connection, self.zephyr_connection = self.login_controller.check_jira_authentication()
        if self.jira_connection:
            self.create_main_window()
            self.show_tp_frame()
            self.root.after(2000, self.root.destroy())

    def create_main_window(self):
        self.main_window = main.Main(Tk())
        self.test_plan_controller = test_plan_controller.TestPlan(self.main_window.window, self.zephyr_connection)
        self.test_plan_controller.tp_frame.set_core_id('User: ' + self.login_controller.core_id)
        self.test_cases_controller = test_cases_controller.TestCases(self.main_window.window, self.zephyr_connection,
                                                                     self.jira_connection)
        self.test_cases_controller.tcs_frame.set_core_id('User: ' + self.login_controller.core_id)
        self.crs_controller = crs_controller.Issues(self.main_window.window, self.zephyr_connection,
                                                    self.jira_connection)
        self.crs_controller.crs_frame.set_core_id('User: ' + self.login_controller.core_id)
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
