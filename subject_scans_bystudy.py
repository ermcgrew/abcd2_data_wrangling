import flywheel
import csv
import pandas as pd
dfamyneg=pd.read_csv('amyneg.csv')

fw = flywheel.Client()

#select project by project ID
try:
    project = fw.get_project('5c508d5fc2a4ad002d7628d8') #NACC-SC
except flywheel.ApiException as e:
    print(f'Error: {e}')

#create list of subjects
try:
    subjects = project.subjects.iter_find()#'created>2022-01-01' 'created>2020-01-01'
except flywheel.ApiException as e:
    print(f'Error: {e}')


# for each subject
#     list of MRI scans
#     if list has 1 item or more, //len is not 0
#         MRI +=1
#     if list has 2+ items,
#         MRIlong+=1


D2MRIcount=0
D2MRIlongcount=0
anegd2mri=0

D2Amycount=0
D2Amylongcount=0
anegd2amy=0

D2Taucount=0
D2Taulongcount=0
anegd2tau=0

ABCMRIcount=0
ABCMRIlongcount=0
anegabcmri=0

ABCAmycount=0
ABCAmylongcount=0
anegabcamy=0

ABCTaucount=0
ABCTaulongcount=0
anegabctau=0

# listtowrite=[]
# headernames=['D2MRI','D2Amyloid','D2Tau','ABCMRI','ABCAmyloid','ABCTau']
# with open(f'imaging_by_numbers3.csv', 'w', newline='') as csvfile:
#     csvwriter=csv.DictWriter(csvfile, fieldnames=headernames)
#     csvwriter.writeheader()
for count, subject in enumerate(subjects, 1):
        print(f'Subject {count}: {subject.label}')
        labels=[session.label for session in subject.sessions() if "Duplicate" not in session.tags and 'Misc.' not in session.tags and 'ABC' in session.label and '7T' not in session.label]
        
        # labeldict={}
        # labeldict['D2MRI']=[label for label in labels if '3T' in label and 'D2' in label]
        # labeldict['ABCMRI']=[label for label in labels if '3T' in label and 'D2' not in label]
        # labeldict['D2Amyloid']=[label for label in labels if 'FBB' in label and 'D2' in label]
        # labeldict['ABCAmyloid']=[label for label in labels if 'FBB' in label and 'D2' not in label] 
        # labeldict['D2Tau']=[label for label in labels if 'AV1451' in label and 'D2' in label]
        # labeldict['ABCTau']=[label for label in labels if 'AV1451' in label and 'D2' not in label] 
        # listtowrite.append(labeldict)

        D2MRIscanlist=[label for label in labels if '3T' in label and 'D2' in label]
        if len(D2MRIscanlist) != 0:
            D2MRIcount+=1
            match=dfamyneg.loc[dfamyneg['INDD']==subject.label]
            if len(match)>=1:
                anegd2mri+=1
        if len(D2MRIscanlist) >=2:
            D2MRIlongcount+=1

        ABCMRIscanlist=[label for label in labels if '3T' in label and 'D2' not in label]
        if len(ABCMRIscanlist) != 0:
            ABCMRIcount+=1
            match=dfamyneg.loc[dfamyneg['INDD']==subject.label]
            if len(match)>=1:
                anegabcmri+=1
        if len(ABCMRIscanlist) >=2:
            ABCMRIlongcount+=1
        
        D2Amyscanlist=[label for label in labels if 'FBB' in label and 'D2' in label]
        if len(D2Amyscanlist) != 0:
            D2Amycount+=1
            match=dfamyneg.loc[dfamyneg['INDD']==subject.label]
            if len(match)>=1:
                anegd2amy+=1
        if len(D2Amyscanlist) >=2:
            D2Amylongcount+=1

        ABCAmyscanlist=[label for label in labels if 'FBB' in label and 'D2' not in label]
        if len(ABCAmyscanlist) != 0:
            ABCAmycount+=1
            match=dfamyneg.loc[dfamyneg['INDD']==subject.label]
            if len(match)>=1:
                anegabcamy+=1
        if len(ABCAmyscanlist) >=2:
            ABCAmylongcount+=1    

        D2Tauscanlist=[label for label in labels if 'AV1451' in label and 'D2' in label]
        if len(D2Tauscanlist) != 0:
            D2Taucount+=1
            # print(f"Tau Scan list:")
            # print(D2Tauscanlist)
            match=dfamyneg.loc[dfamyneg['INDD']==subject.label]
            if len(match)>=1:
                # print(f"Amyneg subject match: {match['INDD']}")
                anegd2tau+=1
        if len(D2Tauscanlist) >=2:
            D2Taulongcount+=1

        ABCTauscanlist=[label for label in labels if 'AV1451' in label and 'D2' not in label]
        if len(ABCTauscanlist) != 0:
            ABCTaucount+=1
            match=dfamyneg.loc[dfamyneg['INDD']==subject.label]
            if len(match)>=1:
                anegabctau+=1
        if len(ABCTauscanlist) >=2:
            ABCTaulongcount+=1 

    # csvwriter.writerows(listtowrite)

print(f'ABCD2 MRI: {D2MRIcount}')
print(D2MRIlongcount)
print(f'ABCD2 Amy: {D2Amycount}')
print(D2Amylongcount)
print(f'ABCD2 Tau: {D2Taucount}')
print(D2Taulongcount)

print()
print(f'amy neg ABCD2 MRI: {anegd2mri}')
print(f'amy neg ABCD2 Amy: {anegd2amy}')
print(f'amy neg ABCD2 Tau: {anegd2tau}')
print()

print(f'ABC MRI: {ABCMRIcount}')
print(ABCMRIlongcount)
print(f'ABC Amy: {ABCAmycount}')
print(ABCAmylongcount)
print(f'ABC Tau: {ABCTaucount}')
print(ABCTaulongcount)

print()
print(f'amy neg ABC MRI: {anegabcmri}')
print(f'amy neg ABC Amy: {anegabcamy}')
print(f'amy neg ABC Tau: {anegabctau}')
print()
