from lib.action import FortinetBaseAction


class GetAddressGroup(FortinetBaseAction):
    def run(self, name=None, output_format=''):
        addresses = self.device.get_address_group(name, output_format=output_format)
        if isinstance(addresses, list):
            return True, addresses
        return False, addresses
