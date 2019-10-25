from lib.action import FortinetBaseAction


class GetAddressObject(FortinetBaseAction):
    def run(self, name=None, filter=None):
        addresses = self.device.get_firewall_address(name, filter=filter)
        if isinstance(addresses, list):
            return True, addresses
        return False, addresses
