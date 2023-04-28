class TestPlan:
    def __init__(self, zephyr_connection, test_cycle_id):
        try:
            self.zephyr_connection = zephyr_connection
            self.test_cycle_issue = self.zephyr_connection.api.test_cycles.get_test_cycle(test_cycle_id)
            self.test_cycle_data = []
            self.set_test_cycle_data()
        except Exception as e:
            print('The issue ID is invalid or does not exist!\n' + str(e))
            self.test_cycle_issue = None

    def get_name(self):
        try:
            return self.test_cycle_issue['name']
        except Exception as e:
            print('Unable to get the status\n' + str(e))
            return None

    def get_description(self):
        try:
            return self.test_cycle_issue['description']
        except Exception as e:
            print('Unable to get the status\n' + str(e))
            return None

    def get_status(self):
        try:
            status = self.test_cycle_issue['status']
            status_issue = self.zephyr_connection.api.statuses.get_status(status['id'])
            return status_issue['name']
        except Exception as e:
            print('Unable to get the status\n' + str(e))
            return None

    def set_test_cycle_data(self):
        try:
            self.test_cycle_data.append(self.get_status())
        except Exception as e:
            print('Unable to set the test cycle data!\n' + str(e))
