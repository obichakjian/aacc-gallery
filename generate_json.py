import os, json

photos_folder = "photos"
members = []

for file in os.listdir(photos_folder):
    if not file.lower().endswith((".png",".jpg",".jpeg",".webp")):
        continue

    try:
        voice, name = file.split(" - ", 1)
        name = name.rsplit(".",1)[0]

        members.append({
            "name": name.strip(),
            "voicepart": voice.strip(),
            "image": f"photos/{file}"
        })
    except:
        print("Skipping:", file)

with open("members.json","w") as f:
    json.dump(members, f, indent=2)

print("Done!")