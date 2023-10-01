#Shourya Garg
#ENG21CS0379
#Satifaction function 2
#Greedy Rule
#dataset: poland_warszawa_2018_ursynow-wysoki-polnocny.pb

import pandas as pd
import chardet
import csv

def budgeting(E):
    # Initializing the tuple
    A, V, c, l = E
    B = set()
    satisfaction = 0
    

    while l > 0:
        maximumvalue = float('999')
        maxitem = 0
        # alloted Satisfaction function 2
        for a in A:
            if a not in B and c[a] <= l:
                current_value = sum(1 for v in V if len(v.intersection(B.union({a}))) > 0) 
                if current_value > maximumvalue: 
                    maximumvalue = current_value
                    maxitem = a

        if maxitem == 0:
            break

        # Adding the selected item to the bundle
        l -= c[maxitem]
        B.add(maxitem)
        satisfaction += maximumvalue

    return B, satisfaction
    #returning the partial bundle 

#To read the dataset file:
if __name__ == "__main__":
    filename = "poland_warszawa_2018_ursynow-wysoki-polnocny.txt"

    with open(filename, 'rb') as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)['encoding']

    with open(filename, 'r', encoding=detected_encoding, errors='replace') as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            if row[0] == 'budget':
                budget = int(row[1])
            if row[0] == 'PROJECTS':
                break
        projects = {}
        for row in reader:  
            if row[0] == 'VOTES':
                break
            if row[0] == 'project_id':
                continue  
            project_id = row[0]
            cost = int(row[1])
            projects[project_id] = cost  
        voters = []
        for row in reader:  
            if row[0] == 'voter_id':
                continue  
            voter_id = row[0]
            vote = set(row[4].split(','))  
            voters.append((voter_id, vote))


    # R, Budgeting method is a function which takes a budgeting scenario:
    A = set(projects.keys())
    V = [set(vote) for _, vote in voters]
    c = projects
    l = budget

    E = (A, V, c, l)
    result, satisfaction = budgeting(E)
    resultslist = list(result)

    # Creating a DataFrame to store the results in excel sheet

    df = pd.DataFrame({"voters ID": resultslist, "Value": [
        c[project_id] for project_id in resultslist]})
    output_filename = "RESULT.xlsx"
    input = pd.ExcelWriter(output_filename, engine="xlsxwriter")
    df_name = pd.DataFrame({"Dataset Name": [filename]})
    df_name.to_excel(input, sheet_name='Results', startrow=1, index=False)
    df.to_excel(input, startrow=5, index=False, sheet_name="Results")

    Excelsheet = input.sheets["Results"]
    totalCost = sum(c[project_id] for project_id in resultslist)
    ln = len(df) + 2
    Excelsheet.write(ln + 6, 0, "Budget")
    Excelsheet.write(ln + 6, 1, l)
    Excelsheet.write(ln + 7, 0, "Total Cost")
    Excelsheet.write(ln + 7, 1, totalCost)
    Excelsheet.write(ln + 8, 0, "Remaining Cost")
    Excelsheet.write(ln + 8, 1, l - totalCost)
    Excelsheet.write(ln + 8, 0, "Total Projects")
    Excelsheet.write(ln + 8, 1, len(result))
    Excelsheet.write(ln + 9, 0, "Total Satisfaction")
    Excelsheet.write(ln + 9, 1, satisfaction)

    input.close()
    print("The outcome(s) set of projects is stored in",output_filename)
    
