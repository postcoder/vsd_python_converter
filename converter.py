import comtypes.client as coms
import os
for file in os.listdir("in"):
    if file.endswith(".vsd"):
        print(os.path.join("in", file))
