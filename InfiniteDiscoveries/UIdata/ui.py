import PySimpleGUI as sg
import textwrap
import os
import sys
import subprocess

def startUI():
    Programfilepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
    cachePath = Programfilepath + "/cache.py"
    import cache

    filepath = cache.filepath

    #sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

    allActions = []

    actionText = ""

    inputButtonSize = (12,10)

    currentObjectText = sg.Text("Generator is not currently running.", background_color=("#0c0f1a"))

    currentActionText = sg.Text("", background_color=("#0c0f1a"), key="currentActionText")

    currentActionLayout = [[currentObjectText],[currentActionText]]

    currentActionFrame = sg.Frame("", layout=currentActionLayout, background_color=("#0c0f1a"), key="currentActionFrame", expand_y=True, expand_x=True)

    startAmountDescText = "Recommended values are however many stars, 7 planets and 3 moons. Higher amounts will generate planets/moons further out and might start causing issues. DO NOT go over 25 planets, due to the amount of letters in the alphabet."

    starAmountDescription = sg.Text(textwrap.fill(startAmountDescText, 49), expand_y=False, expand_x=True, pad=(5,5))

    starAmountInp = sg.Input(default_text=5, key="starAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
    starAmountLayout = [[starAmountInp]]
    starAmountFrame = sg.Frame("Star amount", layout=starAmountLayout, expand_y=True, expand_x=True, pad=(5,5))
    planetAmountInp = sg.Input(default_text=7, key="planetAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
    planetAmountLayout = [[planetAmountInp]]
    planetAmountFrame = sg.Frame("Max planets", layout=planetAmountLayout, expand_y=True, expand_x=True, pad=(5,5))
    moonAmountInp = sg.Input(default_text=3, key="moonAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
    moonAmountLayout = [[moonAmountInp]]
    moonAmountFrame = sg.Frame("Max moons", layout=moonAmountLayout, expand_y=True, expand_x=True, pad=(5,5))

    numInpLayout = [[starAmountFrame, planetAmountFrame, moonAmountFrame],[starAmountDescription]]

    amountInpFrame = sg.Frame("", layout=numInpLayout, background_color=("#43474d"), expand_y=False, expand_x=True, pad=(10,0))

    startButton = sg.Button(button_text="Start Generator", size=(25,5), key="startGenerator", visible=True, expand_y=False, expand_x=True, pad=(10,0))

    estTimeText = sg.Text("Estimated Generator Time: 26.25 minutes.", key="timeRemainingText", background_color=("#43474d"), expand_y=False, expand_x=True)

    directoryText = sg.Input(filepath, size=(30,10), key="directoryText", enable_events=True, expand_y=False, expand_x=True)

    directoryBrowser = sg.FolderBrowse("Set KSP directory...", key="directoryButton", enable_events=True, initial_folder=filepath)

    InfDLayout = [[sg.Text("Infinite Discoveries", background_color=("#43474d"))], [amountInpFrame], [directoryText,directoryBrowser], [startButton], [estTimeText]]

    InfDOutputLayout = [[currentActionFrame]]

    settingsButton = sg.Button("Settings", image_size=(50,50), key="openSettings")

    settingsLayout = [[settingsButton]]

    settingsFrame = sg.Frame("", layout=settingsLayout)

    InputFrame = sg.Frame("", layout=InfDLayout, expand_y=True, expand_x=True, element_justification="c", background_color="#50535c")

    OutputFrame = sg.Frame("", layout=InfDOutputLayout, expand_y=True, expand_x=True, element_justification="c", background_color="#50535c")

    fullLayout = [[InputFrame,OutputFrame],[settingsFrame]]

    InfDWindow = sg.Window(title="Infinite Discoveries 0.9.9", layout=fullLayout, size=(650,400), margins=(5,0), resizable=True, finalize=True, icon=Programfilepath + "/funnyicon.ico", element_justification='c', background_color="#1f2836")

    InfDWindow.TKroot.minsize(650,400)

    # Things??

    while True:
        event, values = InfDWindow.read()

        if event == "starAmountInput":
            try: 
                int(values["starAmountInput"])
            except:
                print("Not a number!")
                InfDWindow["starAmountInput"].update(values["starAmountInput"][:-1])

        if event == "planetAmountInput":
            try: 
                int(values["planetAmountInput"])
                if int(values["planetAmountInput"]) > 25:
                    InfDWindow["planetAmountInput"].update(25)
            except:
                print("Not a number!")
                InfDWindow["planetAmountInput"].update(values["planetAmountInput"][:-1])

        if event == "moonAmountInput":
            try: 
                int(values["moonAmountInput"])
            except:
                print("Not a number!")
                InfDWindow["moonAmountInput"].update(values["moonAmountInput"][:-1])
        try:
            starAmount = int(values["starAmountInput"])
        except:
            starAmount = 0
        try:
            planetAmount = int(values["planetAmountInput"])
        except:
            planetAmount = 0
        try:
            moonAmount = int(values["moonAmountInput"])
        except:
            moonAmount = 0

        if event == "directoryText":
            filepath = values["directoryText"]
            print("Setting directory to: " + filepath)
            cacheFile = open(cachePath, "w")
            cacheFile.write('filepath = "' + filepath + '"')
            cacheFile.close()

        if event == "openSettings":
            settingsWindow = sg.Window(title="Settings", layout=[[]], size=(300,150))
            settingsWindow.read()

        estTime = ((planetAmount * moonAmount) * starAmount)*15

        if estTime >= 60:
            if estTime >= 3600:
                if estTime >= 86400:
                    if estTime >= 604800:
                        if estTime >= 2.628e+6:
                            if estTime >= 3.154e+7:
                                InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/3.154e+7),2)) + " years.")
                            else:
                                InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/2.628e+6),2)) + " months.")
                        else:
                            InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/604800),2)) + " weeks.")
                    else:
                        InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/86400),2)) + " days.")
                else:
                    InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/3600),2)) + " hours.")
            else:
                InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/60),2)) + " minutes.")
        else:
            InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime),2)) + " seconds.")

        if event == "startGenerator":
            try: 
                int(values["starAmountInput"])
                try: 
                    int(values["planetAmountInput"])
                    try: 
                        int(values["moonAmountInput"])
                    except:
                        print("Not a number!")
                except:
                    print("Not a number!")
            except:
                print("Not a number!")

            print("The generator should take AT MOST " + str(round((estTime/60),2)) + " minutes.")

            InfDWindow["startGenerator"].hide_row()

            allActions.append("aaaaaaahahahahha")

            generatorPath = Programfilepath.replace("/UIdata", "")

            systemLoop(starAmount,planetAmount,moonAmount,filepath)

            #sys.path.insert(0, generatorPath + "/GenerateSystem/")

            #subprocess.run(["python", generatorPath + "/GenerateSystem/GenerateSystem.py"], starAmount, planetAmount, moonAmount)

            #thread2 = threading.Thread(target=GenerateSystem.systemLoop(starAmount, planetAmount, moonAmount, filepath))

            #thread2.start()

            #GenerateSystem.systemLoop(starAmount, planetAmount, moonAmount, filepath)

            for i in range(0,len(allActions)):
                actionText = actionText + allActions[i] + "\n"
                InfDWindow["currentActionText"].update(actionText)
            #print(currentActionLayout)

        if event == sg.WINDOW_CLOSED:
            break

startUI()