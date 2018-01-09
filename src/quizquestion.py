

class QuizQuestion():
    # These are all required by constructor so do not require default values
    #title = ""
    #details = []
    #options = []
    #image = ""
    #answer = 
    
    def __init__(self, title, details, options, image, answer):
        self.title = title
        self.details = details
        self.options = options
        self.image = image
        self.answer = answer
    
    def getTitle(self):
        return self.title
        
    def getDetails(self):
        return self.details
        
    def getOptions(self):
        return self.options
        
    def getImage(self):
        return self.image
        
    def getAnswer(self):
        return self.answer
        
    # returns as ascii char 0  = a, 1 = b etc.
    def getAnswerLetter(self):
        return chr(97 + self.answer)
        
        