from lib.action import FortinetBaseAction


class GetSingleAddressObject(FortinetBaseAction):
    def run(self, filters=None, ip_address=None):
        addresses = self.device.get_firewall_address()
        if isinstance(addresses, list):
            if ip_address:
                for item in addresses:
                    if 'subnet' in item.keys() and ip_address in item.get('subnet'):
                        item['found'] = True
                        return True, item
                    else:
                        return True, {'status': ip_address + ' not found in address objects',
                                      'found': False, 'results': item}
        return False, addresses
