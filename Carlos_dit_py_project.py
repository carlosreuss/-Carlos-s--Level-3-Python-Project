import requests
import random

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
        '''This function is used to select the level of question for the user by returning the url fragment that corosponds to the users choice'''
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
        '''This function is used to select the level of question for the user by returning the url fragment that corrosponds to the users choice'''
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
        '''this function has three varbles that store the three diffrent url fragments that corrosponed to what the user has selected to filter the questions.
        it then combinds then all together with the base url'''
        print("")
        num_url = self.num_question_selector()
        dif_url = self.difficulty_selector()
        cat_url = self.cat_selector()
        url = self.base_url + num_url + dif_url + cat_url
        return url

    def get_question(self):
        '''gets the questions from the API.
    it does this by getting the url that was constructed in the create url function,
    then it sends that url to the get requests function which makes a request to the API,
    the API then returns the info and store it in the data var. then it gets formatted into the format of the question'''
        url = self.create_url()
        data = self.make_request(url)
        if data: #as the data received is in a dictionary, if data: checks if there is anything in it and returns true, an empty dictionary will return false
            questions = []

            for question_data in data['results']:
                type = question_data["type"]
                difficulty = question_data["difficulty"]
                category = question_data["category"]
                quest = question_data["question"]
                correct_ans = question_data["correct_answer"]
                incorrect_ans = question_data["incorrect_answers"]
                questions.append([type, difficulty, category, quest, correct_ans, incorrect_ans])  # Append as a list
            return(questions)
        else:
            return []

class Questions:
    '''this class is used to orgnze the questions by the 4 diffrent aspects they inclued
    self.type = catgory
    self.difficulty = difficulty
    self.correct_ans =correct_ans
    self.incorrect_ans = incorrect_ans'''

    def __init__(self, type, difficulty, category, quest, correct_ans, incorrect_ans):
        self.type = type
        self.difficulty = difficulty
        self.category = category
        self.quest = quest
        self.correct_ans = correct_ans
        self.incorrect_ans = incorrect_ans
        

    def shuffle_questions(self):
        answers = [self.correct_ans] + self.incorrect_ans
        random.shuffle(answers)
        correct_index = answers.index(self.correct_ans)
        return answers, correct_index

    def display_questions(self):
        shuffled_answers, correct_index = self.shuffle_questions()
        print("---------")
        print(f"The question: {self.quest}")
        print("")
        for i in range(len(shuffled_answers)):
            print(f"{i + 1}: {shuffled_answers[i]}")
            i = i + 1
        while True:
            try:
                user_ans = int(input("\nEnter the number corrosponding to the answer e.g. 2\b-->:"))

                user_ans = user_ans - 1

                if 0 <= user_ans and user_ans <= 3:
                    if user_ans == correct_index:
                        print("congrats you got it correct")
                        break
                    else:
                        print("unluckly, incorrect")
                        break
                elif 0>= user_ans or user_ans >=3:
                    print("")
                    print("please enter a number that is in the valid range of options: 1-4 or 1-2")
            except ValueError:
                print("Please enter a valid integer")
            except Exception as e:
                print("An unexpected error occurred:", e)


def quiz(questions):
    for question_data in questions: #looping through the data recived from the api class
        question = Questions(*question_data)
        question.display_questions()


def menu():
    api_quiz = Quiz_API()  # Create an instance of Quiz_API

    while True:
        try:
            print("Welcome to The Trivia")
            print("")
            print("Option 1: Start quiz\nOption 2: Quit app")

            user_choice = int(input(": "))

            if user_choice == 1:
                questions = api_quiz.get_question()  # Call the method with the instance
                quiz(questions)
            elif user_choice == 2:
                print("---bye---")
                break
            else:
                print("Please enter a valid option (1 or 2)")
        except ValueError:
            print("Please enter a valid integer")
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    menu()
