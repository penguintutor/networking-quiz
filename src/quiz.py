#!/usr/bin/python3

# Graphical version of networking quiz

# This uses the dev branch of guizero which needs to be linked to the appropriate
# directory - in future this will use the normal production version of guizero 
from guizero.build.lib.guizero import App


import quizapp




def main():
    app = App(title="Networking Quiz", width=1000, height=755, layout="grid")
    quiz_app = quizapp.QuizApp(app)
    quiz_app.setup_gui()


if __name__ == "__main__":
    main()
