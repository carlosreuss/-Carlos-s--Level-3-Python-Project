import requests

class Quiz_API:
    '''this calls calls the api and GETS the data called

    all the xxx below are diffrent strings that connect to create a url for the api so the program can gather
    the infomation and procces it to create the quiz questions and ans.

    self.base_URL : base url : string
    self.hard : hard difficulty questions : string
    self.medium : medium difficulty questions : string
    self.easy : easy difficulty questions : string
    self.ten_questions : ten questions : string
    self.five_question : five questions : string
    self.twenty_question : twenty question : string
    
    '''
    def  __init__(self):
        self.base_url = "https://opentdb.com/api.php?"
        self.hard = "&difficulty=hard"
        self.medium = "&difficulty=medium"
        self.easy = "&difficulty=easy"
        self.ten_question = "amount=10"
        self.five_question = "amount=5"
        self.twenty_question = "amount=20"
        self.sport_cat = ""
        self.math_cat = ""
        self.vehicle_cat = ""

    def make_request(self, url):
        '''this functon sends gains a reponce from the api from the url that has been constsurted
        and then returns it to the function that called it
        '''
        response = requests.get(url) #making a call to the api with the url, in this case the url is the pramaters set of filter the infomation
        if  response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            print("whoops somthing went wrong")

    def create_url(self):
        pass

    def num_question_selector(self):
        ''' this function is used to select how many questions the user wants to do'''
        print("")
        while True:
            try:
                amount = int(input("Option 1: 5 questions\n Options 2: 10 questions\n Option 3: 20 questions\n\nPlease enter the corosponding number for the option you want\n"))
                if amount == 1:
                    return self.five_question
                elif amount == 2:
                    return  self.ten_question
                elif amount == 3:
                    return self.twenty_question
                else:
                    continue
            except:
                print("please enter a valid number")

    def difficulty_selector(self):
        '''This function is used to select the level of question for the user'''
        while True:
            try:
                difficulty = int(input("Option 1: easy\n Options 2: meduim\n Option 3: hard\n\nPlease enter the corosponding number for the option you want\n"))
                if difficulty == 1:
                    return self.easy
                elif difficulty == 2:
                    return  self.medium
                elif difficulty == 3:
                    return self.hard
                else:
                    continue
            except:
                print("please enter a valid number")

    def difficulty_selector(self):
        '''This function is used to select the level of question for the user'''
        while True:
            try:
                difficulty = int(input("Option 1: Sports\n Options 2: Maths\n Option 3: Vehicles\n\nPlease enter the corosponding number for the option you want\n"))
                if difficulty == 1:
                    return self.sport_cat
                elif difficulty == 2:
                    return  self.math_cat
                elif difficulty == 3:
                    return self.vehicle_cat
                else:
                    continue
            except:
                print("please enter a valid number")

if __name__ == "__main__":
    pass


test_sss = 5555