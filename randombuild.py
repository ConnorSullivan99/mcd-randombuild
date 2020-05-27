import random as r

weapons = ["Sword", "Axe", "Glaive", "Daggers", "Soul Knife", "Sickle",
           "Soul Scythe", "Cutlass", "Pickaxe", "Great Hammer", "Mace", "Claymore", "Firebrand", "Highland Axe", "Broadsword", "Heartstealer", "Dancer's Sword", "Fangs of Frost", "Grave Bane", "Venom Glaive", 
           "Hammer of Gravity", "Flall", "Sun's Grace", "Diamond Pickaxe", "Nightmare's Bite", "The Last Laugh", "Eternal Knife", "Diamond Sword", "Hawkbrand"]

armour = ["Hunter's Armour", "Wolf Armour", "Soul Armour", "Evocation Robe", "Mystery Armour", "Scale Mail", "Mercenary Armor", "Spelunker Armor", 
          "Gauntlets", "Thief Armour", "Phantom Armour", "Grim Armour", "Reinforced Mail", "Plate Armour", "Scale Armour", "Soul Robe",
          "Cave Crawler", "Fox Armour", "Highland Armour", "Spider Armour"]

ranged = ["Bow", "Hunting Bow", "Scatter Crossbow", "Longbow", "Trickbow", "Crossbow",
          "Heavy Crossbow", "Shortbow", "Rapid Crossbow", "Power Bow", "Soul Crossbow", "Bonebow", "Guardian Bow", "The Pink Scoundrel", "Twin Bow", "The Slicer", 
          "Imploading Crossbow", "Doom Crossbow", "Voidcaller", "Master's Bow", "Red Snake", "Elite Power Bow", "Butterfly Crossbow", "Lightning Harp Crossbow", 
          "Feral Soul Crossbow", "Bow of Lost Souls", "The Green Menace"]

artifacts = ["Boots of Swiftness", "Death Cap Mushroom", "Tasty Bone", "Torment Quiver", "Harvester", "Fishing Rod", "Soul Eater", "Totem of Regeneration",
             "Lightning Rod", "Light Feather", "Wind Horn", "Flaming Quiver", "Corrupted Beacon", "Totem of Shielding", "Fireworks Arrow",
             "Shock Powder", "Iron Hide Amulet", "Soul Healer", "Love Medallion", "Wonderful Wheat"]

weaponchoice = r.choice(weapons)
armourchoice = r.choice(armour)
rangedchoice = r.choice(ranged)
artifactchoice = r.sample(artifacts, k=3)
a = str(artifactchoice)
b = "[]'"
for char in b:
    a = a.replace(char, "")

print("Your final build is: " + weaponchoice + ", " + armourchoice + ", " +
      rangedchoice + ", " + a)

input("Press ENTER to close program...")
