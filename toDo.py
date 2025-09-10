import json
selected = 0

with open("tasks.json", "r") as f:
    data = json.load(f)

while True:
    for i in range (len(data)):
        print(("- " if selected == i else "  ") + data[i]["task"] + (" √" if data[i]["done"] else " X"))
    print()
    print("Type 'i' for info")
    inp = input("")
    if inp == "]" and selected != len(data) - 1:
        selected += 1
    elif inp == "[" and selected != 0:
        selected -= 1
    elif inp == "m":
        data[selected]["done"] = not data[selected]["done"]
    elif inp == "s":
        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4)
        print("File updated!")
    elif inp == "i":
        print("'[' to go up")
        print("']' to go down")
        print("'m' to mark as done")
        print("'d' to delete")
        print("'a' to add")
        input("'t' to toggle showing complete tasks")
        input("'s' to save changes")