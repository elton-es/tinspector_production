from jira import JIRAError


class TestCases:
    def __init__(self, dalek_connection, tp_id):
        self.dalek_connection = dalek_connection
        try:
            self.tp_issue = self.dalek_connection.issue(tp_id)
            if self.check_if_is_tp():
                self.test_cases_ids = []
                self.test_cases_issues = []
                self.set_test_cases_ids()
                self.set_tcs_issues()
                self.num_tcs = self.get_number_of_tcs()
                self.test_cases_data = []
                self.set_tcs_data()
        except JIRAError as e:
            print('The issue ID is invalid or does not exist!\n' + str(e))
            self.tp_issue = None

    def get_number_of_tcs(self):
        return len(self.test_cases_issues)

    def get_cycle_name(self):
        return self.tp_issue.fields.customfield_10101

    def get_number_of_crs(self):
        count = 0
        for i in range(self.num_tcs):
            if self.get_remote_defect_cr_from_tc(i) != '':
                count += 1
        return count

    def set_test_cases_ids(self):
        for i in range(len(self.tp_issue.fields.issuelinks)):
            key = self.tp_issue.fields.issuelinks[i].outwardIssue.raw['key']
            self.test_cases_ids.append(key)

    def set_tcs_issues(self):
        keys_to_be_removed = []
        for key in self.test_cases_ids:
            tc_issue = self.dalek_connection.issue(key)
            if tc_issue.fields.issuetype.name == 'Test Case Execution':
                self.test_cases_issues.append(tc_issue)
            else:
                keys_to_be_removed.append(key)
        for key in keys_to_be_removed:
            self.test_cases_ids.remove(key)

    def set_tcs_data(self):
        for i in range(self.num_tcs):
            self.test_cases_data.append([])
            self.test_cases_data[i].append(self.get_key_from_tc(i))
            self.test_cases_data[i].append(self.get_test_results_from_tc(i))
            self.test_cases_data[i].append(self.get_remote_defect_cr_from_tc(i))
            self.test_cases_data[i].append(self.get_explanation_from_tc(i))
            self.test_cases_data[i].append(self.get_comments_from_tc(i))

    def get_tcs_issues(self):
        return self.test_cases_issues

    def get_key_from_tc(self, index):
        key = self.test_cases_issues[index].key
        return '' if key is None else key

    def get_test_results_from_tc(self, index):
        test_results = self.test_cases_issues[index].fields.customfield_10148.value
        return '' if test_results is None else test_results

    def get_remote_defect_cr_from_tc(self, index):
        cr = self.test_cases_issues[index].fields.customfield_10150
        return '' if cr is None else cr

    def get_explanation_from_tc(self, index):
        explanation = self.test_cases_issues[index].fields.customfield_10901
        return '' if explanation is None else explanation

    def get_comments_from_tc(self, index):
        comments = []
        for comment in self.test_cases_issues[index].fields.comment.comments:
            comments.append(comment.body)
        return comments

    def check_if_is_tp(self):
        return self.tp_issue.fields.issuetype.name == 'Test Plan'
