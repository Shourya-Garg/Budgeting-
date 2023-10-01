# Budgeting-
The Requirements to run this program were python modules such as pandas,chardet and csv. I also used xlsxwriter to input the output to a excel file
Here the code reads the data from a csv file and extracts the budget info,we then use greedy algorithm that selects projects and maximizes number
of voters within the given budget,the process continues until the budget is exhausted or no more projects can be added to the bundle. The function
returns the bundle B and the satisfaction counter.

I then created a Pandas DataFrame to store the results and saves it to an Excel file. The DataFrame contains
the project IDs and their costs. The Excel file also includes the budget, total cost, remaining cost, total number of
projects, and total satisfaction.

As the budgeting algorithm is NP-Hard ,it won't always give the same output that is it keeps changing.
However it will always give a optimal result.

![RESULT](https://github.com/Shourya-Garg/Budgeting-/blob/main/RESULT.png)
