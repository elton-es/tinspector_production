from jira import JIRAError


class CRs:
    def __init__(self, dalek_connection, idart_connection, tp_id):
        self.dalek_connection = dalek_connection
        try:
            self.tp_issue = self.dalek_connection.issue(tp_id)
            if self.check_if_is_tp():
                self.idart_connection = idart_connection
                self.number_of_failed_tcs = 0
                self.number_of_linked_crs = 0
                self.test_cases_ids = []
                self.failed_tcs_issues = []
                self.linked_crs_ids = []
                self.crs_issues = []
                self.set_test_cases_ids()
                self.set_failed_tcs_issues()
                self.set_linked_crs_ids()
                self.set_crs_issues()
                self.set_number_of_failed_tcs()
                self.set_number_of_linked_crs()
                self.crs_data = []
                self.set_crs_data()
        except JIRAError as e:
            print('The issue ID is invalid or does not exist!\n' + str(e))
            self.tp_issue = None

    def set_test_cases_ids(self):
        for issue in self.tp_issue.fields.issuelinks:
            if issue.outwardIssue.fields.issuetype.name == 'Test Case Execution':
                self.test_cases_ids.append(issue.outwardIssue.key)

    def set_failed_tcs_issues(self):
        keys_to_be_removed = []
        for key in self.test_cases_ids:
            tc_issue = self.dalek_connection.issue(key)
            if tc_issue.fields.customfield_10150 is None:
                keys_to_be_removed.append(key)
            else:
                self.failed_tcs_issues.append(tc_issue)
        for key in keys_to_be_removed:
            self.test_cases_ids.remove(key)

    def set_linked_crs_ids(self):
        for issue in self.failed_tcs_issues:
            for cr_id in issue.fields.customfield_10150.split(','):
                self.linked_crs_ids.append(cr_id)

    def set_crs_issues(self):
        for key in self.linked_crs_ids:
            cr_issue = self.idart_connection.issue(key)
            self.crs_issues.append(cr_issue)

    def set_crs_data(self):
        for i in range(self.number_of_linked_crs):
            self.crs_data.append([])
            self.crs_data[i].append(self.get_key_from_cr(i))
            self.crs_data[i].append(self.get_status_from_cr(i))
            self.crs_data[i].append(self.get_labels_from_cr(i))
            self.crs_data[i].append(self.get_watchers_from_cr(i))
            self.crs_data[i].append(self.get_comments_from_cr(i))

    def set_number_of_failed_tcs(self):
        self.number_of_failed_tcs = len(self.failed_tcs_issues)

    def get_cycle_name(self):
        return self.tp_issue.fields.customfield_10101

    def set_number_of_linked_crs(self):
        self.number_of_linked_crs = len(self.crs_issues)

    def get_key_from_cr(self, index):
        key = self.crs_issues[index].key
        return '' if key is None else key

    def get_status_from_cr(self, index):
        return self.crs_issues[index].fields.status.name

    def get_labels_from_cr(self, index):
        return self.crs_issues[index].fields.labels

    def get_watchers_from_cr(self, index):
        return [watcher.name for watcher in self.idart_connection.watchers(self.crs_issues[index]).watchers]

    def get_comments_from_cr(self, index):
        return self.crs_issues[index].fields.comment.comments

    def check_if_is_tp(self):
        return self.tp_issue.fields.issuetype.name == 'Test Plan'
