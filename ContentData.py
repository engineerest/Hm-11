import random

selectionValue = random.randint(1, 11)
massiveRndm = random.choice(["Наукове дослідження", "Твір"])
for i in range(selectionValue):
    result = f"{massiveRndm} - {i}"  # Подобие Твір 1, твір 2
