from lib.action import FortinetBaseAction


class GetAddressObject(FortinetBaseAction):
    def run(self, specific=None, filters=None):
        addresses = self.device.get_firewall_address(specific=specific, filters=filters)
        if isinstance(addresses, list):
            return True, addresses
        return False, addresses
