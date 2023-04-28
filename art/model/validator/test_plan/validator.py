import re


class Validator:

    def __init__(self, values):
        self.status = values[0]
        self.validations = ['', False]

    def validate_status(self):
        if self.status == 'Done':
            self.validations[1] = True
            return True
        else:
            self.validations[0] = 'The status needs to be Done!'
            return False
