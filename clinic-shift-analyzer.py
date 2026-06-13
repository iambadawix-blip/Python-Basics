#bismillahir rahmanir raheem
'''Build a program that analyzes hospital patient records stored in nested dictionaries and lists.'''

patient_col = {
        'patient_1': {
    'name': 'mohanad',
    'age': '23',
    'department': 'urology',
    'symptoms': ['fever', 'headache'],
    'vital signs': {
       'temp': 39,
       'bp': 90,
       'hr': 75
    },
    'medications': ['panadol', 'chloroquine']
    },
        'patient_2': {
    'name': 'usman',
    'age': '24',
    'department': 'urology',
    'symptoms': ['fever', 'chest pain'],
    'vital signs': {
       'temp': 39,
       'bp': 130,
       'hr': 68
    },
    'medications': ['chloroquine', 'diazepam']
    },
        'patient_3': {
    'name': 'ibrahim',
    'age': '25',
    'department': 'cardiology',
    'symptoms': ['chest pain', 'headache'],
    'vital signs': {
       'temp': 36,
       'bp': 80,
       'hr': 80
    },
    'medications': ['panadol', 'diazepam']
    }
}

'''1. Generate a patient report

For every patient, display all their information in a readable format.'''

for k, v in patient_col.items():
   for patient_det, values in v.items(): #det here means details

      print (f'{patient_det.title()}: {values}')


'''2. Detect abnormal findings

Examine the vital signs and identify patients who have abnormal values.

Do not ask me for the exact conditions unless you're completely stuck.'''

for k, v in patient_col.items():
    temp = v['vital signs']['temp']
    if temp > 38:
        print (f'{v['name']} has a fever')
    bp = v ['vital signs']['bp']
    if bp > 129:
        print(f'{v['name']} has tachycardia')
    hr = v ['vital signs']['hr']
    if hr > 100:
        print(f'{v['name']} has hypertension')

'''Count departments

Determine how many patients belong to each department.'''

dept = []
for k, v in patient_col.items():
   dept.append(v['department'])
print(dept)





meds = []
'''4. Analyze medications

Count how frequently each medication appears across all patients.'''
for v in patient_col.values():
    meds.extend(v['medications'])
for med in set(meds):
    print(med, meds.count(med))




'''5. Find the oldest patient

Search through all records and identify the oldest person.'''
ages = []
for v in patient_col.values():
    ages.append(v['age'])
print (f'The oldest patient here is {max(ages)}')


'''6. Symptom analysis

Identify patients who have many symptoms.

You decide what qualifies as "many."'''
#people with more than one symptom have many symptoms

for v in patient_col.values():
    
    if len(v['symptoms']) > 1:
        print ('This patient has many symptoms')





'''7. Create a shift summary

At the end, print overall statistics about the hospital shift.

Examples of things that could be summarized:

Total patients
Number of abnormal cases
Number of departments
Number of unique medications'''
#this checks the total number of patients

print(len(patient_col))
#abnormal cases undefined
#this should check the number of departments
#first we add them to a set
dept = []
for v in patient_col.values():
    dept.append(v['department'])
dept = set(dept)
print (len(dept))

#this should check for the number of unique medications
meds = []
for v in patient_col.values():
    meds.extend(v['medications'])
# ¨¨
meds = set(meds)
print (f'the number of unique meds is {len(meds)}')

