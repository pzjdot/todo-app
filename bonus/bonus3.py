import os.path

base_path = '/Users/pzj/PycharmProjects/pythonProject1'
subfiles_path = os.path.join(base_path, 'mega/journal')


#
date = input("Enter today's date: ")
full_path = os.path.join(subfiles_path, f"{date}.txt")

mood = input("How do you rate your mood today from 1 to 10")
thoughts = input("Let your thoughts flow: \n")

with open(full_path, 'w') as files:
    files.writelines(f"Mood Rating: {mood} \n\n")
    files.writelines("journal Entry: \n")
    files.write(thoughts)
