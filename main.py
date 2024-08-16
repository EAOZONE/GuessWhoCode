from adafruit_servokit import ServoKit
import math
import time
import random

Base = 0
Shoulder = 1
Elbow = 2
Wrist = 3
WristXY = 4
Gripper = 5

channel = [0, 0, 0, 0, 0, 0]
channel[Base] = 15
channel[Shoulder] = 0
channel[Elbow] = 14
channel[Wrist] = 13
channel[WristXY] = 1
channel[Gripper] = 2

kit = ServoKit(channels=16)
kit._pca.frequency = 100
for i in range(6):
    kit.servo[channel[i]].set_pulse_width_range(500, 2500)

angles = [0, 0, 0, 0, 0, 0]
phases = [0, 0, 0, 0, 0, 0]
home_position = [100, 40, 180, 100, 0, 0]
home_position[Base] = 100
home_position[Shoulder] = 100
home_position[Elbow] = 160
home_position[Wrist] = 100
home_position[WristXY] = 5
home_position[Gripper] = 0

for i in range(6):
    angles[i] = home_position[i]

phases[Base] = math.pi / 8.0
phases[Shoulder] = math.pi / 8.0
phases[Elbow] = -math.pi / 8.0
phases[Wrist] = math.pi / 4.0
phases[WristXY] = 3.0 / 8.0 * math.pi
phases[Gripper] = 3.0 / 8.0 * math.pi

the_number = random.randint(0, 23)

previous_angles = [100, 100, 160, 100, 0, 0]
new_angle = [0, 0, 0, 0, 0, 0]


def go_to(angles):
    for i in range(1, 30):
        for q in range(6):
            new_angle[q] = float((i * angles[q]) / 30.0) + float(((30 - i) * previous_angles[q]) / 30.0)
            kit.servo[channel[q]].angle = new_angle[q]
        time.sleep(.005)
    for q in range(6):
        previous_angles[q] = angles[q]


def go_home():
    go_to(home_position)


go_home()


def input_angle(index, text):
    angle_input = input(text + "(" + str(angles[index]) + ")")
    if (angle_input != ""):
        angles[index] = int(angle_input)


def enter_base_angle():
    while True:
        if input("go home") == "yes":
            go_home()
        input_angle(Base, "Base angle:")
        input_angle(Shoulder, "Shoulder angle:")
        input_angle(Elbow, "Elbow angle:")
        input_angle(Wrist, "Wrist angle:")
        input_angle(WristXY, "WristXY angle:")
        go_to(angles)


# enter_base_angle()

def answer_no():
    names_to_remove2 = [i for i in choices if i in question_map[computer_question]]
    return names_to_remove2


def answer_yes():
    names_to_remove2 = [i for i in choices if i not in question_map[computer_question]]
    return names_to_remove2


def get_number_index(number):
    if "1" in number:
        return 0
    if "2" in number:
        return 1
    if "3" in number:
        return 2
    if "4" in number:
        return 3
    if "5" in number:
        return 4
    if "6" in number:
        return 5


def get_letter_index(letter):
    if "A" in letter:
        return 0
    if "B" in letter:
        return 1
    if "C" in letter:
        return 2
    if "D" in letter:
        return 3


A_Base_delta = 5;


def A1_start_angles():
    angles[Base] = 124
    angles[Shoulder] = 138
    angles[Elbow] = 160
    angles[Wrist] = 80


def A1_end_angles():
    angles[Base] = 124
    angles[Shoulder] = 110
    angles[Elbow] = 135
    angles[Wrist] = 105


def A2_start_angles():
    A1_start_angles()
    angles[Base] -= A_Base_delta


def A2_end_angles():
    A1_end_angles()
    angles[Base] -= A_Base_delta


def A3_start_angles():
    A1_start_angles()
    angles[Base] -= 2 * A_Base_delta


def A3_end_angles():
    A1_end_angles()
    angles[Base] -= 2 * A_Base_delta


def A4_start_angles():
    A1_start_angles()
    angles[Base] -= 3 * A_Base_delta


def A4_end_angles():
    A1_end_angles()
    angles[Base] -= 3 * A_Base_delta


def A5_start_angles():
    A1_start_angles()
    angles[Base] -= 4 * A_Base_delta


def A5_end_angles():
    A1_end_angles()
    angles[Base] -= 4 * A_Base_delta


def A6_start_angles():
    A1_start_angles()
    angles[Base] -= 5 * A_Base_delta


def A6_end_angles():
    A1_end_angles()
    angles[Base] -= 5 * A_Base_delta


def letter_number_to_remove(squares_to_remove):
    base_start = [125, 128, 134, 137]
    base_end = [95, 95, 95, 95]
    base_increment = [0, 0, 0, 0]
    for i in range(4):
        base_increment[i] = (base_start[i] - base_end[i]) / 5
        print(base_increment[i])

    letter_to_remove = squares_to_remove[0]
    number_to_remove = squares_to_remove[1]
    print(letter_to_remove + number_to_remove)

    if "A1" == squares_to_remove:
        A1_start_angles()
        go_to(angles)
        time.sleep(.5)
        A1_end_angles()
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "B1" == squares_to_remove:
        print("You have B")
        angles[Base] = 129
        angles[Shoulder] = 100
        angles[Elbow] = 120
        angles[Wrist] = 105
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 129
        angles[Shoulder] = 90
        angles[Elbow] = 130
        angles[Wrist] = 135
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "C1" == squares_to_remove:
        print("You have B")
        angles[Base] = 134
        angles[Shoulder] = 60
        angles[Elbow] = 80
        angles[Wrist] = 110
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 134
        angles[Shoulder] = 20
        angles[Elbow] = 40
        angles[Wrist] = 100
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "D1" == squares_to_remove:
        print("You have B")
        angles[Base] = 140
        angles[Shoulder] = 15
        angles[Elbow] = 45
        angles[Wrist] = 115
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 140
        angles[Shoulder] = 0
        angles[Elbow] = 30
        angles[Wrist] = 130
        go_to(angles)
        time.sleep(.5)
        go_home()
    if "A2" == squares_to_remove:
        A2_start_angles()
        go_to(angles)
        time.sleep(.5)
        A2_end_angles()
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "B2" == squares_to_remove:
        print("You have B")
        angles[Base] = 122
        angles[Shoulder] = 100
        angles[Elbow] = 120
        angles[Wrist] = 105
        go_to(angles)
        time.sleep(.5)
        angles[Elbow] = 130
        angles[Base] = 122
        angles[Shoulder] = 90
        angles[Wrist] = 135
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "C2" == squares_to_remove:
        print("You have B")
        angles[Base] = 125
        angles[Shoulder] = 60
        angles[Elbow] = 80
        angles[Wrist] = 110
        go_to(angles)
        time.sleep(.5)
        angles[Elbow] = 40
        angles[Base] = 125
        angles[Shoulder] = 20
        angles[Wrist] = 100
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "D2" == squares_to_remove:
        print("You have B")
        angles[Base] = 129
        angles[Shoulder] = 15
        angles[Elbow] = 45
        angles[Wrist] = 115
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 129
        angles[Shoulder] = 0
        angles[Elbow] = 40
        angles[Wrist] = 140
        go_to(angles)
        time.sleep(.5)
        go_home()
    if "A3" == squares_to_remove:
        A3_start_angles()
        go_to(angles)
        A3_end_angles()
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "B3" == squares_to_remove:
        print("You have B")
        angles[Base] = 115
        angles[Shoulder] = 100
        angles[Elbow] = 120
        angles[Wrist] = 105
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 115
        angles[Shoulder] = 90
        angles[Elbow] = 130
        angles[Wrist] = 135
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "C3" == squares_to_remove:
        print("You have B")
        angles[Base] = 116
        angles[Shoulder] = 60
        angles[Elbow] = 80
        angles[Wrist] = 110
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 116
        angles[Shoulder] = 20
        angles[Elbow] = 40
        angles[Wrist] = 100
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "D3" == squares_to_remove:
        print("You have B")
        angles[Base] = 118
        angles[Shoulder] = 15
        angles[Elbow] = 45
        angles[Wrist] = 115
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 118
        angles[Shoulder] = 0
        angles[Elbow] = 40
        angles[Wrist] = 140
        go_to(angles)
        time.sleep(.5)
        go_home()
    if "A4" == squares_to_remove:
        A4_start_angles()
        go_to(angles)
        time.sleep(.5)
        A4_end_angles()
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "B4" == squares_to_remove:
        print("You have B")
        angles[Base] = 108
        angles[Shoulder] = 100
        angles[Elbow] = 120
        angles[Wrist] = 105
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 108
        angles[Shoulder] = 90
        angles[Elbow] = 130
        angles[Wrist] = 135
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "C4" == squares_to_remove:
        print("You have B")
        angles[Base] = 107
        angles[Shoulder] = 60
        angles[Elbow] = 80
        angles[Wrist] = 110
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 107
        angles[Shoulder] = 20
        angles[Elbow] = 40
        angles[Wrist] = 100
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "D4" == squares_to_remove:
        print("You have B")
        angles[Base] = 107
        angles[Shoulder] = 15
        angles[Elbow] = 45
        angles[Wrist] = 115
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 107
        angles[Shoulder] = 0
        angles[Elbow] = 40
        angles[Wrist] = 140
        go_to(angles)
        time.sleep(.5)
        go_home()
    if "A5" == squares_to_remove:
        A5_start_angles()
        go_to(angles)
        time.sleep(.5)
        A5_end_angles()
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "B5" == squares_to_remove:
        print("You have B")
        angles[Base] = 101
        angles[Shoulder] = 100
        angles[Elbow] = 120
        angles[Wrist] = 105
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 101
        angles[Shoulder] = 90
        angles[Elbow] = 130
        angles[Wrist] = 135
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "C5" == squares_to_remove:
        print("You have B")
        angles[Base] = 98
        angles[Shoulder] = 60
        angles[Elbow] = 80
        angles[Wrist] = 110
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 98
        angles[Shoulder] = 20
        angles[Elbow] = 40
        angles[Wrist] = 100
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "D5" == squares_to_remove:
        print("You have B")
        angles[Base] = 96
        angles[Shoulder] = 15
        angles[Elbow] = 45
        angles[Wrist] = 115
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 96
        angles[Shoulder] = 0
        angles[Elbow] = 40
        angles[Wrist] = 150
        go_to(angles)
        time.sleep(.5)
        go_home()
    if "A6" == squares_to_remove:
        A6_start_angles()
        go_to(angles)
        time.sleep(.5)
        A6_end_angles()
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "B6" == squares_to_remove:
        print("You have B")
        angles[Base] = 92
        angles[Shoulder] = 100
        angles[Elbow] = 120
        angles[Wrist] = 105
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 92
        angles[Shoulder] = 90
        angles[Elbow] = 130
        angles[Wrist] = 135
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "C6" == squares_to_remove:
        print("You have B")
        angles[Base] = 90
        angles[Shoulder] = 60
        angles[Elbow] = 80
        angles[Wrist] = 110
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 90
        angles[Shoulder] = 60
        angles[Elbow] = 40
        angles[Wrist] = 100
        go_to(angles)
        time.sleep(.5)
        go_home()
    elif "D6" == squares_to_remove:
        print("You have B")
        angles[Base] = 86
        angles[Shoulder] = 15
        angles[Elbow] = 45
        angles[Wrist] = 115
        go_to(angles)
        time.sleep(.5)
        angles[Base] = 86
        angles[Shoulder] = 0
        angles[Elbow] = 30
        angles[Wrist] = 130
        go_to(angles)
        time.sleep(.5)
        go_home()


def enter_square_to_remove():
    while True:
        square = input("Square to remove:")
        letter_number_to_remove(square)
        time.sleep(1)


enter_square_to_remove()

names = ["Sarah", "Nick", "Andy", "Chris", "Tyler", "Emily", "Jon", "Alex", "Joshua", "Matt", "Megan", "Kyle",
         "Brandon", "William", "Jake", "Rachael", "Daniel", "James", "Justin", "Connor", "David", "Zachary", "Joseph",
         "Ashley"]
red_hair = ["David", "Zachary", "Joseph", "Ashley"]
black_hair = ["Sarah", "Nick", "Andy", "Chris", "Tyler"]
brown_hair = ["Rachael", "Daniel", "James", "Justin", "Connor"]
Yellow_hair = ["Megan", "Kyle", "Brandon", "William", "Jake"]
hat = ["Rachael", "Daniel", "Brandon", "Ashley", "Chris"]
glasses = ["Sarah", "Nick", "Emily", "Alex", "Joseph"]
facial_hair = ["Jon", "Joshua", "Andy", "Tyler", "David", "William", "Jake", "James", "Justin", "Connor"]
girl = ["Ashley", "Rachael", "Megan", "Emily", "Sarah"]
White_hair = ["Emily", "Jon", "Alex", "Joshua", "Matt"]
bald = ["David", "Alex", "Zachary", "James", "Nick"]
boy = ["Nick", "Andy", "Chris", "Tyler", "David", "Jon", "Alex", "Joshua", "Matt", "Zachary", "Kyle", "Brandon",
       "William", "Jake", "Joseph", "Daniel", "James", "Justin", "Connor"]
questions = ["black_hair", "white_hair", "Yellow_hair", "brown_hair", "glasses", "girl", "boy", "facial_hair",
             "red_hair", "bald", "hat"]
choices = ["Sarah", "Nick", "Andy", "Chris", "Tyler", "Emily", "Jon", "Alex", "Joshua", "Matt", "Megan", "Kyle",
           "Brandon", "William", "Jake", "Rachael", "Daniel", "James", "Justin", "Connor", "David", "Zachary", "Joseph",
           "Ashley"]
names_on_board = [["Sarah", "Nick", "Andy", "Chris", "Tyler", "David"],
                  ["Emily", "Jon", "Alex", "Joshua", "Matt", "Zachary"],
                  ["Megan", "Kyle", "Brandon", "William", "Jake", "Joseph"],
                  ["Rachael", "Daniel", "James", "Justin", "Connor", "Ashley"]]

board_map = dict()
board_map["Sarah"] = "A1"
board_map["Nick"] = "A2"
board_map["Andy"] = "A3"
board_map["Chris"] = "A4"
board_map["Tyler"] = "A5"
board_map["David"] = "A6"
board_map["Emily"] = "B1"
board_map["Jon"] = "B2"
board_map["Alex"] = "B3"
board_map["Joshua"] = "B4"
board_map["Matt"] = "B5"
board_map["Zachary"] = "B6"
board_map["Megan"] = "C1"
board_map["Kyle"] = "C2"
board_map["Brandon"] = "C3"
board_map["William"] = "C4"
board_map["Jake"] = "C5"
board_map["Joseph"] = "C6"
board_map["Rachael"] = "D1"
board_map["Daniel"] = "D2"
board_map["James"] = "D3"
board_map["Justin"] = "D4"
board_map["Connor"] = "D5"
board_map["Ashley"] = "D6"

question_map = dict()
question_map["black_hair"] = black_hair
question_map["white_hair"] = White_hair
question_map["Yellow_hair"] = Yellow_hair
question_map["brown_hair"] = brown_hair
question_map["glasses"] = glasses
question_map["girl"] = girl
question_map["boy"] = boy
question_map["facial_hair"] = facial_hair
question_map["red_hair"] = red_hair
question_map["bald"] = bald
question_map["hat"] = hat
the_name = names[the_number]
names.append("Nick")
won = "I haven't won yet"
game_over = False
I_won = False
Human_won = False
while game_over == False:
    guess = input(
        "Guess you can choose black hair, red hairhair', 'bald', 'h, brown hair, yellow hair, white hair, hat, facial hair, glasses, girl, bald, boy, or a name and make sure you spell it correctly!!!")
    if guess == the_name:
        Human_won = True
        game_over = True
        print("correct")
    elif guess == "black hair":
        if the_name in black_hair:
            print("yes")
        else:
            print("no")
    elif guess == "red hair":
        if the_name in red_hair:
            print("yes")
        else:
            print("no")
    elif guess == "brown hair":
        if the_name in brown_hair:
            print("yes")
        else:
            print("no")
    elif guess == "yellow hair":
        if the_name in Yellow_hair:
            print("yes")
        else:
            print("no")
    elif guess == "white hair":
        if the_name in White_hair:
            print("yes")
        else:
            print("no")
    elif guess == "hat":
        if the_name in hat:
            print("yes")
        else:
            print("No")
    elif guess == "facial hair":
        if the_name in facial_hair:
            print("yes")
        else:
            print("No")
    elif guess == "glasses":
        if the_name in glasses:
            print("yes")
        else:
            print("No")
    elif guess == "girl":
        if the_name in girl:
            print("yes")
        else:
            print("No")
    elif guess == "bald":
        if the_name in bald:
            print("yes")
        else:
            print("No")
    elif guess == "boy":
        if the_name in boy:
            print("yes")
        else:
            print("No")
    else:
        print("incorrect")

    if len(questions) == 0 or len(choices) <= 3:
        person = random.choice(choices)
        print(person)
        answer = input("correct?")
        if answer == "no":
            print("Please remove " + person)
            print("Please remove " + board_map[person])
            choices.remove(person)
            letter_number_to_remove(board_map[person])
        elif answer == "yes":
            I_won = True
            game_over = True
            print("Yay")
    else:
        computer_question = random.choice(questions)

        while len(answer_no()) == 0 or len(answer_yes()) == 0:
            questions.remove(computer_question)
            computer_question = random.choice(questions)
            print("question changed")
            print(questions)
        print(computer_question)
        answer = input("correct?")
        questions.remove(computer_question)
        # print(questions)
        if answer == "no":
            names_to_remove = answer_no()
            # print("Please remove ")
            squares_to_remove = [board_map[i] for i in names_to_remove if i in board_map]
            for i in range(len(squares_to_remove)):
                letter_number_to_remove(squares_to_remove[i])
            # print(squares_to_remove)
            # print (names_to_remove)
            new_choices = [i for i in choices if i not in question_map[computer_question]]
            choices = new_choices
        elif answer == "yes":
            names_to_remove = answer_yes()
            print("Please remove ")
            squares_to_remove = [board_map[i] for i in names_to_remove if i in board_map]
            for i in range(len(squares_to_remove)):
                letter_number_to_remove(squares_to_remove[i])
            # print(squares_to_remove)
            # print (names_to_remove)
            new_choices = [i for i in choices if i in question_map[computer_question]]
            choices = new_choices
# print(choices)
if I_won == True and Human_won == False:
    print("I won")
    angles[Base] = 180
    angles[Shoulder] = 60
    angles[Wrist] = 160
    angles[Elbow] = 150
    for q in range(6):
        kit.servo[channel[q]].angle = angles[q]
    time.sleep(.5)
    angles[Base] = 0
    angles[Shoulder] = 10
    angles[Wrist] = 20
    angles[Elbow] = 150
    for q in range(6):
        kit.servo[channel[q]].angle = angles[q]
elif Human_won == True and I_won == False:
    print("you won")
else:
    print("We tied")