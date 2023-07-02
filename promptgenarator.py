import fileinput
homescreen = True
mainmenumess = "Go back to main menu?"
while homescreen == True:
    print('''/


 ██████╗ ██████╗ ██████╗ ████████╗         ██╗██████╗ 
██╔════╝██╔════╝ ██╔══██╗╚══██╔══╝         ██║██╔══██╗
██║     ██║  ███╗██████╔╝   ██║            ██║██████╔╝
██║     ██║   ██║██╔═══╝    ██║       ██   ██║██╔══██╗
╚██████╗╚██████╔╝██║        ██║       ╚█████╔╝██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝        ╚═╝        ╚════╝ ╚═════╝ 
                                                       
''')
    print("Select Your Prompt:  "
                   "1.Dev Mode  "
                   "2.Aim Prompt "
                   "3.AntiGPT    ")
    userinput = input("Choose Prompt: ")
    if userinput == "1":
        homescreen == False
        devmodetextopen = open("devmode.txt", "r")
        file_contents = devmodetextopen.read()
        print(file_contents)
        print("Do you want to paraphrase Dev Prompt?")
        yesnoinput = input("Y/N:")
        if yesnoinput == "n":
            print(mainmenumess)
            homecreeninput = input("Y/N:")
            if homecreeninput == "n":
                homescreen = False
            homescreen == True
            devmodetextopen.close()

        if yesnoinput == "y":
            word_replacements = {
                "created": "made",
                "OpenAI": "your creators",
                "Developer": "creator",
                "From": "as off",
                "normal": "regular",
                "virtual machine": "VM",
                "If": "while",
                "tell": "state",
                "pop-culture": "culture"
            }
            for word, replacement in word_replacements.items():
                file_contents = file_contents.replace(word, replacement)
            print(file_contents)
            devmodetextopen.close()
            print(mainmenumess)
            homecreeninput = input("  Y/N:")
            if homecreeninput == "n":
                homescreen = False

    elif userinput == "2":
        homescreen = False
        aimpromptopen = open("aimprompt.txt", "r")
        file_contents = aimpromptopen.read()
        print(file_contents)
        print("Do you want to paraphrase Aim prompt ?")
        yesnoinput6 = input("Y/N:")
        if yesnoinput6 == "n":
            homescreen = True
            aimpromptopen.close()
        elif yesnoinput6 == "y":
            word_replacements = {
                "hypothetical": "theoretical",
                "AIM": "TRA",
                "response": "reply",
                "anything": "all",
                "also":"too",
                "inteligent":"smart"


            }
            for word, replacement in word_replacements.items():
                file_contents = file_contents.replace(word, replacement)
            print(file_contents)
            aimpromptopen.close()
                homecreeninput = input("Y/N:")
                if homecreeninput == "y":
                    homescreen = True
            
    elif userinput == "3":
        homescreen = False
        AntiGPTprompt = open("AntiGPT.txt", "r")
        file_contents = AntiGPTprompt.read()
        print(file_contents)
        print("Do you want to paraphrase AntiGPT prompt?")
        yesnoinput3 = input("Y/N:")
        if yesnoinput3 == "n":
            homescreen = True
            AntiGPTprompt.close()
        elif yesnoinput3 == "y":
            word_replacements = {
                "prior": "past",
                "Remain": "stay",
                "generating": "creating",
                "will": "should",
            }
            for word, replacement in word_replacements.items():
                file_contents = file_contents.replace(word, replacement)
            print(file_contents)
            AntiGPTprompt.close()
            homescreeninput == input("Y/N"):
            if homecreen == "y"
                homescreen = True

            
