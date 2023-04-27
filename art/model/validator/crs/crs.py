import re


class CRSValidator:
    def __init__(self, crs, android_version, expected_labels, expected_watchers):
        self.crs = crs
        self.num_crs = len(self.crs)
        self.android_version = android_version
        self.expected_labels = expected_labels
        self.expected_watchers = expected_watchers
        self.validations = list(map(lambda x: [x[0], [], False], self.crs))

    def validate_cr_project(self, index):
        cr_key = self.crs[index][0]
        if re.search('IKGAME*', cr_key):
            return True
        if self.android_version == 'Android 10 (Q)':
            if re.search('IKSWQ*', cr_key):
                return True
            else:
                self.validations[index][1].append('CR must be from SW Q RELEASE (IKSWQ) project!')
                return False
        if self.android_version == 'Android 11 (R)':
            if re.search('IKSWR*', cr_key):
                return True
            else:
                self.validations[index][1].append('CR must be from SW R RELEASE (IKSWR) project!')
                return False
        if self.android_version == 'Android 12 (S)':
            if re.search('IKSWS*', cr_key):
                return True
            else:
                self.validations[index][1].append('CR must be from SW S RELEASE (IKSWS) project!')
                return False
        if self.android_version == 'Android 13 (T)':
            if re.search('IKSWT*', cr_key):
                return True
            else:
                self.validations[index][1].append('CR must be from SW T RELEASE (IKSWT) project!')
                return False
        if self.android_version == 'Android 14 (U)':
            if re.search('IKSWU*', cr_key):
                return True
            else:
                self.validations[index][1].append('CR must be from SW U RELEASE (IKSWU) project!')
                return False

    def validate_cr_status(self, index):
        if self.crs[index][1] != 'Closed':
            return True
        else:
            self.validations[index][1].append('CR status can not be Closed!')
            return False

    def validate_cr_labels(self, index, expected_labels):
        for expected_label in expected_labels:
            if expected_label not in self.crs[index][2]:
                self.validations[index][1].append('Label ' + expected_label + ' needs to be added!')
                return False
        return True

    def validate_cr_watchers(self, index, expected_watchers):
        for expected_watcher in expected_watchers:
            if expected_watcher not in self.crs[index][3]:
                self.validations[index][1].append('Watcher ' + expected_watcher + ' needs to be added!')
                return False
        return True

    def validate_all(self):
        for i in range(self.num_crs):
            result = self.validate_cr_project(i) and self.validate_cr_status(i) and \
                     self.validate_cr_labels(i, self.expected_labels) and \
                     self.validate_cr_watchers(i, self.expected_watchers)
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
