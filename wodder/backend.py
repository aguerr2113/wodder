
import random 


beginner_met = ['100 m run','50 m run']
short_metcon =['400 m run','200 m run','2 min jumping jacks','400 m row', '200 m row']
speed_long_met = ['400 m run','200 m run','400 m row', '200 m row']
mid_long_met = ['800 m run','1200 m run', '1600 m run']
long_metcon =['5km run','10km run']

gymnastics = [ 'sit-up','leg-rasies']
upper_push_gym = ['push-up','dip','burpee',]
upper_pull = ['pull-up','row']
lower_push = ['squat']
pl_gym = ['jump squat','plyo push-up','plyo row']
str_gym_push =['weighted push-up','weighted dip']
str_gym_pull =['weighted pull-up','weighted row']

upper_push_weightlift = ['push-press','bench-press','thruster']
upper_pull_weightlift = ['Row']
lower_push_weightlift = ['backsquat','front-squat','lunge']
lower_pull_weighlift = ['deadlift','clean']

def beginner_weight_num():
    return random.randint(1,6)
def intermediate_weight_num():
    return random.randint(4,12)
def advanced_weight_num():
    return random.randint(8,21)



def metcontrip_beg(short_metcon,upper_push_gym,lower_pull_weighlift):
    num1 = beginner_weight_num()
    num2 = beginner_weight_num()
    gym = num1 ,random.choice(upper_push_gym)
    lift = num2 , random.choice(lower_pull_weighlift)
    new_g = ':'.join(str(item).strip("()', ")for item in gym)
    new_l = ':'.join(str(item).strip("()', ")for item in lift)

    workout = [(random.choice(short_metcon)),new_g,new_l]
    print(workout)


def metcontrip_int(short_metcon,upper_push_gym,lower_pull_weighlift):
    num1 = intermediate_weight_num()
    num2 = intermediate_weight_num()
    gym = num1 ,random.choice(upper_push_gym)
    lift = num2 , random.choice(lower_pull_weighlift)
    new_g = ':'.join(str(item).strip("()', ")for item in gym)
    new_l = ':'.join(str(item).strip("()', ")for item in lift)

    workout = [(random.choice(short_metcon)),new_g,new_l]
    print(workout)

def metcontrip_adv(short_metcon,upper_push_gym,lower_pull_weighlift):
    num1 = advanced_weight_num()
    num2 = advanced_weight_num()
    gym = num1 ,random.choice(upper_push_gym)
    lift = num2 , random.choice(lower_pull_weighlift)
    new_g = ':'.join(str(item).strip("()', ")for item in gym)
    new_l = ':'.join(str(item).strip("()', ")for item in lift)

    workout = [(random.choice(short_metcon)),new_g,new_l]
    print(workout)
# metcontrip(short_metcon,upper_push_gym,lower_pull_weighlift)

def wods():
    level = int(input(f'What level of fitness are you? \nBeginner(0)\nIntermediate(1)\nAdvanced(2)\n'))
    time = int(input(f'How much time(min) do you have to exercise 1-60\n'))
    print(f'Your workout of the day is:\nDo as many rounds/reps as possible in {time} minutes')
    if level == 0:
        metcontrip_beg(short_metcon,upper_push_gym,lower_pull_weighlift)
    elif level == 1:
        metcontrip_int(short_metcon,upper_push_gym,lower_pull_weighlift)
    elif level == 2:
        metcontrip_adv(short_metcon,upper_push_gym,lower_pull_weighlift)
    
wods()