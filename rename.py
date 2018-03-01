import os
path = r'C:\Users\Khairul Basar\Documents\CWD Projects\Searchline Database\00_WORKING\WL_SLOT1_submission_date_30-03-2018\1-11'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.docx'))
    i = i + 1
