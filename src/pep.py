from gettext import gettext as _

MOODS = {
          'afraid': _('Afraid'),
          'amazed': _('Amazed'),
          'angry': _('Angry'),
          'amorous': _('Amorous'),
          'annoyed': _('Annoyed'),
          'anxious': _('Anxious'),
          'aroused': _('Aroused'),
          'ashamed': _('Ashamed'),
          'bored': _('Bored'),
          'brave': _('Brave'),
          'calm': _('Calm'),
          'cautious': _('Cautious'),
          'cold': _('Cold'),
          'confident': _('Confident'),
          'confused': _('Confused'),
          'contemplative': _('Contemplative'),
          'contented': _('Contented'),
          'cranky': _('Cranky'),
          'crazy': _('Crazy'),
          'creative': _('Creative'),
          'curious': _('Curious'),
          'dejected': _('Dejected'),
          'depressed': _('Depressed'),
          'disappointed': _('Disappointed'),
          'disgusted': _('Disgusted'),
          'dismayed': _('Dismayed'),
          'distracted': _('Distracted'),
          'embarrassed': _('Embarrassed'),
          'envious': _('Envious'),
          'excited': _('Excited'),
          'flirtatious': _('Flirtatious'),
          'frustrated': _('Frustrated'),
          'grumpy': _('Grumpy'),
          'guilty': _('Guilty'),
          'happy': _('Happy'),
          'hopeful': _('Hopeful'),
          'hot': _('Hot'),
          'humbled': _('Humbled'),
          'humiliated': _('Humiliated'),
          'hungry': _('Hungry'),
          'hurt': _('Hurt'),
          'impressed': _('Impressed'),
          'in_awe': _('In awe'),
          'in_love': _('In love'),
          'indignant': _('Indignant'),
          'interested': _('Interested'),
          'intoxicated': _('Intoxicated'),
          'invincible': _('Invincible'),
          'jealous': _('Jealous'),
          'lonely': _('Lonely'),
          'lucky': _('Lucky'),
          'mean': _('Mean'),
          'moody': _('Moody'),
          'nervous': _('Nervous'),
          'neutral': _('Neutral'),
          'offended': _('Offended'),
          'outraged': _('Outraged'),
          'playful': _('Playful'),
          'proud': _('Proud'),
          'relaxed': _('Relaxed'),
          'relieved': _('Relieved'),
          'remorseful': _('Remorseful'),
          'restless': _('Restless'),
          'sad': _('Sad'),
          'sarcastic': _('Sarcastic'),
          'serious': _('Serious'),
          'shocked': _('Shocked'),
          'shy': _('Shy'),
          'sick': _('Sick'),
          'sleepy': _('Sleepy'),
          'spontaneous': _('Spontaneous'),
          'stressed': _('Stressed'),
          'strong': _('Strong'),
          'surprised': _('Surprised'),
          'thankful': _('Thankful'),
          'thirsty': _('Thirsty'),
          'tired': _('Tired'),
          'undefined': _('Undefined'),
          'weak': _('Weak'),
          'worried': _('Worried')
}




ACTIVITIES = {
        'doing_chores': {
            'category': _('Doing_chores'),

            'buying_groceries': _('Buying groceries'),
            'cleaning': _('Cleaning'),
            'cooking': _('Cooking'),
            'doing_maintenance': _('Doing maintenance'),
            'doing_the_dishes': _('Doing the dishes'),
            'doing_the_laundry': _('Doing the laundry'),
            'gardening': _('Gardening'),
            'running_an_errand': _('Running an errand'),
            'walking_the_dog': _('Walking the dog'),
            'other': _('Other'),
            }
        'drinking': {
            'category': _('Drinking'),

            'having_a_beer': _('Having a beer'),
            'having_coffee': _('Having coffee'),
            'having_tea': _('Having tea'),
            'other': _('Other'),
            }
        'eating': {
            'category':_('Eating'),

            'having_breakfast': _('Having breakfast'),
            'having_a_snack': _('Having a snack'),
            'having_dinner': _('Having dinner'),
            'having_lunch': _('Having lunch'),
            'other': _('Other'),
            }
        'exercising': {
            'category': _('Exercising'),

            'cycling': _('Cycling'),
            'dancing': _('Dancing'),
            'hiking': _('Hiking'),
            'jogging': _('Jogging'),
            'playing_sports': _('Playing sports'),
            'running': _('Running'),
            'skiing': _('Skiing'),
            'swimming': _('Swimming'),
            'working_out': _('Working out'),
            'other': _('Other'),
            }
        'grooming': {
            'category': _('Grooming'),

            'at_the_spa': _('At the spa'),
            'brushing_teeth': _('Brushing teeth'),
            'getting_a_haircut': _('Getting a haircut'),
            'shaving': _('Shaving'),
            'taking_a_bath': _('Taking a bath'),
            'taking_a_shower': _('Taking a shower'),
            'other': _('Other'),
            }
        'having_appointment': {
            'category': _('Having appointment'),

            'other': _('Other'),
            }
        'inactive': {
            'category': _('Inactive'),

            'day_off': _('Day_off'),
            'hanging_out': _('Hanging out'),
            'hiding': _('Hiding'),
            'on_vacation': _('On vacation'),
            'praying': _('Praying'),
            'scheduled_holiday': _('Scheduled holiday'),
            'sleeping': _('Sleeping'),
            'thinking': _('Thinking'),
            'other': _('Other'),
            }
        'relaxing': {
            'category': _('Relaxing'),

            'fishing': _('Fishing'),
            'gaming': _('Gaming'),
            'going_out': _('Going out'),
            'partying': _('Partying'),
            'reading': _('Reading'),
            'rehearsing': _('Rehearsing'),
            'shopping': _('Shopping'),
            'smoking': _('Smoking'),
            'socializing': _('Socializing'),
            'sunbathing': _('Sunbathing'),
            'watching_a_movie': _('Watching a movie'),
            'watching_tv': _('Watching tv'),
            'other': _('Other'),
            }
        'talking': {
            'category': _('Talking'),

            'in_real_life': _('In real life'),
            'on_the_phone': _('On the phone'),
            'on_video_phone': _('On video phone'),
            'other': _('Other'),
            }
        'traveling': {
            'category': _('Traveling'),

            'commuting': _('Commuting'),
            'driving': _('Driving'),
            'in_a_car': _('In a car'),
            'on_a_bus': _('On a bus'),
            'on_a_plane': _('On a plane'),
            'on_a_train': _('On a train'),
            'on_a_trip': _('On a trip'),
            'walking': _('Walking'),
            'cycling': _('Cycling'),
            'other': _('Other'),
            }
        'undefined': {
            'category': _('Undefined'),

            'other': _('Other'),
            }
        'working': {
            'category': _('Working'),

            'coding': _('Coding'),
            'in_a_meeting': _('In a meeting'),
            'writing': _('Writing'),
            'studying': _('Studying'),
            'other': _('Other'),
            }
        }








