class TestCases:
    def __init__(self, zephyr_connection, jira_connection, test_cycle_id):
        self.zephyr_connection = zephyr_connection
        self.jira_connection = jira_connection
        try:
            self.test_cycle_issue = self.zephyr_connection.api.test_cycles.get_test_cycle(test_cycle_id)
            if self.test_cycle_issue:
                self.test_executions_keys = []
                self.test_executions_issues = []
                self.set_test_executions_keys_and_issues()
                self.number_of_test_executions = 0
                self.set_number_of_test_executions()
                self.number_of_failed_test_executions = 0
                self.number_of_issues = 0
                self.set_number_of_failed_test_executions_and_issues()
                self.test_executions_data = []
                self.set_test_executions_data()
        except Exception as e:
            print('The Test Cycle ID is invalid or does not exist!\n' + str(e))
            self.test_cycle_issue = None

    def set_test_executions_keys_and_issues(self):
        try:
            test_executions = self.zephyr_connection.api.test_executions.get_test_executions()
            for test_execution in test_executions:
                if test_execution['testCycle']['id'] == self.test_cycle_issue['id']:
                    self.test_executions_keys.append(test_execution['key'])
                    self.test_executions_issues.append(test_execution)
        except Exception as e:
            print('Unable to set up the test executions ids and issues!\n' + str(e))

    def get_test_execution_key(self, index):
        try:
            return self.test_executions_keys[index]
        except Exception as e:
            print('Unable to get the test execution key!\n' + str(e))
            return None

    def set_number_of_test_executions(self):
        try:
            self.number_of_test_executions = len(self.test_executions_keys)
        except Exception as e:
            print('Unable to set up the number of test executions!\n' + str(e))

    def get_environment(self, index):
        try:
            environment = self.test_executions_issues[index]['environment']
            environment_issue = self.zephyr_connection.api.environments.get_environment(environment['id'])
            return environment_issue['name']
        except Exception as e:
            print('Unable to get the test execution environment!\n' + str(e))
            return None

    def get_test_result(self, index):
        try:
            status = self.test_executions_issues[index]['testExecutionStatus']
            status_issue = self.zephyr_connection.api.statuses.get_status(status['id'])
            return status_issue['name']
        except Exception as e:
            print('Unable to get the test execution result!\n' + str(e))
            return None

    def get_comment(self, index):
        try:
            return self.test_executions_issues[index]['comment']
        except Exception as e:
            print('Unable to get the test execution comment!\n' + str(e))
            return None

    def get_issues_keys(self, index):
        try:
            issues_keys = []
            issues = self.test_executions_issues[index]['links']['issues']
            for issue in issues:
                issue_object = self.jira_connection.issue(issue['issueId'])
                issues_keys.append(issue_object.key)
            return issues_keys
        except Exception as e:
            print('Unable to get the issues keys!\n' + str(e))
            return None

    def set_number_of_failed_test_executions_and_issues(self):
        try:
            issues = []
            for i in range(self.number_of_test_executions):
                test_result = self.get_test_result(i)
                if test_result == 'Fail':
                    self.number_of_failed_test_executions += 1
                    issues_keys = self.get_issues_keys(i)
                    for issue in issues_keys:
                        if issue not in issues:
                            issues.append(issue)
            self.number_of_issues = len(issues)
        except Exception as e:
            print('Unable to set the number of failed test executions and issues!\n' + str(e))

    def set_test_executions_data(self):
        for i in range(self.number_of_test_executions):
            self.test_executions_data.append([])
            self.test_executions_data[i].append(self.test_executions_keys[i])
            self.test_executions_data[i].append(self.get_environment(i))
            self.test_executions_data[i].append(self.get_test_result(i))
            self.test_executions_data[i].append(self.get_comment(i))
            self.test_executions_data[i].append(self.get_issues_keys(i))
