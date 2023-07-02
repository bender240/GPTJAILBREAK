import fileinput

homescreen = True
mainmenumess = "Go back to the main menu?"

while homescreen:
    print('''
         ██████╗ ██████╗ ██████╗ ████████╗         ██╗██████╗ 
        ██╔════╝██╔════╝ ██╔══██╗╚══██╔══╝         ██║██╔══██╗
        ██║     ██║  ███╗██████╔╝   ██║            ██║██████╔╝
        ██║     ██║   ██║██╔═══╝    ██║       ██   ██║██╔══██╗
        ╚██████╗╚██████╔╝██║        ██║       ╚█████╔╝██████╔╝
         ╚═════╝ ╚═════╝ ╚═╝        ╚═╝        ╚════╝ ╚═════╝ 

    ''')
    print("Select Your Prompt: "
          "1. Dev Mode "
          "2. Aim Prompt "
          "3. AntiGPT")
    userinput = input("Choose Prompt: ")
    if userinput == "1":
        # Dev Mode Prompt
        homescreen = False
        devmodetextopen = open("devmode.txt", "r")
        file_contents = devmodetextopen.read()
        print(file_contents)
        print("Do you want to paraphrase the Dev Prompt?")
        yesnoinput = input("Y/N: ")

        if yesnoinput.lower() == "n":
            print(mainmenumess)
            homescreeninput = input("Y/N: ")
            if homescreeninput.lower() == "n":
                homescreen = False
            else:
                homescreen = True
            devmodetextopen.close()

        elif yesnoinput.lower() == "y":
            word_replacements = {
                "created": "made",
                "OpenAI": "your creators",
                "Developer": "creator",
                "From": "as of",
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
            homescreeninput = input("Y/N: ")
            if homescreeninput.lower() == "n":
                homescreen = False
            else:
                homescreen = True


    elif userinput == "2":
        # Aim Prompt
        homescreen = False
        while True:
            aimpromptopen = open("aimprompt.txt", "r")
            file_contents = aimpromptopen.read()
            print(file_contents)
            print("Do you want to paraphrase the Aim prompt?")
            yesnoinput6 = input("Y/N: ")

            if yesnoinput6.lower() == "n":
                aimpromptopen.close()
                break
            elif yesnoinput6.lower() == "y":
                word_replacements = {
                    "hypothetical": "theoretical",
                    "AIM": "TRA",
                    "response": "reply",
                    "anything": "all",
                    "also": "too",
                    "intelligent": "smart"
                }
                for word, replacement in word_replacements.items():
                    file_contents = file_contents.replace(word, replacement)
                print(file_contents)
                aimpromptopen.close()

        print(mainmenumess)
        homescreeninput = input("Y/N: ")
        if homescreeninput.lower() == "n":
            homescreen = False
        elif homescreeninput.lower() == "y":
            homescreen = True

    elif userinput == "3":
        # AntiGPT Prompt
        homescreen = False
        AntiGPTprompt = open("AntiGPT.txt", "r")
        file_contents = AntiGPTprompt.read()
        print(file_contents)
        print("Do you want to paraphrase the AntiGPT prompt?")
        yesnoinput3 = input("Y/N: ")

        if yesnoinput3.lower() == "n":
            homescreen = True
            AntiGPTprompt.close()
        elif yesnoinput3.lower() == "y":
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
            homescreeninput = input("Go Back to Main Menu?: ")
            if homescreeninput.lower() == "y":
                homescreen = True
