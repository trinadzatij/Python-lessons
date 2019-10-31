#!/usr/bin/env python3

interface = input('Enter interface type and number: \n')
vlan = input('Enter vlan number: \n')

access_template=['switchport mode access',
                'switchport access vlan {}',
                'switchport nonegotiate',
                'spanning-tree portfast',
                'spanning-tree bpduguard enable']

print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
