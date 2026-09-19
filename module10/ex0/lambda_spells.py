artifact_sorter = (
    lambda artifacts: sorted(artifacts,
                             key=lambda artifact:
                             artifact["power"],
                             reverse=True))

power_filter = (
    lambda mages, min_power: filter(lambda mage:
                                    mage["power"] >= min_power,
                                    mages))

spell_transformer = (
    lambda spells: map(lambda spell: "*" + spell + "*", spells))

mage_stats = (
    lambda mages: {
        "max_power": max(map(lambda mage: mage["power"], mages)),
        "min_power": min(map(lambda mage: mage["power"], mages)),
        "avg_power": round(
            sum(map(
                lambda mage: mage["power"], mages)) / len(mages),
            2
        )
    }
)

artifacts = [{'name': 'Fire Staff', 'power': 100, 'type': 'armor'},
             {'name': 'Wind Cloak', 'power': 114, 'type': 'accessory'},
             {'name': 'Lightning Rod', 'power': 107, 'type': 'accessory'},
             {'name': 'Wind Cloak', 'power': 76, 'type': 'relic'}]

mages = [{'name': 'River', 'power': 93, 'element': 'earth'},
         {'name': 'Nova', 'power': 92, 'element': 'fire'},
         {'name': 'Rowan', 'power': 86, 'element': 'fire'},
         {'name': 'Zara', 'power': 83, 'element': 'water'},
         {'name': 'Ember', 'power': 78, 'element': 'fire'}]

spells = ['fireball', 'tsunami', 'blizzard', 'earthquake']

print("Testing artifact sorter...")
sorted_arts = artifact_sorter(artifacts)
print(*(f'{art["name"]} ({art["power"]} power)' for art in sorted_arts),
      sep=" comes before ")

print("\nTesting power_filter...")
print(list(power_filter(artifacts, 100)))

print("\nTesting spell_transformer...")
updated_spells = spell_transformer(spells)
print(*updated_spells)

print("\nTesting mage_stats...")
print(mage_stats(mages))
