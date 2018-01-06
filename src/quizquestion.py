

class QuizQuestion():
    title = ""
    details = []
    options = []
    image = ""
    answer = ""
    
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
        
        