import json
import quizquestion


class QuizDetails():
    title = ""
    questions = []
    current_question = 0
    
    
    def next_question(self):
        self.current_question += 1
        if (self.current_question > len(self.questions) -1):
            self.current_question = self.questions -1
    
    def prev_question(self):
        self.current_question -= 1
        if (self.current_question < 0):
            self.current_question = 0
    
    def setQuestionNum(self, question_num):
        if (question_num >= 0 and question_num < len(self.questions)):
            self.current_question = question_num
    
    def getQuestion(self):
        return self.questions[current_question]
    
    def getTitle(self):
        return self.title
        
    def numQuestions(self):
        return len(self.questions)
    
    def load(self, filename):
        ##todo - if existing quiz replace
        ##todo - need to catch errors
        with open("quizzes/"+filename) as json_file:
            json_data = json.load(json_file)
            # Get title of the quiz from the root key
            root_keys = list(json_data.keys())
            self.title = root_keys[0]
            
            question_num = 0
            for this_question in json_data[self.title]:
                
                question_title = list(this_question.keys())[0]
                question_details = [
                    this_question[question_title]["details1"], this_question[question_title]["details2"], this_question[question_title]["details3"],
                    this_question[question_title]["details4"],
                    this_question[question_title]["details5"]
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
                
                #print (str(this_question))
        return True