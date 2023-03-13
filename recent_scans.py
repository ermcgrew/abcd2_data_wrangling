import flywheel
import csv
import pandas as pd


fw = flywheel.Client()

#select project by project ID
try:
    project = fw.get_project('5c508d5fc2a4ad002d7628d8') #NACC-SC
except flywheel.ApiException as e:
    print(f'Error: {e}')

#list of sessions
try:
    sessions = project.sessions.iter_find('created>2023-01-01')
except flywheel.ApiException as e:
    print(f'Error: {e}')

d2count=0
mricount=0
taupetcount=0
amypetcount=0
subjects=0
subjectlist=[]

for session in sessions:
    if 'D2' in session.label:
        d2count +=1
        print(session.label)
        # print(session.subject.label)
        if session.subject.label not in subjectlist:
            subjectlist.append(session.subject.label)
            subjects+=1
        
        if "3T" in session.label:
            mricount+=1
        elif 'FBBPET' in session.label:
            amypetcount +=1
        elif 'AV1451' in session.label:
            taupetcount +=1 
        


print(f"Total ABCD2 sessions: {d2count}")
print(f"3T sessions: {mricount}")
print(f"Amyloid PET sessions: {amypetcount}")
print(f"Tau PET sessions: {taupetcount}")
print(f'Number of subejcts: {subjects}')
