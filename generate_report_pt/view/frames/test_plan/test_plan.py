from tkinter import *
from tkinter import ttk, messagebox


class TestPlan:
    def __init__(self, window):
        self.frame = Frame(window)

        # Test plan params frame
        self.tp_params_frame = Frame(self.frame)
        self.tp_params_frame['width'] = 500
        self.tp_params_frame['height'] = 700
        self.tp_params_frame['background'] = '#677756'
        self.tp_params_frame['highlightbackground'] = '#A9A9A9'
        self.tp_params_frame['highlightthickness'] = 1
        self.tp_params_frame.pack(side='left', fill='y', padx=2, pady=2)

        # Frame for general info
        self.tp_general_frame = Frame(self.tp_params_frame)
        self.tp_general_frame['highlightbackground'] = 'silver'
        self.tp_general_frame['background'] = '#E8E9E9'
        self.tp_general_frame['highlightthickness'] = 1
        self.tp_general_frame.pack(side=TOP, padx=5, pady=5)

        # Params
        self.view_name_label = Label(self.tp_general_frame, width=20)
        self.view_name_label['text'] = 'Test Plan View'
        self.view_name_label['background'] = '#E8E9E9'
        self.view_name_label['font'] = ('Calibri', 15, 'bold')
        self.view_name_label.pack(padx=10, pady=10)

        self.core_id_label = Label(self.tp_general_frame)
        self.core_id_label['text'] = 'Core ID:'
        self.core_id_label['background'] = '#E8E9E9'
        self.core_id_label['font'] = ('Calibri', 12)
        self.core_id_label.pack(padx=10, pady=10)

        self.tp_id_label = Label(self.tp_general_frame)
        self.tp_id_label['text'] = 'Test Plan ID'
        self.tp_id_label['background'] = '#E8E9E9'
        self.tp_id_label['font'] = ('Calibri', 12)
        self.tp_id_label.pack(padx=10, pady=10)

        self.tp_id_entry = Entry(self.tp_general_frame)
        self.tp_id_entry['font'] = ('Calibri', 12)
        self.tp_id_entry['justify'] = 'center'
        self.tp_id_entry.pack(fill=X, padx=10)

        self.tp_search_button = Button(self.tp_general_frame)
        self.tp_search_button['font'] = ('Calibri', 12)
        self.tp_search_button['text'] = 'Search TP'
        self.tp_search_button.pack(pady=10, padx=10, fill=X)

        # Frame for review info
        self.tp_review_frame = Frame(self.tp_params_frame)
        self.tp_review_frame['background'] = '#E8E9E9'
        self.tp_review_frame['highlightbackground'] = 'silver'
        self.tp_review_frame['highlightthickness'] = 1
        self.tp_review_frame.pack(side=TOP, padx=5)

        self.tv_test_cycle = Label(self.tp_review_frame, width=20)
        self.tv_test_cycle['text'] = 'Review info'
        self.tv_test_cycle['background'] = '#E8E9E9'
        self.tv_test_cycle['font'] = ('Calibri', 15, 'bold')
        self.tv_test_cycle.pack(padx=10, pady=10)

        self.tv_test_cycle_name = Label(self.tp_review_frame)
        self.tv_test_cycle_name['text'] = 'To be updated'
        self.tv_test_cycle_name['background'] = '#E8E9E9'
        self.tv_test_cycle_name['font'] = ('Calibri', 10)
        self.tv_test_cycle_name.pack(padx=10)

        self.tp_validate_button = Button(self.tp_review_frame)
        self.tp_validate_button['font'] = ('Calibri', 12)
        self.tp_validate_button['text'] = 'Review data'
        self.tp_validate_button.pack(fill=X, padx=10, pady=5)

        # Test plan data frame
        self.tp_data_frame = Frame(self.frame)
        self.tp_data_frame['width'] = 1920
        self.tp_data_frame['height'] = 700
        self.tp_data_frame['background'] = '#677756'
        self.tp_data_frame['highlightbackground'] = '#A9A9A9'
        self.tp_data_frame['highlightthickness'] = 1
        self.tp_data_frame.pack(side='right', fill='both', padx=2, pady=2)

        # Treeview vertical scrollbar
        self.sc_tree_vertical = Scrollbar(self.tp_data_frame)
        self.sc_tree_vertical.pack(side=RIGHT, fill=Y)

        # Treeview horizontal scrollbar
        self.sc_tree_horizontal = Scrollbar(self.tp_data_frame, orient='horizontal')
        self.sc_tree_horizontal.pack(side=BOTTOM, fill=X)

        # Test plan treeview
        self.tv_data = ttk.Treeview(self.tp_data_frame)
        self.tv_data['yscrollcommand'] = self.sc_tree_vertical.set
        self.tv_data['xscrollcommand'] = self.sc_tree_horizontal.set
        self.tv_data['columns'] = (1, 2, 3, 4, 5)
        self.tv_data['show'] = 'headings'
        self.tv_data['height'] = 1080
        self.tv_data.column(1, width=150, anchor='c')
        self.tv_data.column(2, width=200, anchor='c')
        self.tv_data.column(3, width=475, anchor='c')
        self.tv_data.column(4, width=200, anchor='c')
        self.tv_data.column(5, width=550, anchor='c')
        self.tv_data.heading(1, text='Property')
        self.tv_data.heading(2, text='Subproperty')
        self.tv_data.heading(3, text='Actual value')
        self.tv_data.heading(4, text='Validation')
        self.tv_data.heading(5, text='Comment')
        self.tv_data.insert('', 'end', iid=1, values=['Summary', '-'], tags=('init',))
        self.tv_data.insert('', 'end', iid=2, values=['Status', '-'], tags=('init',))
        self.tv_data.insert('', 'end', iid=3, values=['Primary Software', '-'], tags=('init',))
        self.tv_data.insert('', 'end', iid=4, values=['HW Revision', '-'], tags=('init',))
        self.tv_data.insert('', 'end', iid=5, values=['Configuration', 'Carrier'], tags=('init',))
        self.tv_data.insert('', 'end', iid=6, values=['Configuration', 'Serial Number'], tags=('init',))
        self.tv_data.insert('', 'end', iid=7, values=['Configuration', 'SIM Card'], tags=('init',))
        self.tv_data.insert('', 'end', iid=8, values=['Configuration', 'SD Card'], tags=('init',))
        self.tv_data.insert('', 'end', iid=9, values=['Configuration', 'HW Version/Revision'], tags=('init',))
        self.tv_data.pack(fill='both', padx=5, pady=5)

        # Tags for TreeView
        self.tv_data.tag_configure('init', font=('Helvetica', 10), foreground='#77878B', background='#E8E8E8')
        self.tv_data.tag_configure('fetched', font=('Helvetica', 11, 'bold'), foreground='#363636', background='#E8E8E8')
        self.tv_data.tag_configure('ok', font=('Helvetica', 11, 'bold'), foreground='#50C878', background='#E8E8E8')
        self.tv_data.tag_configure('not_ok', font=('Helvetica', 11, 'bold'), foreground='#880808', background='#F3E8EA')

        # Configure the vertical scrollbar
        self.sc_tree_vertical.config(command=self.tv_data.yview)

        # Configure the horizontal scrollbar
        self.sc_tree_horizontal.config(command=self.tv_data.xview)

        # Adding style to treeview
        self.style = ttk.Style(self.tp_data_frame)
        self.style.configure('Treeview',
                             foreground='black',
                             rowheight=50,
                             )
        self.style.map('Treeview', background=[('selected', '#ADD8E6')])

    def get_tp_id(self):
        return self.tp_id_entry.get()

    def set_tv_value(self, row, column, value):
        self.tv_data.set(row, column, value)

    def set_tv_tags(self, iid, tag):
        self.tv_data.item(iid, tags=tag)

    def set_core_id(self, core_id):
        self.core_id_label['text'] = core_id

    def set_test_cycle_name(self, test_cycle):
        self.tv_test_cycle_name['text'] = test_cycle

    def show_warning(self, title, message):
        messagebox.showwarning(title, message, parent=self.frame)

    def show_error(self, title, message):
        messagebox.showerror(title, message, parent=self.frame)
