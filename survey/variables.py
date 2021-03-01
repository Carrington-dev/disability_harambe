group_A = '15-19'
group_B = '20-24'
group_C = '25-29'
group_D = '30-34'
group_E = '35-39'
group_F = '40-44'
group_G = '45-49'
group_H = '50-54'
group_I = '55-59'
group_J = '60-64'
group_K = '65-69'
group_L = '70-74'
group_M ='75-79'
group_N =  '85-89'
group_O = '95-99'


AGE_OF_INTERVIEWEE = (
    (group_A , '15-19'),
    (group_B , '20-24'),
    (group_C , '25-29'),
    (group_D , '30-34'),
    (group_E , '35-39'),
    (group_F , '40-44'),
    (group_G , '45-49'),
    (group_H , '50-54'),
    (group_I , '55-59'),
    (group_J , '60-64'),
    (group_K , '65-69'),
    (group_L , '70-74'),
    (group_M , '75-79'),
    (group_N , '85-89'),
    (group_O , '95-99'),
)

Government = 'Government'
Inter_governmental_organization = 'Inter governmental organization'
Human_rights_organization = 'Human rights organization'
Organization_of_persons_WITH_disability = 'Organization of persons with disability'
Family_member_of_person_WITH_disabilities = 'Family member of person with disabilities'
Public_healthcare_organization = 'Public healthcare organization'
Private_healthcare_organization = 'Private healthcare organization'
Other_specify = 'Other (Specify)'

Stakeholder_classification = (
    (Government , 'Government'),
    (Inter_governmental_organization, 'Inter governmental organization'),
    (Human_rights_organization , 'Human rights organization'),
    (Organization_of_persons_WITH_disability , 'Organization of persons with disability'),
    (Family_member_of_person_WITH_disabilities , 'Family member of person with disabilities'),
    (Public_healthcare_organization , 'Public healthcare organization'),
    (Private_healthcare_organization , 'Private healthcare organization'),
    (Other_specify, 'Other (Specify)'),
)


MALE = 'male'
FEMALE = 'female'

GENDER = (
    (MALE, 'male'),
    (FEMALE, 'female'),
)

strongly_disagree = 'strongly_disagree'
disagree = 'Disagree'
neutral = 'Neutral'
agree = 'agree'
strongly_agree = 'strongly agree'

question_A = (
    (strongly_disagree , 'Strongly disagree '),
    (disagree, 'Disagree'),
    (neutral , 'Neutral'),
    (agree, 'Agree'),
    (strongly_agree, 'Strongly agree'),
)

no = 'no'
yes = 'yes'
not_sure = 'Neutral'

question_B = (
    (no , ' No '),
    (yes, 'Yes'),
    (not_sure , 'Neutral '),
)


sign_language = "Sign Language"
easy_read = "Easy Read or Plain Language"
audio_formats = "audio formats"
multiple_languages = "multiple languages"
websites = "Websites are accessible for screen reader users "
captioning = "Captioning services"
other = "Other (please specify)"
no_info = "No information has been provided in any format"

not_at_all = "Not at all",
little_support_was_given = "Little support was given"
adequate_support_was_given = "Adequate support was given"
some_times = "Sometimes"
all_the_time = "All the time"
true = True
false = False


question_C = [
    ( sign_language,  "Sign Language" ),
    ( easy_read , "Easy Read or Plain Language" ),
    ( audio_formats,  "audio formats" ),
    ( multiple_languages,  "multiple languages" ),
    ( websites,  "Websites are accessible for screen reader users " ),
    ( captioning,  "Captioning services" ),
    ( other,  "Other (please specify)" ),
    ( no_info,  "No information has been provided in any format" ),
]

    



question_D = (
   ( "Not at all" , "Not at all"),
   ( "Little support was given" , "Little support was given"),
   ( "Adequate support was given" , "Adequate support was given"),
)


question_E = (
   ( "Not at all" , "Not at all"),
   ( "Sometimes" , "Sometimes"),
   ( "All the time" , "All the time"),
)


question_F = (
    ( 'True' , True ),
    ( 'False' , False ),
)
