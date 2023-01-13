import pandas as pd
import flywheel

dfamyneg=pd.read_csv('amyneg.csv')

fw = flywheel.Client()
#select project by project ID
try:
    project = fw.get_project('5c508d5fc2a4ad002d7628d8') #NACC-SC
except flywheel.ApiException as e:
    print(f'Error: {e}')
#create list of sessions
try:
    sessions = project.sessions.iter_find()  #'created>2022-12-01'
except flywheel.ApiException as e:
    print(f'Error: {e}')

anegd2mri=0
anegd2tau=0
anegd2amy=0

D2MRIcount=0
D2Taucount=0
D2Amycount=0
ABCMRIcount=0
ABCTaucount=0
ABCAmycount=0

for count, session in enumerate(sessions, 1):
    print(f'Loop {count}: {session.label}')

    if 'Duplicate' in session.tags or 'Misc.' in session.tags: 
        print(f'{session.label} has tag {session.tags}, skip')
        continue
    else:
        if 'ABC' not in session.label: 
            print("Not ABC/ABCD2 session")
            continue
        else:
            if 'D2' in session.label:
                sessname=session.label
                sesslist=sessname.split('x')
                match=dfamyneg.loc[dfamyneg['INDD']==sesslist[0]]
                if len(match)>=1:
                    print('yes negative')
                    if '3T' in session.label: #or '7T' in session.label:
                        D2MRIcount+=1
                        anegd2mri+=1
                    elif 'AV1451' in session.label:
                        D2Taucount+=1
                        anegd2tau+=1
                    elif 'FBBPET' in session.label:
                        D2Amycount+=1
                        anegd2amy+=1
                else:
                    if '3T' in session.label:# or '7T' in session.label:
                        D2MRIcount+=1
                    elif 'AV1451' in session.label:
                        D2Taucount+=1
                    elif 'FBBPET' in session.label:
                        D2Amycount+=1
            else:
                if '3T' in session.label:# or '7T' in session.label: 
                    ABCMRIcount+=1                
                elif 'AV1451' in session.label:
                    ABCTaucount+=1
                elif 'FBBPET' in session.label:
                    ABCAmycount+=1

d2total=D2MRIcount+D2Taucount+D2Amycount
abctotal=ABCMRIcount+ABCTaucount+ABCAmycount

print(f'{count} sessions in project {project.label} checked')  
print()
print(f'All ABCD2: {d2total}')
print(f'ABCD2 MRI: {D2MRIcount}')
print(f'ABCD2 Tau: {D2Taucount}')
print(f'ABCD2 Amy: {D2Amycount}')
print()
print(f'amy neg ABCD2 MRI: {anegd2mri}')
print(f'amy neg ABCD2 Tau: {anegd2tau}')
print(f'amy neg ABCD2 Amy: {anegd2amy}')
print()
print(f'All ABC total: {abctotal}')
print(f'ABC MRI: {ABCMRIcount}')
print(f'ABC Tau: {ABCTaucount}')
print(f'ABC Amy: {ABCAmycount}')