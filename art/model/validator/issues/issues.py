import re


class IssuesValidator:
    def __init__(self, values, expected_labels, expected_watchers):
        self.values = values
        self.number_of_issues = len(self.values)
        self.expected_labels = expected_labels
        self.expected_watchers = expected_watchers
        self.validations = list(map(lambda x: [x[0], [], False], self.values))

    def validate_issue_project(self, index):
        issue_key = self.values[index][0]
        if re.search('UN*', issue_key):
            return True
        else:
            self.validations[index][1].append('The issue must be from UX Nator (UN) project!')
            return False

    def validate_issue_status(self, index):
        status = self.values[index][1]
        if status != 'Done':
            return True
        else:
            self.validations[index][1].append('Issue status can not be Done!')
            return False

    def validate_issue_labels(self, index):
        for expected_label in self.expected_labels:
            if expected_label not in self.values[index][2]:
                self.validations[index][1].append('Label ' + expected_label + ' needs to be added!')
                return False
        return True

    def validate_issue_watchers(self, index):
        for expected_watcher in self.expected_watchers:
            if expected_watcher not in self.values[index][3]:
                self.validations[index][1].append('Watcher ' + expected_watcher + ' needs to be added!')
                return False
        return True

    def validate_issue_comments(self, index):
        if self.values[index][4]:
            comment = self.values[index][4][0].body
            if 'OS' in comment and 'Browser' in comment:
                return True
            else:
                self.validations[index][1].append('OS and Browser must be informed in comments!')
                return False
        else:
            self.validations[index][1].append('Comment can not be empty!')
            return False

    def validate_all(self):
        for i in range(self.number_of_issues):
            validation = self.validate_issue_project(i)
            validation = self.validate_issue_status(i) and validation
            validation = self.validate_issue_labels(i) and validation
            validation = self.validate_issue_watchers(i) and validation
            validation = self.validate_issue_comments(i) and validation
            self.validations[i][2] = validation
        return self.validations

    def generate_actions_message(self):
        message = """"""
        for validation in self.validations:
            if not validation[2]:
                message += 'On ' + validation[0] + ':\n'
                for action in validation[1]:
                    message += '    ' + action + '\n'
        if message == """""":
            print('No actions are needed')
        else:
            print(message)
