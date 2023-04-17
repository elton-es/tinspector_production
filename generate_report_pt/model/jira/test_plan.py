from jira import JIRAError


class TestPlan:
    def __init__(self, dalek_connection, tp_id):
        try:
            self.tp_issue = dalek_connection.issue(tp_id)
        except JIRAError as e:
            print('The issue ID is invalid or does not exist!\n' + str(e))
            self.tp_issue = None

    def get_tp_field(self, field):
        try:
            if field == 'summary':
                return self.tp_issue.fields.summary
            elif field == 'status':
                return self.tp_issue.fields.status.name
            elif field == 'build':
                return self.tp_issue.fields.customfield_10120
            elif field == 'configuration':
                return self.tp_issue.fields.customfield_10122
            elif field == 'hw_revision':
                return self.tp_issue.fields.customfield_10514.value
            else:
                return 'Please, provide a valid field'
        except JIRAError as e:
            print('Issue Does Not Exist\n' + str(e))
            return 'Please, provide a valid issue'

    def check_if_is_tp(self):
        return self.tp_issue.fields.issuetype.name == 'Test Plan'
