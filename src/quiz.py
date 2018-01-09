#!/usr/bin/python3

# Graphical version of networking quiz

# This uses the dev branch of guizero which needs to be linked to the appropriate
# directory - in future this will use the normal production version of guizero 
from guizero.build.lib.guizero import App
import quizapp

# WARNING - in this version some of the configuration details are hardcoded
# including the name of the quiz file and the serial address for the 
# arduino.
# If these need to be changed then they are in quizapp.py

# Note that in the quiz file then the answer is indexed from 1 (not 0)


def main():
    app = App(title="Networking Quiz", width=1000, height=755, layout="grid")
    quiz_app = quizapp.QuizApp(app)
    quiz_app.setup_gui()


if __name__ == "__main__":
    main()
