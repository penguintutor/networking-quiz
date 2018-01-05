#!/usr/bin/python3

# Graphical version of networking quiz

# This uses the dev branch of guizero which needs to be linked to the appropriate
# directory - in future this will use the normal production version of guizero 

from guizero.build.lib.guizero import App, Text, PushButton, info, MenuBar, Picture
import quizdetails


quiz = quizdetails.QuizDetails() 





# Load quiz from disk
def load_quiz():
    quiz.load("quiz1.json")
    pass


# Start the quiz
def start_quiz():
    load_quiz()
    print ("Title "+quiz.getTitle())


# Move to prev question
def prev_question():
    pass


# Move to next question
def next_question():
    pass

# Open a new quiz
def file_open():
    pass

# exit the app
def file_exit():
    app.destroy()

# About
def help_about():
    info("About Quiz", "Created by Stewart Watkiss\nhttp://www.penguintutor.com")


def main():
    menubar = MenuBar(app,
            toplevel=["File", "Help"],
            options=[
                    [ ["Open",file_open],["Exit", file_exit] ] ,
                    [ ["About", help_about] ]
                    ])
    
    # column 0 and row 0 are used for dummy images for spacing
    # cols 1 to 5 used for actual display
    # dimensions shown to the right are minimum (using image)
    padding0_0 = Picture(app, image="layout/0_0.gif", grid=[0,0])       # 1 pixel
    padding1_0 = Picture(app, image="layout/1_0.gif", grid=[1,0])       # 100 pixel
    padding2_0 = Picture(app, image="layout/2_0.gif", grid=[2,0])       # 550 pixel
    padding2_0 = Picture(app, image="layout/3_0.gif", grid=[3,0])       # 100 pixel
    padding3_0 = Picture(app, image="layout/4_0.gif", grid=[4,0])       # 100 pixel
    
    padding0_2 = Picture(app, image="layout/0_2.gif", grid=[0,2])       # 100 pixel
    padding0_12 = Picture(app, image="layout/0_12.gif", grid=[0,12])    # 100 pixel
    
    text_title = Text(app, text="Networking Quiz", size=30, grid=[2,1,2,1])
    image_logo = Picture(app, image="images/logo.gif", grid=[4,1,2,1])
    
    text_question_title = Text(app, text="Start Quiz", align="left", size=25, grid=[1,2,2,1])
    
    text_question_details_1 = Text(app, text="Enter the quiz by cabling up the patch-panel", align="left", size=18, grid=[1,3,3,1])
    text_question_details_2 = Text(app, text="the question number is shown at the top", align="left", size=18, grid=[1,4,2,1])
    text_question_details_3 = Text(app, text="the answer corresponds to a port on the", align="left", size=18, grid=[1,5,2,1])
    text_question_details_4 = Text(app, text="second row", align="left", size=18, grid=[1,6,2,1])
    text_question_details_5 = Text(app, text="", align="left", size=18, grid=[1,7,2,1])
    
    text_question_option_1 = Text(app, text="Press start when ready", align="left", size=18, grid=[1,8,2,1])
    text_question_option_2 = Text(app, text="", align="left", size=18, grid=[1,9,2,1])
    text_question_option_3 = Text(app, text="", align="left", size=18, grid=[1,10,2,1])
    text_question_option_4 = Text(app, text="", align="left", size=18, grid=[1,11,2,1])
    
    image_question = Picture(app, image="images/network1.gif", grid=[3,3,3,9])
    
    
    left_button = PushButton(app, text="<< Previous", command=prev_question, grid=[1,13])
    left_button.hide()
    right_button = PushButton(app, text="Start quiz", command=start_quiz, grid=[5,13])
    app.display()





if __name__ == "__main__":
    app = App(title="Networking Quiz", width=1000, height=755, layout="grid")
    main()
