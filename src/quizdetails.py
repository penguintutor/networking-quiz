import json
import quizquestion


class QuizDetails():
    title = ""
    questions = []
    current_question = 0
        
    def isFirst(self):
        if self.current_question == 0:
            return True
        return False
    
    def isLast(self):
        if self.current_question == len(self.questions)-1:
            return True
        return False
    
    def nextQuestion(self):
        self.current_question += 1
        if (self.current_question > len(self.questions) -1):
            self.current_question = len(self.questions) -1
    
    def prevQuestion(self):
        self.current_question -= 1
        if (self.current_question < 0):
            self.current_question = 0
    
    def setQuestionNum(self, question_num):
        if (question_num >= 0 and question_num < len(self.questions)):
            self.current_question = question_num
    
    def getQuestionNum(self):
        return self.current_question
    
    # if question_num not provided (or -1) then returns current question
    # otherwise returns the requested question
    def getQuestion(self, question_num = -1):
        if question_num == -1:
            question_num = self.current_question
        return self.questions[question_num]
    
    def getTitle(self):
        return self.title
        
    def numQuestions(self):
        return len(self.questions)
        
    # Iterate through all questions, return answers as a list
    def getAnswers(self):
        answers = []
        for question in self.questions:
            answers.append(question.getAnswer())
        return answers
    
    def load(self, filename):
        ##todo - if existing quiz replace
        ##todo - need to catch errors
        
        
        # Reset current quiz - remove all entries and reset counter to 0
        self.questions = []
        self.current_question = 0
        
        with open(filename) as json_file:
            json_data = json.load(json_file)
            # Get title of the quiz from the root key
            root_keys = list(json_data.keys())
            self.title = root_keys[0]

            ## Todo update to use a title field instead of the json tag
            # to be consistant with quizstrings

            question_num = 0
            for this_question in json_data[self.title]:
                
                question_title = list(this_question.keys())[0]
                question_details = [
                    this_question[question_title]["details1"], 
                    this_question[question_title]["details2"], 
                    this_question[question_title]["details3"],
                    this_question[question_title]["details4"],
                    this_question[question_title]["details5"],
                    this_question[question_title]["details6"]
                ]
                question_options = [
                    this_question[question_title]["option1"],
                    this_question[question_title]["option2"],
                    this_question[question_title]["option3"],
                    this_question[question_title]["option4"]
                ]
                question_image = this_question[question_title]["image"]
                question_answer = this_question[question_title]["answer"]
                
                
                self.questions.append(quizquestion.QuizQuestion(question_title, question_details, question_options, question_image, question_answer)) 
        #print ("Quiz loaded "+str(len(self.questions))+" questions")
        return True