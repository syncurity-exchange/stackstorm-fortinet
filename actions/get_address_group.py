from lib.action import FortinetBaseAction


class GetAddressGroup(FortinetBaseAction):
    def run(self, name=None, filters=None):
        addresses = self.device.get_address_group(name, filters=None)
        if isinstance(addresses, list):
            return True, addresses
        return False, addresses
