import re


class TestCasesValidator:
    def __init__(self, test_cases, android_version):
        self.test_cases = test_cases
        self.num_tcs = len(self.test_cases)
        self.android_version = android_version
        self.validations = list(map(lambda x: [x[0], [], False], self.test_cases))

    def validate_test_results(self, index):
        if self.test_cases[index][1] in ['Pass', 'Fail', 'Delete']:
            return True
        else:
            self.validations[index][1].append('Test results must be Pass, Fail, or Delete!')
            return False

    def validate_remote_defect_cr(self, index):
        remote_defect_cr = self.test_cases[index][2]
        if self.test_cases[index][1] in ['Pass', 'Delete']:
            if remote_defect_cr in [None, '']:
                return True
            else:
                self.validations[index][1].append('Remote defect CR should be empty!')
                return False
        elif self.test_cases[index][1] == 'Fail':
            if re.search('^(IKGAME-)[0-9]*', remote_defect_cr):
                return True
            if self.android_version == 10:
                if re.search('^(IKSWQ-)[0-9]*', remote_defect_cr):
                    return True
                else:
                    self.validations[index][1].append('CR must be from Android Q project')
                    return False
            elif self.android_version == 11:
                if re.search('^(IKSWR-)[0-9]*', remote_defect_cr):
                    return True
                else:
                    self.validations[index][1].append('CR must be from Android R project')
                    return False
            elif self.android_version == 12:
                if re.search('^(IKSWS-)[0-9]*', remote_defect_cr):
                    return True
                else:
                    self.validations[index][1].append('CR must be from Android S project')
                    return False
            elif self.android_version == 13:
                if re.search('^(IKSWT-)[0-9]*', remote_defect_cr):
                    return True
                else:
                    self.validations[index][1].append('CR must be from Android T project')
                    return False
            elif self.android_version == 14:
                if re.search('^(IKSWU-)[0-9]*', remote_defect_cr):
                    return True
                else:
                    self.validations[index][1].append('CR must be from Android U project')
                    return False
        else:
            return False

    def validate_explanation(self, index):
        remote_defect_cr = self.test_cases[index][2]
        explanation = self.test_cases[index][3]
        if self.test_cases[index][1] == 'Pass':
            return True
        elif self.test_cases[index][1] == 'Delete':
            return not(self.test_cases[index][3] in [None, ''])
        elif self.test_cases[index][1] == 'Fail':
            if remote_defect_cr in [None, '']:
                return False
            if re.search('.*' + remote_defect_cr + '.*', explanation):
                return True
            else:
                self.validations[index][1].append('Explanation must be in format \"CR Key - Short description\"')
                return False
        else:
            return False

    def validate_comments(self, index):
        if not self.test_cases[index][4]:
            self.validations[index][1].append('Comment can\'t be empty')
            return False
        elif len(self.test_cases[index][4]) > 1:
            self.validations[index][1].append('Keep only one comment in this TC')
            return False
        else:
            lines = str(self.test_cases[index][4][0]).split('\r\n')
            lines = list(map(lambda x: x.lower(), lines))
            any([item for item in lines if 'serial' in item])
            if any([item for item in lines if 'serial' in item]):
                if any([item for item in lines if 'build' in item]):
                    return True
                else:
                    self.validations[index][1].append('Build ID must be present in comment')
            else:
                self.validations[index][1].append('Build ID must be present in comment')
                return False

    def validate_all(self):
        for i in range(self.num_tcs):
            result = self.validate_test_results(i) and self.validate_remote_defect_cr(i) and \
                     self.validate_explanation(i) and self.validate_comments(i)
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
