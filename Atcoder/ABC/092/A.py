
train = []

for i in range(2):
    train.append(int(input()))

bus = []

for i in range(2):
    bus.append(int(input()))

train_pay = min(train)
bus_pay = min(bus)

print(train_pay + bus_pay)
