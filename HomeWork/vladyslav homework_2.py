import sys

# Constants used to check conditions
NICKNAME_CONDITION_WEIGHT = 4
SEX_CONDITION_WEIGHT = 3
AGE_CONDITION_WEIGHT = 2


def gender_input_and_validation() -> str:  # sex input and validation
    gender_input: str = input('Pls, enter your Sex:')
    while gender_input != 'Male' or gender_input != 'Female':  # 'Male' or male_input != 'Female'
        if gender_input == 'Male' or gender_input == 'Female':  # 'Male' or male_input == 'Female'
            return gender_input
        else:
            gender_input: str = input('Invalid value entered, pls enter "Male" or "Female"')


def age_input_and_validation() -> int:  # age input and validation: numeric or not
    while True:
        try:
            age_input: int = int(input('Please enter your age: '))  # input and changing age type from string to int
            return age_input
        except ValueError:
            print('Invalid age entered, please enter a numeric value')


# User input
nickname: str = input("Hello, User! \nPlease, enter your Nickname: ")
gender: str = gender_input_and_validation()
age: int = age_input_and_validation()

# Variable for saving points of different conditions
star_wars_and_mandalorian_scores: int = 0
tmnt_scores: int = 0
transformers_score: int = 0
insurgent_score: int = 0
durak_score: int = 0

# check for condition 2
if 'admin' in nickname or 'Admin' in nickname:  # check for condition 2
    print('Welcome, Overlord!')

# Check by gender
if gender == 'Male':
    star_wars_and_mandalorian_scores += SEX_CONDITION_WEIGHT
    tmnt_scores += SEX_CONDITION_WEIGHT
if gender == 'Female':
    transformers_score += SEX_CONDITION_WEIGHT
    insurgent_score += SEX_CONDITION_WEIGHT

# Check by age
if 10 < age < 14 or age > 30:  # 3.1 condition check
    star_wars_and_mandalorian_scores += AGE_CONDITION_WEIGHT
if 22 < age < 32:  # 3.2 condition check
    transformers_score += AGE_CONDITION_WEIGHT
if age < 16:  # 3.3 condition check
    insurgent_score += AGE_CONDITION_WEIGHT
if age < 12:  # 3.5 condition check
    tmnt_scores += AGE_CONDITION_WEIGHT
if nickname == 'Jenya':
    durak_score += NICKNAME_CONDITION_WEIGHT

# Default recommendation
score_of_selected_recommendation: int = transformers_score
selected_recommendation: str = 'I recommend watching "Transformers"'

# Checking recommendations for the scores

if star_wars_and_mandalorian_scores > score_of_selected_recommendation:
    score_of_selected_recommendation = star_wars_and_mandalorian_scores
    selected_recommendation = 'I recommend watching "StarWars" and \'Mandalorian\''
if tmnt_scores > score_of_selected_recommendation:
    score_of_selected_recommendation = tmnt_scores
    selected_recommendation = 'I recommend watching "TMNT"'
if insurgent_score > score_of_selected_recommendation:
    score_of_selected_recommendation = insurgent_score
    selected_recommendation = 'I recommend watching "Insurgent"'
if durak_score > score_of_selected_recommendation:
    score_of_selected_recommendation = durak_score
    selected_recommendation = 'I recommend watching \'Durak\''

# Print recommendation
print(selected_recommendation, '\n')

if nickname == 'Guido':  # 3.6 condition check
    print('Thank you so much!')
