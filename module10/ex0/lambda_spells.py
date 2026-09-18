artifact_sorter = (
    lambda artifacts: sorted(artifacts,
                             key=lambda artifact: artifact["power"],
                             reverse=True))

power_filter = (
    lambda mages, min_power: filter(lambda mage:
                                    mage["power"] >= min_power,
                                    mages))

spell_transformer = (
    lambda spells: map(lambda spell: "*" + spell + "*", spells))

#todo
mage_stats = (lambda mages: max(mages))
