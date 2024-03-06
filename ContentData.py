import random

count = random.randint(1, 11)
massiveRndm = random.choice(["Наукове дослідження", "Твір"])
for i in range(count):
    result = f"{massiveRndm} - {i}"  # Подобие Твір 1, твір 2
