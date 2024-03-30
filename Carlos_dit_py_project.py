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



    def num_question_selector(self):
        ''' this function is used to select how many questions the user wants to do and then returns the url required to create the overall url that gets sent to the api'''
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

    def cat_selector(self):
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

    def create_url(self):
        print("")
        num_url = self.num_question_selector()
        dif_url = self.difficulty_selector()
        cat_url = self.cat_selector()
        url = self.base_url + num_url + dif_url + cat_url
        return url

    def get_question(self):
        '''gets the questions from the API'''
        url = self.create_url()
        data = self.make_request(url)
        if data: #as the data recvied is in a dictonary, if data: cheacks in their is thing in it and retuns true, an emty dictonary will return false
            questions_data = data.get('results', [])
            question_formated = []
            for question_data in questions_data: #here we are looping through the data recived from the api and matching the infomation up their in program varable
                category = question_data['category']
                difficulty = question_data['difficulty']
                correct_ans = question_data['correct_answer']
                incorrect_ans = question_data['incorrect_answers']
                question_formated.append(Questions(category, difficulty, correct_ans, incorrect_ans))#here those varables get put in to the order of how the class Question is set up
            return question_formated
        else:
            return []

class Questions:

    def __init__(self, category, difficulty, correct_ans, incorrect_ans):
        self.type = category
        self.difficulty = difficulty
        self.correct_ans = correct_ans
        self.incorrect_ans = incorrect_ans
        

def menu():
    '''this functon is the menu system and it creates an instance and allows the user to navigate arround the app'''
    api_quiz = Quiz_API() # Create an instance of Quiz_API

    while True:
        try:
            print("Welcome to The Trivia")
            print("")
            print("Option 1: Start quiz\nOption 2: Quit app")

            user_choice = int(input(": "))

            if user_choice == 1:
                questions = api_quiz.get_question() # Call the method with the instance
            elif user_choice == 2:
                print("---bye---")
                break
        except ValueError:
            print("Please enter a valid answer.")

if __name__ == "__main__":
    menu()