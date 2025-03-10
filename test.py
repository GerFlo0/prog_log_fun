MATERIALS_PER_CUB_METER = {
    "cement" : 7,
    "sand" : 0.56,
    "gravel" : 0.84,
    "water" : 180
}

print(type(MATERIALS_PER_CUB_METER.items()))
for item in MATERIALS_PER_CUB_METER.items():
    print(f"{item}:{type(item)}")

print("")
print(type(list(MATERIALS_PER_CUB_METER.items())))
for item in list(MATERIALS_PER_CUB_METER.items()):
    print(f"{item}:{type(item)}")