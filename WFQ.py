#Input packets as a string, S=Stard, P=Priority, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen", \
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",\
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",\
                 "E Sue"]
priority = []
standard = []
economy = []

#Sorts input_packets into 3 lists depending on first letter.
for packet in input_packets:
    if packet[0] == "S":
        standard.append(packet)
    elif packet[0] == "P":
        priority.append(packet)
    elif packet[0] == "E":
        economy.append(packet)

def wfq():
    """Apply wfq to lists and print accordingly"""
    while True:
        if priority or standard or economy:
            for i in range(3):
                if priority:
                    print(f"Priority: {priority.pop()}")
            for i in range(2):
                if standard:
                    print(f"Standard: {standard.pop()}")
            for i in range(1):
                if economy:
                    print(f"Economy: {economy.pop()}")
        else:
            break

print(priority)
print(standard)
print(economy)

wfq()