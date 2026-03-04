allowed = set("123")
userchoice = input("Choose the story [1-3]: ")

# Keep asking until a valid choice is made
while set(userchoice) - allowed or userchoice == "":
    userchoice = input("Invalid choice. Choose the story [1-3]: ")

# Define the prompts for each story
if int(userchoice) == 1:
    uv = [
        "Number:", "Measure of time:", "Mode of Transportation", "Adjective", "Adjective2",
        "Noun", "Color", "Part of the Body", "Verb", "Number2", "Noun2", "Noun3",
        "Part of the Body 2", "Verb","Noun4","Adjective3", "Silly Word", "Noun"
    ]
elif int(userchoice) == 2:
    uv = [
        "Proper Noun (Person’s Name):", "Noun:", "Adjective (Feeling)", "Verb:", "Adjective (Feeling) 2:", "Animal:", "Verb 2:",
        "Color:", "Verb (ending in ing):", "Adverb (ending in ly):", "Number:", "Measure of Time:",
        "Color:", "Animal:", "Number:", "Silly Word:", "Noun 2:"
    ]
elif int(userchoice) == 3:
    uv = [
        "Proper Noun (Person’s Name):", "Adjective:", "Color:", "Animal:", "Place:", "Adjective2:", "Magical Creature (Plural):",
        "Adjective 3:", "Magical Creature (Plural)2:", "Room in House:", "Noun:", "Noun 2:", "Plural 3:",
        "Adjective 4:", "Noun (Plural)4:", "Number:", "Measure of Time:", "Verb (ending in ing):",
        "Adjective 5:", "Noun 5:"
    ]

# Collect user inputs
ui = []
for prompt in uv:
    answer = input(f"Input {prompt} ")
    ui.append(answer)

# Print the chosen story
if int(userchoice) == 1:
    print(f"\nIt was about {ui[0]} {ui[1]} ago when I arrived at the hospital in a {ui[2]}. "
          f"The hospital is a {ui[3]} place, there are a lot of {ui[4]} {ui[5]} here. "
          f"There are nurses here who have {ui[6]} {ui[7]}. "
          f"If someone wants to come into my room I told them that they have to {ui[8]} first. "
          f"I’ve decorated my room with {ui[9]} {ui[10]}. "
          f"Today I talked to a doctor and they were wearing a {ui[11]} on their {ui[12]}. "
          f"I heard that all doctors {ui[13]} {ui[14]} every day for breakfast. "
          f"The most {ui[15]} thing about being in the hospital is the {ui[16]} {ui[17]}!")

elif int(userchoice) == 2:
    print(f"\nThis weekend I am going camping with {ui[0]}. "
          f"I packed my lantern, sleeping bag, and {ui[1]}. "
          f"I am so {ui[2]} to {ui[3]} in a tent. "
          f"I am {ui[4]} we might see a {ui[5]}, I hear they’re kind of dangerous. "
          f"While we’re camping, we are going to hike, fish, and {ui[6]}. "
          f"I have heard that the {ui[7]} lake is great for {ui[8]}. "
          f"Then we will {ui[9]} hike through the forest for {ui[10]} {ui[11]}. "
          f"If I see a {ui[12]} {ui[13]} while hiking, I am going to bring it home as a pet! "
          f"At night we will tell {ui[14]} {ui[15]} stories and roast {ui[16]} around the campfire!!")

elif int(userchoice) == 3:
    print(f"\nDear {ui[0]}, I am writing to you from a {ui[1]} castle in an enchanted forest. "
          f"I found myself here one day after going for a ride on a {ui[2]} {ui[3]} in {ui[4]}. "
          f"There are {ui[5]} {ui[6]} and {ui[7]} {ui[8]} here! "
          f"In the {ui[9]} there is a pool full of {ui[10]}. "
          f"I fall asleep each night on a {ui[11]} of {ui[12]} and dream of {ui[13]} {ui[14]}. "
          f"It feels as though I have lived here for {ui[15]} {ui[16]}. "
          f"I hope one day you can visit, although the only way to get here now is {ui[17]} on a {ui[18]} {ui[19]}!!")
