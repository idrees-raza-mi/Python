
file=open("poem.txt","r")
text=file.readlines()

twinkle_found = False
for line in text:
    if "twinkle" in line:
        twinkle_found = True
        break

if twinkle_found:
    print("The poem has letter 'twinkle'")
else:
    print("The poem does not have letter 'twinkle'")
file.close()