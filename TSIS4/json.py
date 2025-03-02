import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

for interface in data['imdata']:
    attributes = interface['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))