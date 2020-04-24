from itertools import count

from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzServiceError


def get_wlan_status(fc):
    status = []
    action = 'GetInfo'
    for n in count(1):
        service = f'WLANConfiguration{n}'
        try:
            result = fc.call_action(service, action)
        except FritzServiceError:
            break
        status.append((service, result))
    return status


def get_compact_wlan_status(fc):
    keys = ('NewSSID', 'NewChannel', 'NewStatus')
    return [
        (service, {key[3:]: status[key] for key in keys})
        for service, status in get_wlan_status(fc)
    ]


def main(address, password):
    fc = FritzConnection(address=address, password=password)
    for service, status in get_compact_wlan_status(fc):
        print(f'{service}: {status}')


if __name__ == '__main__':
    main(address='192.168.2.1', password='Fr@010265')
