import requests
import random

class QuizAPI:
    '''
    this calls calls the api and GETS the data called

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
        '''
        This functon sends gains a reponce from the api from the url that has been constsurted
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
                    print("please enter a valid integer within the range of 1-3")
            except ValueError:
                print("Please enter a valid integer")
            except Exception as e:
                print("An unexpected error occurred:", e)

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
                    print("please enter a valid integer within the range of 1-3")
            except ValueError:
                print("Please enter a valid integer")
            except Exception as e:
                print("An unexpected error occurred:", e)

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
                    print("please enter a valid integer within the range of 1-3")
            except ValueError:
                print("Please enter a valid integer")
            except Exception as e:
                print("An unexpected error occurred:", e)

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
    '''
    this class is used to orgnze the questions by the 6 diffrent aspects they inclued
    self.type = type
    self.type = catgory
    self.difficulty = difficulty
    self.quest = quest
    self.correct_ans =correct_ans
    self.incorrect_ans = incorrect_ans
    '''

    def __init__(self, type, difficulty, category, quest, correct_ans, incorrect_ans):
        self.type = type
        self.difficulty = difficulty
        self.category = category
        self.quest = quest
        self.correct_ans = correct_ans
        self.incorrect_ans = incorrect_ans
        

    def shuffle_questions(self):
        """
        the job of this function is to shuffle the correct answer with the provided other worng answers as when the data is recived
        the correct answer and the wrongs answer are not mixed. its job is to also keep track of the index possion of the correct answer in the list of the shuffled answers
        """
        answers = [self.correct_ans] + self.incorrect_ans
        random.shuffle(answers)
        correct_index = answers.index(self.correct_ans)
        return answers, correct_index

    def display_questions(self):
        '''
        this functions job is to not only display the questions, 
        but also send the data to the shuffle_questions function to recuive the shuffled answers and the correct index(the loctation of the correct answer in the list) of the correct anser
        '''
        shuffled_answers, correct_index = self.shuffle_questions() # getting the suffled answers as well as the index possition of the correct answer in that list of shuffled answers.
        print("---------")
        print(f"The question: {self.quest}")#printing the question
        print("")
        for i in range(len(shuffled_answers)): #looping thru the list of possible answer (shiuffled_answers) to nicely print then out in a new line everytime
            print(f"{i + 1}: {shuffled_answers[i]}")
            i = i + 1
        while True:#while true loop with the try except to validate the users input to makes sure it is a integer that has a corrsponding option
            try:
                user_ans = int(input("\nEnter the number corrosponding to the answer e.g. 2\b-->:"))

                user_ans = user_ans - 1

                if 0 <= user_ans and user_ans <= 3 or 0 <= user_ans and user_ans <= 2:#checks if the ans within the range
                    if user_ans == correct_index:
                        print("congrats you got it correct")
                        return 1
                    else:
                        print("unluckly, incorrect")
                        return 0
                else:
                    print("")
                    print("please enter a number that is in the valid range of options: 1-4 or 1-2")
            except ValueError: #occurs when the user inputs a interger that has no corrosponding answer
                print("Please enter a valid integer")
            except Exception as e: #occurs when the program experaces a fault or bug
                print("An unexpected error occurred:", e)


def quiz(questions):
    '''
    The quiz function purpose is to loop through the dat and send question by question to the questions class's functions.
    Then the infomation of if the user got the question correct or not is returned, 0  being incoret and 1 being correct.
    this then gets (summed and divided)*100 to get the percentage of corret ans. Then it prints out a summary of the users performance in a scentace.
    '''
    ans_correct = 0 #reseting the amout of correct answers
    for question_data in questions: #looping through the data recived from the api class
        question = Questions(*question_data) # the *question_data is creating a list called question with the use of all of the question data and an instance of the Question class
        ans_cor = question.display_questions() #calling the display question function in the Question class
        ans_correct = ans_correct + ans_cor #adding a 1 if corrent and a 0 if incorret
    decs_per_correct = ans_correct / len(questions) # creasting a percentage of answer that were corret answers in decimal form
    percentage_correct = decs_per_correct * 100 #making the percanetage to a proper percentage
    print("")
    '''
    the if stamtent is making sure that eventhing went well, and also creating the measge that the user will recive containing their results.
    '''
    if percentage_correct >= 80:
        print(f"Well Done, you got {ans_correct} out of {len(questions)} which is outstanding\n that is {percentage_correct}% correct")
    elif 70 <= percentage_correct and percentage_correct <= 79:
        print(f"Nice Work, you got {ans_correct} out of {len(questions)} which is great\n that is {percentage_correct}% correct")
    elif 60 <= percentage_correct and percentage_correct <= 69:
        print(f"Good Stuff, you got {ans_correct} out of {len(questions)} which is good\n that is {percentage_correct}% correct")
    elif 50 <= percentage_correct and percentage_correct <= 59:
        print(f"Nice, you got {ans_correct} out of {len(questions)} which is good\n that is {percentage_correct}% correct")
    elif 10 <= percentage_correct and percentage_correct <= 49:
        print(f"good atempet, you got {ans_correct} out of {len(questions)} which is allright\n that is {percentage_correct}% correct")
    elif 0 <= percentage_correct and percentage_correct <= 9:
        print(f"Unluckly, you got {ans_correct} out of {len(questions)} which is not the best,\n that is {percentage_correct}% correct, better luck next time")
    else:
        print("opps somthing went wrong when processing you data to get your final score.")
    print("-----")
    

def menu():
    '''
    The menu function is the fist funtion called in the program.
    A menus job is to allow the user to navagate arround a program.
    In this case the menu system allows the user to choose from two diffrent option which consist of starting a quiz and ending/closeing the program.
    The menu is also the home of the program as it is were the infomation gathered for the QuizAPI gets sent to the Question api via the quiz function.
    This function also uses a while true, try except loop to ensure that the user will get propted to enter a val answer if they do not
    '''
    api_quiz = QuizAPI()  # Create an instance of QuizAPI

    while True:
        try:
            print("Welcome to The Trivia")
            print("")
            print("Option 1: Start quiz\nOption 2: Quit app")

            user_choice = int(input("\nEnter the number corosponding to the option you want to proceed with: "))

            if user_choice == 1:
                questions = api_quiz.get_question()  # Call the method with the instance
                quiz(questions) # passing the data recived of the querstions from the API to the quiz function
            elif user_choice == 2:
                print("---bye---")
                break
            else:
                print("Please enter a valid option (1 or 2)")
        except ValueError:
            print("Please enter a valid integer")
        except Exception as e: #this tells the user what the error is if the program fails its self, for example when the data recived frm the API has change its own format reusting to it haveing more or less varbles
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    menu()
