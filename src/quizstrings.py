# Text has been moved to this class, potential to add different languages in future
# Note that this is not complete, some text (eg. buttons) has not been changed

# The corresponding json file, must be consistant by having all entries for all pages
# If an entry is not required (or is updated using a different method - eg. quiz options)
# then it should be added as empty quotes ""

import json

class QuizStrings():
    
    filename = "quizstrings.json"
    # pages contains a dict (indexed by page / screen name), then includes a dictionary which may contain lists (eg. details)
    pages = {}
    
    
    # Returns as a hash dictionary - useful for a full page update
    def getPage(self, page_name):
        return self.pages[page_name]
        
    def getTitle(self):
        return self.title
    
    
    def load(self):
        ##todo - possibly add error checking - Not so important as it should 
        # fail anyway and not neccessarily in a user friendly way (user should not be editing
        # the strings file and if it's missing then it's as bad as a missing .py file
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
            # Get title of the app from the root key
            root_keys = list(json_data.keys())
            self.title = root_keys[0]
            
            # Json file is then broken down into relevant screens (referred to as pages)
            for this_page in json_data[self.title]:
                
                page = list(this_page.keys())[0]
                page_title = this_page[page]["title"]
                page_details = [
                    this_page[page]["details1"], 
                    this_page[page]["details2"], 
                    this_page[page]["details3"],
                    this_page[page]["details4"],
                    this_page[page]["details5"],
                    this_page[page]["details6"]
                ]
                page_options = [
                    this_page[page]["option1"],
                    this_page[page]["option2"],
                    this_page[page]["option3"],
                    this_page[page]["option4"]
                ]
                page_image = this_page[page]["image"]
                page_left_button = this_page[page]["left_button"]
                page_right_button = this_page[page]["right_button"]
                

                self.pages[page]={"title" : page_title, "details": page_details, "options" : page_options, "image" : page_image, "left_button" : page_left_button, "right_button" : page_right_button} 
    