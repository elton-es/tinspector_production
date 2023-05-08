class TestCasesValidator:
    def __init__(self, values):
        self.values = values
        self.num_test_executions = len(self.values)
        self.validations = list(map(lambda x: [x[0], [], False], self.values))

    def validate_environment(self, index):
        environment = self.values[index][1]
        valid_environments = ['Ubuntu 18.04', 'Ubuntu 20.04', 'Ubuntu 22.04', 'Windows 10', 'Windows 11']
        if not environment:
            self.validations[index][1].append('Environment can not be empty')
            return False
        elif environment in valid_environments:
            return True
        else:
            self.validations[index][1].append('The Environment must be Ubuntu or Windows!')
            return False

    def validate_test_results(self, index):
        test_results = self.values[index][2]
        if not test_results:
            self.validations[index][1].append('Test Results can not be empty!')
            return False
        elif test_results == 'Pass':
            return True
        elif test_results == 'Fail':
            issues = self.values[index][4]
            if not issues:
                self.validations[index][1].append('Issues must be informed!')
                return False
            else:
                return self.validate_issues(index)
        else:
            self.validations[index][1].append('The test results must be Pass or Fail!')
            return False

    def validate_comment(self, index):
        environment = self.values[index][1]
        comment = self.values[index][3]
        if not comment:
            self.validations[index][1].append('Comment can not be empty')
            return False
        elif not environment:
            self.validations[index][1].append('Environment can not be empty')
            return False
        elif environment in comment and 'Browser' in comment:
            return True
        else:
            self.validations[index][1].append('Operating System and Browser must be present in comment!')
            return False

    def validate_issues(self, index):
        issues = self.values[index][4]
        for issue in issues:
            if 'UN-' not in issue:
                self.validations[index][1].append('The issue must be from UX Nator (UN) project')
                return False
        return True

    def validate_all(self):
        for i in range(self.num_test_executions):
            result = self.validate_environment(i)
            result = self.validate_test_results(i) and result
            result = self.validate_comment(i) and result
            self.validations[i][2] = result
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
