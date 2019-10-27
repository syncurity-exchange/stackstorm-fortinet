from lib.action import FortinetBaseAction


class GetSingleAddressObject(FortinetBaseAction):
    def run(self, specific=None, filters=None, ip_address=None):
        addresses = self.device.get_firewall_address(specific=specific, filters=filters)
        if isinstance(addresses, list):
            if ip_address:
                for item in addresses:
                    if 'subnet' in item.keys() and ip_address in item.get('subnet'):
                        return True, item
        return False, {'status': ip_address + ' not found in address objects'}
