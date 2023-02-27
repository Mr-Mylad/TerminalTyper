from os import chdir
from os.path import isdir
from os.path import curdir
fullText = []
Text = "How do you know the text value unless you saw the code?"

def save():
    Name = Text.split(" ")[1]
    print(f"Same path or different? (\".\" if same ({curdir}), the path if different)")
    Path = input("File name: ")
    if Path != ".":
        if isdir(Path):
            chdir(Path)
        else:
            print("That\'s not a real path! Try again.\n")
            save()
        with open(Name, "w") as File:
            for i in range(0, len(fullText)):
                File.write(fullText[i])
        print("Thank you for writing! Have a nice day!")
        exit()

def main():
    global fullText
    global Text
    Text = input(">> ")
    if Text.split(" ")[0] == "fid":
        save()
    else:
        Text = Text + "\n"
    fullText.append(Text)
    main()
print("Write your text(Write \"fid filename.txt\" when finished")
main()