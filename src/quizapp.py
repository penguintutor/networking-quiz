# This uses the dev branch of guizero which needs to be linked to the appropriate
# directory - in future this will use the normal production version of guizero 
from guizero.build.lib.guizero import App, Text, PushButton, info, MenuBar, Picture

import quizdetails
# For testing the gui without the arduino comment out the quizarduino entry and replace with quizarduinodev 
import quizarduino
#import quizarduinodev as quizarduino
import time

class QuizApp():
    
    ## These values are hardcoded here in this version
    
    quiz_filename = "quiz1.json"
    serial_port = '/dev/ttyACM0'
    
    
    def __init__ (self, app):
        self.app = app
        self.quiz = quizdetails.QuizDetails() 
        # Setup serial connection to arduino
        self.arduino = quizarduino.QuizArduino(self.serial_port)
        self.arduino.connect()
        # send blue to indicate startup
        self.arduino.send_recv ([3,3,3,3,3,3])
        

    def home(self):
        pass
    
    # Updates buttons on gui to reflect first and last buttons
    # Also highlights appropriate port for question
    def upd_buttons(self):
        if self.quiz.isFirst():
            self.left_button.text="Return"
            self.left_button.change_command(self.home)
        else:
            self.left_button.text="<< Previous"
            self.left_button.change_command(self.prev_question)
        if self.quiz.isLast():
            self.right_button.text="End Quiz"
            self.right_button.change_command(self.end_quiz)
        else:
            self.right_button.text="Next >>"
            self.right_button.change_command(self.next_question)
        # Light up the current question
        status_leds = [0,0,0,0,0,0]
        status_leds[self.quiz.getQuestionNum()] = 3
        self.arduino.send_recv(status_leds)
    
    # Load quiz from disk
    def load_quiz(self):
        self.quiz.load(self.quiz_filename)
        pass
    
    
    # Start the quiz
    def start_quiz(self):
        #print ("Start Quiz")
        self.load_quiz()
        self.text_title.value = self.quiz.getTitle()
        #self.text_question_title.value = self.quiz.getQuestion().getTitle()
        self.upd_question()
        self.upd_buttons()
        
    # Update display of question
    def upd_question(self):
        #print ("On question "+str(self.quiz.getQuestionNum()))
        this_question = self.quiz.getQuestion()
        self.text_question_title.value = this_question.getTitle()
        
        details = this_question.getDetails()
        self.text_question_details_1.value = details[0]
        self.text_question_details_2.value = details[1]
        self.text_question_details_3.value = details[2]
        self.text_question_details_4.value = details[3]
        self.text_question_details_5.value = details[4]
        self.text_question_details_6.value = details[5]
        
        options = this_question.getOptions()
        self.text_question_option_1.value = options[0]
        self.text_question_option_2.value = options[1]
        self.text_question_option_3.value = options[2]
        self.text_question_option_4.value = options[3]
        
        self.image_question.value = "images/"+this_question.getImage()
    
    # Move to prev question
    def prev_question(self):
        self.quiz.prevQuestion()
        self.upd_question()
        self.upd_buttons()
    
    
    # Move to next question
    def next_question(self):
        self.quiz.nextQuestion()
        self.upd_question()
        self.upd_buttons()
        
    # dummy command (see explanation later regarding guizero bug)
    def button_pressed(self):
        pass
        
    # End quiz
    def end_quiz(self):
        # Set all leds blue to indicate marking and get status
        status_leds = [3,3,3,3,3,3]
        given_answers = self.arduino.send_recv(status_leds)
        score = 0
        # compare given_answers with correct answers
        # correct_answers = self.quiz.getAnswers()
        # for i in range (0,6):
            # response = "incorrect"
            # if (given_answers[i] == correct_answers[i]) :
                # response = "correct"
            # print ("Question " + str(i+1) + " received "+str(given_answers[i]) + " should be "+str(correct_answers[i]) + " answer is "+response)
        details = []
        for i in range (0,6):
            # get the question
            this_question = self.quiz.getQuestion(i)
            # compare whether answer correct 
            if (given_answers[i] == this_question.getAnswer()):
                # correct answer
                score += 1
                details.append(this_question.getTitle()+ " is correct, Answer = "+ this_question.getAnswerLetter())
                status_leds[i] = 1
            else:
                details.append(this_question.getTitle()+ " is incorrect, Correct answer = "+ this_question.getAnswerLetter())
                status_leds[i] = 2
                
        self.text_question_title.value = "Results"
        self.text_question_details_1.value = details[0]
        self.text_question_details_2.value = details[1]
        self.text_question_details_3.value = details[2]
        self.text_question_details_4.value = details[3]
        self.text_question_details_5.value = details[4]
        self.text_question_details_6.value = details[5]
        
        # Set eval based on score
        if (score < 2) :
            eval_string = "Your network is NOT working"
        elif (score > 4) :
            eval_string = "High speed network"
        else:
            eval_string = "Network performance acceptable"
        
        ##Todo update image
        
        self.text_question_option_1.value = ""
        self.text_question_option_2.value = "Score "+str(score)+" out of 6"
        self.text_question_option_3.value = ""
        self.text_question_option_4.value = eval_string
        
        # Update LEDs with status
        self.arduino.send_recv(status_leds)
        
        ##Todo change buttons to say "return to quiz and restart quiz" 
        
        
    
    # Open a new quiz
    def file_open(self):
        ##Todo load different quiz
        pass
    
    # exit the self.app
    def file_exit(self):
        self.app.destroy()
    
    # About
    def help_about(self):
        info("About Quiz", "Created by Stewart Watkiss\nhttp://www.penguintutor.com")
    
    
    def setup_gui(self):    
        menubar = MenuBar(self.app,
                toplevel=["File", "Help"],
                options=[
                        [ ["Open",self.file_open],["Exit", self.file_exit] ] ,
                        [ ["About", self.help_about] ]
                        ])
        
        # column 0 and row 0 are used for dummy images for spacing
        # cols 1 to 5 used for actual display
        # dimensions shown to the right are minimum (using image)
        padding0_0 = Picture(self.app, image="layout/0_0.gif", grid=[0,0])       # 1 pixel
        padding1_0 = Picture(self.app, image="layout/1_0.gif", grid=[1,0])       # 100 pixel
        padding2_0 = Picture(self.app, image="layout/2_0.gif", grid=[2,0])       # 550 pixel
        padding2_0 = Picture(self.app, image="layout/3_0.gif", grid=[3,0])       # 100 pixel
        padding3_0 = Picture(self.app, image="layout/4_0.gif", grid=[4,0])       # 100 pixel
        
        padding0_2 = Picture(self.app, image="layout/0_2.gif", grid=[0,2])       # 100 pixel
        padding0_12 = Picture(self.app, image="layout/0_13.gif", grid=[0,13])    # 100 pixel
        
        self.text_title = Text(self.app, text="Quiz", size=30, grid=[2,1,2,1])
        image_logo = Picture(self.app, image="images/logo.gif", grid=[4,1,2,1])
        
        self.text_question_title = Text(self.app, text="Start Quiz", align="left", size=25, grid=[1,2,2,1])
        
        self.text_question_details_1 = Text(self.app, text="Enter the quiz by cabling up the patch-panel", align="left", size=18, grid=[1,3,3,1])
        self.text_question_details_2 = Text(self.app, text="the question number is shown at the top", align="left", size=18, grid=[1,4,2,1])
        self.text_question_details_3 = Text(self.app, text="the answer corresponds to a port on the", align="left", size=18, grid=[1,5,2,1])
        self.text_question_details_4 = Text(self.app, text="second row", align="left", size=18, grid=[1,6,2,1])
        self.text_question_details_5 = Text(self.app, text="", align="left", size=18, grid=[1,7,2,1])
        self.text_question_details_6 = Text(self.app, text="", align="left", size=18, grid=[1,8,2,1])
        
        self.text_question_option_1 = Text(self.app, text="Press start when ready", align="left", size=18, grid=[1,9,2,1])
        self.text_question_option_2 = Text(self.app, text="", align="left", size=18, grid=[1,10,2,1])
        self.text_question_option_3 = Text(self.app, text="", align="left", size=18, grid=[1,11,2,1])
        self.text_question_option_4 = Text(self.app, text="", align="left", size=18, grid=[1,12,2,1])
        
        self.image_question = Picture(self.app, image="images/network1.gif", grid=[3,3,3,9])
        
        
        # Due to a bug in guizero (issue 103) the original button command is
        # set to a dummy method and change_command used to set the command instead
        self.left_button = PushButton(self.app, text="Return", command=self.button_pressed, grid=[1,13])
        self.left_button.change_command(self.prev_question)
        #self.left_button.hide()
        #self.right_button = PushButton(self.app, text="Start quiz", command=self.start_quiz, grid=[5,13])
        self.right_button = PushButton(self.app, self.button_pressed, text="Start quiz", grid=[5,13])
        self.right_button.change_command(self.start_quiz)
        self.app.display()
