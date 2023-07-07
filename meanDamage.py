from math import floor


variant = input("Choose variant: simple, bone, bone+mod, compare, 3:")

if (variant == "3"):
    damageBoneDouble = 12
    damageBoneSimple = 16
    damageBoneTwohand = 20
    mod = 5
    # 0 4 8 12
    # 4 8 12 16
    # 8 12 16 20

    meanBoneDouble = (damageBoneDouble + 1) / 2
    specBoneConstDouble = 0
    for i in range(1, damageBoneDouble + 2):
        specBoneConstDouble = specBoneConstDouble + (damageBoneDouble + 1 - i) * i
    if (specBoneConstDouble != 0):
        specBoneConstDouble = specBoneConstDouble / damageBoneDouble / 20

    meanBoneSimple = (damageBoneSimple + 1) / 2
    specBoneConstSimple = 0
    for i in range(1, damageBoneSimple + 2):
        specBoneConstSimple = specBoneConstSimple + (damageBoneSimple + 1 - i) * i
    specBoneConstSimple = specBoneConstSimple / damageBoneSimple / 20

    meanBoneTwohand = (damageBoneTwohand + 1) / 2
    specBoneConstTwohand = 0
    for i in range(1, damageBoneSimple + 2):
        specBoneConstTwohand = specBoneConstTwohand + (damageBoneTwohand + 1 - i) * i
    specBoneConstTwohand = specBoneConstTwohand / damageBoneTwohand / 20

    for kd in range (6, 19, 3):
        damageDouble = ((meanBoneDouble + (20 - kd  + floor(mod/2))/2)* (20 - kd + floor(mod/2))/20 + specBoneConstDouble) * 2
        damageSimple = (meanBoneSimple + (20 - kd + mod)/2)* (20 - kd + mod)/20 + specBoneConstSimple
        damageTwohand = (meanBoneTwohand + (20 - kd + mod)/2)* (20 - kd + mod)/20 + specBoneConstTwohand

        print("BoneDouble:", damageBoneDouble, "KD:", kd, "MOD:",  mod, "(", mod/2, ")", "Damage:", damageDouble)
        print("BoneSimple:", damageBoneSimple, "KD:", kd, "MOD:", mod, "Damage:", damageSimple)
        print("BoneSimple:", damageBoneTwohand, "KD:", kd, "MOD:", mod, "Damage:", damageTwohand)
        print()
else:
    damageBone = int(input("Input Bone:"))
    meanBone = (damageBone + 1) / 2
    specBoneConst = 0
    for i in range(1, damageBone + 2):
        specBoneConst = specBoneConst + (damageBone + 1 - i) * i
    specBoneConst = specBoneConst / damageBone / 20

    if (variant == "simple"):
        kd = int(input("Input KD:"))
        bonusDamage = int(input("Input MOD:"))
        damage = (meanBone + (20 - kd + bonusDamage)/2)* (20 - kd + bonusDamage)/20 + specBoneConst
        print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "Damage:", damage)
    elif (variant == "bone"):
        for kd in range (12, 28, 3):
            for bonusDamage in range (8, -2, -2):
                damage = (meanBone + (20 - kd + bonusDamage)/2)* (20 - kd + bonusDamage)/20 + specBoneConst
                print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "Damage:", damage)
            print()
    elif (variant == "bone+mod"):
        mod = int(input("Input MOD:"))
        for kd in range (12, 25, 3):
            for bonusDamage in range (6, -2, -2):
                damage = (meanBone + (20 - kd + bonusDamage + mod)/2)* (20 - kd + bonusDamage + mod)/20 + specBoneConst
                print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "+", mod, "Damage:", damage)
            print()
    elif (variant == "compare"):
        mod = int(input("Input MOD:"))

        damageBone2 = int(input("Input Bone2:"))
        meanBone2 = (damageBone2 + 1) / 2
        specBoneConst2 = 0
        for i in range(1, damageBone2 + 2):
            specBoneConst2 = specBoneConst2 + (damageBone2 + 1 - i) * i
        specBoneConst2 = specBoneConst2 / damageBone2 / 20
        mod2 = int(input("Input MOD2:"))

        for kd in range (12, 25, 3):
            for bonusDamage in range (6, -2, -2):
                damage = (meanBone + (20 - kd + bonusDamage + mod)/2)* (20 - kd + bonusDamage + mod)/20 + specBoneConst
                damage2 = (meanBone2 + (20 - kd + bonusDamage + mod2)/2)* (20 - kd + bonusDamage + mod2)/20 + specBoneConst2
                print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "+", mod, "Damage:", damage)
                print("Bone2:", damageBone2, "KD:", kd, "MOD2:", bonusDamage, "+", mod2, "Damage2:", damage2)
            print()





# while (artem.alive):
#     while (artem.result != lose):
#         artem.result = artem.gaming
#     while (artem.result != win):
#         artem.result = artem.gaming
