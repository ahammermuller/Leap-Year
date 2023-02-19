
def invited_names():
    path ="C:/Users/aline/Documents/UDEMY/Mail Merge/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
    with open(path) as invited:
        invited_read = invited.readlines()
        names = []
        for name in invited_read:
            names.append(name.strip())
    return names

def open_letter(name):
    path = "C:/Users/aline/Documents/UDEMY/Mail Merge/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
    with open(path) as start:
        text = start.read()
        new_letter = text.replace("[name]", name)
    return new_letter

def send_mail(name, letter):
    path = f"C:/Users/aline/Documents/UDEMY/Mail Merge/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt"
    with open(path, "w") as file:
        file.write(letter)

def main():
    names = invited_names()
    for name in names:
        letter = open_letter(name)
        send_mail(name, letter)

main()
