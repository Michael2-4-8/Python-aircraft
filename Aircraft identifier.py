print("This is the aircraft identifier.")
print("Please give one of the options, typed exactly as in the question (surrounded by \"quote marks\".")
Type=input("Was the aircraft a \"Helicopter\" or a \"Plane\"?")
if Type== ("Helicopter"):
    Rotors=("How many rotors did the helicopter have, \"1\", or \"2\"?")
elif Type==("plane"):
    Prop=("Did the aircraft have \"propellers\" or \"Jet engines\"?")
    if Prop==("Jet engines"):
        Engines=input("How many engines did the aircraft have, \"1\", \"2\", \"3\", \"4\", \"6\", or \"8\"?")
        if Engines==("1"):
            MilCiv=input("Was the aircraft \"Military\" or \"Commercial\"?")
            if MilCiv==("Commercial"):
                Wings=input("Was the aircraft a \"Biplane\" or a \"Monoplane\"?")
                if wings==("Monoplane"):
                    print("The aircraft could be a \"PiperJet Altaire\", \" Cirrus Vision SF50\", a .")
                elif wings==("Biplane"):
                    print("The aircraft is most likey a \"PZL Mielec M-15 Belphegor\"")
            elif MilCiv==("Military"):
                Canard=input("Did the aircraft have canards(\"True\" or \"False\")?")
                if canard ==("True"):
                    print("The aircraft could be a \"Saab Jas 39 Gripen\", a \"Saab 37 Viggen\", or a \"Chengdu J-10\".") 
                elif canard ==("False"):
                    Delta=input("Did the aircraft have a delta wing(\"True\" or \"False\")?")
                    if Delta==("True"):
                        HorizStabil=input("Did the aircraft have Horizontal stabilisers(\"True\" or \"False\")?")
                        if HorizStabil==("True"):
                            print("The aircraft could be a \"General Dynamics F-16\", an \"Su-9 Fishpot\"  ")
                        elif HorizStabil==("False"):
                            print ("The aircraft could be a \"Dassault Mirage\", a \"HAL Tejas\", a \"Boulton Paul P111\" ")
                    elif Delta==("False"):
                        print("The aircraft could be a \"MiG-23 Flogger\", a \"Heinkel He-162\" a \"F-86 Sabre\", an \"F-80 Shooting Star\" ")
