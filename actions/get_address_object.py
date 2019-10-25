from lib.action import FortinetBaseAction


class GetAddressObject(FortinetBaseAction):
    def run(self, name=None, filters=None):
        addresses = self.device.get_firewall_address(name, filters=filters)
        if isinstance(addresses, list):
            return True, addresses
        return False, addresses
