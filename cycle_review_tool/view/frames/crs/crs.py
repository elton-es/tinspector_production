from tkinter import *
from tkinter import ttk, messagebox


class CRs:
    def __init__(self, window):
        self.frame = Frame(window)

        # CRs params frame
        self.crs_params_frame = Frame(self.frame)
        self.crs_params_frame['width'] = 500
        self.crs_params_frame['height'] = 700
        self.crs_params_frame['background'] = '#677756'
        self.crs_params_frame['highlightbackground'] = '#A9A9A9'
        self.crs_params_frame['highlightthickness'] = 1
        self.crs_params_frame.pack(side='left', fill='y', padx=2, pady=2)

        # Frame for general info
        self.crs_general_frame = Frame(self.crs_params_frame)
        self.crs_general_frame['highlightbackground'] = 'silver'
        self.crs_general_frame['background'] = '#E8E9E9'
        self.crs_general_frame['highlightthickness'] = 1
        self.crs_general_frame.pack(side=TOP, padx=5, pady=5)

        # Params
        self.view_name_label = Label(self.crs_general_frame, width=20)
        self.view_name_label['text'] = 'CRs View'
        self.view_name_label['background'] = '#E8E9E9'
        self.view_name_label['font'] = ('Calibri', 15, 'bold')
        self.view_name_label.pack(padx=10, pady=10)

        self.core_id_label = Label(self.crs_general_frame)
        self.core_id_label['text'] = 'Core ID:'
        self.core_id_label['background'] = '#E8E9E9'
        self.core_id_label['font'] = ('Calibri', 12)
        self.core_id_label.pack(padx=10, pady=10)

        self.tp_id_label = Label(self.crs_general_frame)
        self.tp_id_label['text'] = 'Test Plan ID'
        self.tp_id_label['background'] = '#E8E9E9'
        self.tp_id_label['font'] = ('Calibri', 12)
        self.tp_id_label.pack(padx=10, pady=10)

        self.tp_id_entry = Entry(self.crs_general_frame)
        self.tp_id_entry['font'] = ('Calibri', 12)
        self.tp_id_entry['justify'] = 'center'
        self.tp_id_entry.pack(fill=X, padx=10)

        self.tp_search_button = Button(self.crs_general_frame)
        self.tp_search_button['font'] = ('Calibri', 12)
        self.tp_search_button['text'] = 'Search TP'
        self.tp_search_button.pack(pady=10, padx=10, fill=X)

        # Frame for review info
        self.crs_review_frame = Frame(self.crs_params_frame)
        self.crs_review_frame['background'] = '#E8E9E9'
        self.crs_review_frame['highlightbackground'] = 'silver'
        self.crs_review_frame['highlightthickness'] = 1
        self.crs_review_frame.pack(side=TOP, padx=5)

        self.tv_test_cycle = Label(self.crs_review_frame, width=20)
        self.tv_test_cycle['text'] = 'Review info'
        self.tv_test_cycle['background'] = '#E8E9E9'
        self.tv_test_cycle['font'] = ('Calibri', 15, 'bold')
        self.tv_test_cycle.pack(padx=10, pady=10)

        self.tv_test_cycle_name = Label(self.crs_review_frame)
        self.tv_test_cycle_name['text'] = 'To be updated'
        self.tv_test_cycle_name['background'] = '#E8E9E9'
        self.tv_test_cycle_name['font'] = ('Calibri', 10)
        self.tv_test_cycle_name.pack(padx=10)

        self.tv_failed_tcs_number = Label(self.crs_review_frame)
        self.tv_failed_tcs_number['text'] = 'Number of failed TCs:'
        self.tv_failed_tcs_number['background'] = '#E8E9E9'
        self.tv_failed_tcs_number['font'] = ('Calibri', 10)
        self.tv_failed_tcs_number.pack(padx=10)

        self.tv_crs_number = Label(self.crs_review_frame)
        self.tv_crs_number['text'] = 'Number of CRs:'
        self.tv_crs_number['background'] = '#E8E9E9'
        self.tv_crs_number['font'] = ('Calibri', 10)
        self.tv_crs_number.pack(padx=10)

        self.tv_android_version = Label(self.crs_review_frame)
        self.tv_android_version['text'] = 'Choose the Android Version'
        self.tv_android_version['background'] = '#E8E9E9'
        self.tv_android_version['font'] = ('Calibri', 12)
        self.tv_android_version.pack(padx=10, pady=5)

        self.lb_android_version = Listbox(self.crs_review_frame)
        self.lb_android_version['height'] = 5
        self.lb_android_version['justify'] = 'center'
        self.lb_android_version.insert(END, 'Android 10 (Q)')
        self.lb_android_version.insert(END, 'Android 11 (R)')
        self.lb_android_version.insert(END, 'Android 12 (S)')
        self.lb_android_version.insert(END, 'Android 13 (T)')
        self.lb_android_version.insert(END, 'Android 14 (U)')
        self.lb_android_version['font'] = ('Calibri', 10)
        self.lb_android_version.pack(padx=10)

        self.tv_labels = Label(self.crs_review_frame)
        self.tv_labels['text'] = 'Type in the device\'s labels'
        self.tv_labels['background'] = '#E8E9E9'
        self.tv_labels['font'] = ('Calibri', 12)
        self.tv_labels.pack(padx=10, pady=5)

        self.labels_text = Text(self.crs_review_frame)
        self.labels_text['width'] = 30
        self.labels_text['height'] = 4
        self.labels_text['font'] = ('Calibri', 10)
        self.labels_text.pack(fill=X, padx=10)

        self.tv_watchers = Label(self.crs_review_frame)
        self.tv_watchers['text'] = 'Type in the watchers'
        self.tv_watchers['background'] = '#E8E9E9'
        self.tv_watchers['font'] = ('Calibri', 12)
        self.tv_watchers.pack(padx=10, pady=5)

        self.watchers_text = Text(self.crs_review_frame)
        self.watchers_text['width'] = 20
        self.watchers_text['height'] = 4
        self.watchers_text['font'] = ('Calibri', 10)
        self.watchers_text.pack(fill=X, padx=10)

        self.tp_validate_button = Button(self.crs_review_frame)
        self.tp_validate_button['font'] = ('Calibri', 12)
        self.tp_validate_button['text'] = 'Review data'
        self.tp_validate_button['state'] = 'disabled'
        self.tp_validate_button.pack(fill=X, padx=10, pady=5)

        # CRs data frame
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

        # CRs treeview
        self.tv_data = ttk.Treeview(self.tc_data_frame)
        self.tv_data['yscrollcommand'] = self.sc_tree_vertical.set
        self.tv_data['xscrollcommand'] = self.sc_tree_horizontal.set
        self.tv_data['columns'] = (1, 2, 3, 4, 5, 6, 7)
        self.tv_data['show'] = 'headings'
        self.tv_data['height'] = 1080
        self.tv_data.column(1, width=150, anchor='c')
        self.tv_data.column(2, width=150, anchor='c')
        self.tv_data.column(3, width=200, anchor='c')
        self.tv_data.column(4, width=200, anchor='c')
        self.tv_data.column(5, width=400, anchor='c')
        self.tv_data.column(6, width=100, anchor='c')
        self.tv_data.column(7, width=400, anchor='c')
        self.tv_data.heading(1, text='Key')
        self.tv_data.heading(2, text='CR Status')
        self.tv_data.heading(3, text='Expected labels')
        self.tv_data.heading(4, text='Expected watchers')
        self.tv_data.heading(5, text='Comments')
        self.tv_data.heading(6, text='Validation')
        self.tv_data.heading(7, text='Notes')
        self.tv_data.pack(fill='both', padx=5, pady=5)

        # Create 400 rows
        for i in range(50):
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
        self.style.configure('Treeview', foreground='black', rowheight=70)
        self.style.map('Treeview', background=[('selected', '#ADD8E6')])

    def get_tp_id(self):
        return self.tp_id_entry.get()

    def get_android_version(self):
        return self.lb_android_version.get(ANCHOR)

    def get_devices_labels(self):
        return self.labels_text.get(1.0, END)

    def get_watchers(self):
        return self.watchers_text.get(1.0, END)

    def set_tv_value(self, row, column, value):
        self.tv_data.set(row, column, value)

    def set_tv_tags(self, iid, tag):
        self.tv_data.item(iid, tags=tag)

    def set_core_id(self, core_id):
        self.core_id_label['text'] = core_id

    def set_test_cycle_name(self, test_cycle):
        self.tv_test_cycle_name['text'] = test_cycle

    def set_number_of_failed_tcs(self, number):
        self.tv_failed_tcs_number['text'] = number

    def set_number_of_crs(self, number):
        self.tv_crs_number['text'] = number

    def show_warning(self, title, message):
        messagebox.showwarning(title, message, parent=self.frame)

    def show_error(self, title, message):
        messagebox.showerror(title, message, parent=self.frame)

    def enable_validate_button(self):
        self.tp_validate_button['state'] = 'normal'

    def disable_validate_button(self):
        self.tp_validate_button['state'] = 'disabled'
