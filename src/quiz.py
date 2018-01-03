#!/usr/bin/python3

# Graphical version of networking quiz

# This uses the dev branch of guizero which needs to be linked to the appropriate
# directory - in future this will use the normal production version of guizero 

from guizero.build.lib.guizero import App, Text, PushButton, info, MenuBar, Picture


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
    # cols 1 to 4 used for actual display
    padding0_0 = Picture(app, image="layout/0_0.gif", grid=[0,0])
    padding1_0 = Picture(app, image="layout/1_0.gif", grid=[1,0])
    padding2_0 = Picture(app, image="layout/2_0.gif", grid=[2,0])
    padding2_0 = Picture(app, image="layout/3_0.gif", grid=[3,0])
    padding3_0 = Picture(app, image="layout/4_0.gif", grid=[4,0])
    
    padding0_2 = Picture(app, image="layout/0_2.gif", grid=[0,2])
    
    text_title = Text(app, text="Networking Quiz", size=30, grid=[1,1,4,1])
    text_question_title = Text(app, text="Question 1", align="left", size=25, grid=[1,2,2,1])
    
    text_question_details_1 = Text(app, text="This is the text description for question 1", align="left", size=18, grid=[1,3,3,1])
    text_question_details_2 = Text(app, text="This is the second line of text description for question 1", align="left", size=18, grid=[1,4,3,1])
    text_question_details_3 = Text(app, text="This is a third line of text", align="left", size=18, grid=[1,5,3,1])
    text_question_details_4 = Text(app, text="There is one more line after this", align="left", size=18, grid=[1,6,3,1])
    text_question_details_5 = Text(app, text="The 5th and last line of text", align="left", size=18, grid=[1,7,3,1])
    
    image_question = Picture(app, image="images/network1.gif", grid=[4,3,2,5])
    
    
    button = PushButton(app, text="Next Question", command=next_question, grid=[5,8])
    app.display()





if __name__ == "__main__":
    app = App(title="Networking Quiz", width=1000, height=755, layout="grid")
    main()
