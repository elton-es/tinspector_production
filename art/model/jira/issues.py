from jira import JIRAError


class Issues:
    def __init__(self, zephyr_connection, jira_connection, test_cycle_id):
        self.zephyr_connection = zephyr_connection
        self.jira_connection = jira_connection
        try:
            self.test_cycle_issue = self.zephyr_connection.api.test_cycles.get_test_cycle(test_cycle_id)
            if self.test_cycle_issue:
                self.number_of_failed_test_executions = 0
                self.number_of_linked_issues = 0
                self.test_executions_ids = []
                self.failed_test_executions_issues = []
                self.linked_issues_ids = []
                self.issues_objects = []
                self.set_test_executions_ids()
                self.set_failed_test_executions_issues()
                self.set_linked_issues_ids_and_objects()
                self.set_number_of_failed_test_executions()
                self.set_number_of_linked_issues()
                self.issues_data = []
                self.set_issues_data()
        except Exception as e:
            print('The issue ID is invalid or does not exist!\n' + str(e))
            self.test_cycle_issue = None

    def set_test_executions_ids(self):
        test_executions = self.zephyr_connection.api.test_executions.get_test_executions()
        for test_execution in test_executions:
            if test_execution['testCycle']['id'] == self.test_cycle_issue['id']:
                self.test_executions_ids.append(test_execution['key'])

    def set_failed_test_executions_issues(self):
        for key in self.test_executions_ids:
            test_execution_issue = self.zephyr_connection.api.test_executions.get_test_execution(key)
            number_of_linked_issues = len(test_execution_issue['links']['issues'])
            if number_of_linked_issues > 0:
                self.failed_test_executions_issues.append(test_execution_issue)

    def set_linked_issues_ids_and_objects(self):
        for test_execution_issue in self.failed_test_executions_issues:
            linked_issues = test_execution_issue['links']['issues']
            for linked_issue in linked_issues:
                id_zephyr = linked_issue['issueId']
                issue_object = self.jira_connection.issue(id_zephyr)
                id_jira = issue_object.key
                self.linked_issues_ids.append(id_jira)
                self.issues_objects.append(issue_object)

    def set_issues_data(self):
        for i in range(self.number_of_linked_issues):
            self.issues_data.append([])
            self.issues_data[i].append(self.get_key_from_issue(i))
            self.issues_data[i].append(self.get_status_from_issue(i))
            self.issues_data[i].append(self.get_labels_from_issue(i))
            self.issues_data[i].append(self.get_watchers_from_issue(i))
            self.issues_data[i].append(self.get_comments_from_issue(i))

    def set_number_of_failed_test_executions(self):
        self.number_of_failed_test_executions = len(self.failed_test_executions_issues)

    def set_number_of_linked_issues(self):
        self.number_of_linked_issues = len(self.issues_objects)

    def get_key_from_issue(self, index):
        key = self.issues_objects[index].key
        return '' if key is None else key

    def get_status_from_issue(self, index):
        return self.issues_objects[index].fields.status.name

    def get_labels_from_issue(self, index):
        return self.issues_objects[index].fields.labels

    def get_watchers_from_issue(self, index):
        return [watcher.displayName for watcher in self.jira_connection.watchers(self.issues_objects[index]).watchers]

    def get_comments_from_issue(self, index):
        return self.issues_objects[index].fields.comment.comments
