import json


class QuizDetails():
    title = ""
    questions = []
    options = []
    images = []
    answers = []
    
    
    def getTitle(self):
        return self.title
    
    def load(self, filename):
        ##todo - need to catch errors
        with open("quizzes/"+filename) as json_file:
            json_data = json.load(json_file)
            # Get title of the quiz from the root key
            root_keys = list(json_data.keys())
            self.title = root_keys[0]
            
            question_num = 0
            for this_question in json_data[self.title]:
                
                print (str(this_question))
        return True