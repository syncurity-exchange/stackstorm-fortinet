from lib.action import FortinetBaseAction


class UpdateAddressGroup(FortinetBaseAction):
    def run(self, name=None, member=None):

        group_members = self.device.get_address_group(name)
        print(group_members)
        new_member = {'name': member, 'q_origin_key': member}
        group_members[0][member].append(new_member)
        payload = "{\'member\': " + str(group_members[0]['member']) + "}"
        status_code = self.device.update_address_group(name, payload)
        if status_code == 200:
            return True, status_code
        return False, status_code
