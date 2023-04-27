from tkinter import *
from tkinter import ttk, messagebox


class TestCases:
    def __init__(self, window):
        self.frame = Frame(window)

        # Test cases params frame
        self.tc_params_frame = Frame(self.frame)
        self.tc_params_frame['width'] = 500
        self.tc_params_frame['height'] = 700
        self.tc_params_frame['background'] = '#677756'
        self.tc_params_frame['highlightbackground'] = '#A9A9A9'
        self.tc_params_frame['highlightthickness'] = 1
        self.tc_params_frame.pack(side='left', fill='y', padx=2, pady=2)

        # Frame for general info
        self.tc_general_frame = Frame(self.tc_params_frame)
        self.tc_general_frame['highlightbackground'] = 'silver'
        self.tc_general_frame['background'] = '#E8E9E9'
        self.tc_general_frame['highlightthickness'] = 1
        self.tc_general_frame.pack(side=TOP, padx=5, pady=5)

        # Params
        self.view_name_label = Label(self.tc_general_frame, width=20)
        self.view_name_label['text'] = 'Test Executions View'
        self.view_name_label['background'] = '#E8E9E9'
        self.view_name_label['font'] = ('Calibri', 15, 'bold')
        self.view_name_label.pack(padx=10, pady=10)

        self.core_id_label = Label(self.tc_general_frame)
        self.core_id_label['text'] = 'User:'
        self.core_id_label['background'] = '#E8E9E9'
        self.core_id_label['font'] = ('Calibri', 12)
        self.core_id_label.pack(padx=10, pady=10)

        self.tp_id_label = Label(self.tc_general_frame)
        self.tp_id_label['text'] = 'Test Cycle ID'
        self.tp_id_label['background'] = '#E8E9E9'
        self.tp_id_label['font'] = ('Calibri', 12)
        self.tp_id_label.pack(padx=10, pady=10)

        self.test_cycle_id_entry = Entry(self.tc_general_frame)
        self.test_cycle_id_entry['font'] = ('Calibri', 12)
        self.test_cycle_id_entry['justify'] = 'center'
        self.test_cycle_id_entry.pack(fill=X, padx=10)

        self.tp_search_button = Button(self.tc_general_frame)
        self.tp_search_button['font'] = ('Calibri', 12)
        self.tp_search_button['text'] = 'Search Test Cycle'
        self.tp_search_button.pack(pady=10, padx=10, fill=X)

        # Frame for review info
        self.tc_review_frame = Frame(self.tc_params_frame)
        self.tc_review_frame['background'] = '#E8E9E9'
        self.tc_review_frame['highlightbackground'] = 'silver'
        self.tc_review_frame['highlightthickness'] = 1
        self.tc_review_frame.pack(side=TOP, padx=5)

        self.tv_test_cycle = Label(self.tc_review_frame, width=20)
        self.tv_test_cycle['text'] = 'Review info'
        self.tv_test_cycle['background'] = '#E8E9E9'
        self.tv_test_cycle['font'] = ('Calibri', 15, 'bold')
        self.tv_test_cycle.pack(padx=10, pady=10)

        self.tv_tcs_number = Label(self.tc_review_frame)
        self.tv_tcs_number['text'] = 'Number of Test Executions:'
        self.tv_tcs_number['background'] = '#E8E9E9'
        self.tv_tcs_number['font'] = ('Calibri', 10)
        self.tv_tcs_number.pack(padx=10)

        self.tv_issues_number = Label(self.tc_review_frame)
        self.tv_issues_number['text'] = 'Number of Issues:'
        self.tv_issues_number['background'] = '#E8E9E9'
        self.tv_issues_number['font'] = ('Calibri', 10)
        self.tv_issues_number.pack(padx=10)

        self.tp_validate_button = Button(self.tc_review_frame)
        self.tp_validate_button['font'] = ('Calibri', 12)
        self.tp_validate_button['text'] = 'Review data'
        self.tp_validate_button['state'] = 'disabled'
        self.tp_validate_button.pack(fill=X, padx=10, pady=5)

        # Test plan data frame
        self.tc_data_frame = Frame(self.frame)
        self.tc_data_frame['width'] = 1920
        self.tc_data_frame['height'] = 700
        self.tc_data_frame['background'] = '#677756'
        self.tc_data_frame['highlightbackground'] = '#A9A9A9'
        self.tc_data_frame['highlightthickness'] = 1
        self.tc_data_frame.pack(side='right', fill='both', padx=2, pady=2)

        # Treeview vertical scrollbar
        self.sc_tree_vertical = Scrollbar(self.tc_data_frame)
        self.sc_tree_vertical.pack(side=RIGHT, fill=Y)

        # Treeview horizontal scrollbar
        self.sc_tree_horizontal = Scrollbar(self.tc_data_frame, orient='horizontal')
        self.sc_tree_horizontal.pack(side=BOTTOM, fill=X)

        # Test cases treeview
        self.tv_data = ttk.Treeview(self.tc_data_frame)
        self.tv_data['yscrollcommand'] = self.sc_tree_vertical.set
        self.tv_data['xscrollcommand'] = self.sc_tree_horizontal.set
        self.tv_data['columns'] = (1, 2, 3, 4, 5, 6, 7)
        self.tv_data['show'] = 'headings'
        self.tv_data['height'] = 1080
        self.tv_data.column(1, width=100, anchor='c')
        self.tv_data.column(2, width=150, anchor='c')
        self.tv_data.column(3, width=150, anchor='c')
        self.tv_data.column(4, width=400, anchor='c')
        self.tv_data.column(5, width=400, anchor='c')
        self.tv_data.column(6, width=100, anchor='c')
        self.tv_data.column(7, width=400, anchor='c')
        self.tv_data.heading(1, text='Key')
        self.tv_data.heading(2, text='Environment')
        self.tv_data.heading(3, text='Test Results')
        self.tv_data.heading(4, text='Comments')
        self.tv_data.heading(5, text='Issues')
        self.tv_data.heading(6, text='Validation')
        self.tv_data.heading(7, text='Notes')
        self.tv_data.pack(fill='both', padx=5, pady=5)

        # Create 400 rows
        for i in range(400):
            self.tv_data.insert('', 'end', iid=i + 1, values=['', '', '', '', '', '', ''], tags=('init',))

        # Tags for TreeView
        self.tv_data.tag_configure('init', font=('Helvetica', 8), foreground='#77878B', background='#E8E8E8')
        self.tv_data.tag_configure('fetched', font=('Helvetica', 8, 'bold'), foreground='#363636', background='#E8E8E8')
        self.tv_data.tag_configure('ok', font=('Helvetica', 8, 'bold'), foreground='#50C878', background='#E8E8E8')
        self.tv_data.tag_configure('not_ok', font=('Helvetica', 8, 'bold'), foreground='#880808', background='#F3E8EA')

        # Configure the vertical scrollbar
        self.sc_tree_vertical.config(command=self.tv_data.yview)

        # Configure the horizontal scrollbar
        self.sc_tree_horizontal.config(command=self.tv_data.xview)

        # Adding style to treeview
        self.style = ttk.Style(self.tc_data_frame)
        self.style.configure('Treeview',
                             foreground='black',
                             rowheight=70,
                             )
        self.style.map('Treeview', background=[('selected', '#ADD8E6')])

    def get_test_cycle_id(self):
        return self.test_cycle_id_entry.get()

    def set_tv_value(self, row, column, value):
        self.tv_data.set(row, column, value)

    def set_tv_tags(self, iid, tag):
        self.tv_data.item(iid, tags=tag)

    def set_core_id(self, core_id):
        self.core_id_label['text'] = core_id

    def set_number_of_tcs(self, number):
        self.tv_tcs_number['text'] = number

    def set_number_of_issues(self, number):
        self.tv_issues_number['text'] = number

    def show_warning(self, title, message):
        messagebox.showwarning(title, message, parent=self.frame)

    def show_error(self, title, message):
        messagebox.showerror(title, message, parent=self.frame)

    def enable_validate_button(self):
        self.tp_validate_button['state'] = 'normal'

    def disable_validate_button(self):
        self.tp_validate_button['state'] = 'disabled'
