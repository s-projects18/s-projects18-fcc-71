import re

def arithmetic_arranger(problems, flag=True):
  # transform input data --------------
  # list of list with 3 elements in each sublist
  data = list() 
  for problem in problems:
    t = problem.split(' ')
    if(len(t)!=3):
      return "Wrong input format. Should be e.g.: 23 + 44."
    data.append(t)


  # checks ---------------------------
  if len(problems)>5:
    return "Error: Too many problems."
  
  for d in data:
    if d[1]!='+' and d[1]!='-':
      return "Error: Operator must be '+' or '-'."
    if re.search("[^0-9]+", d[0]) or re.search("[^0-9]+", d[2]):
      return "Error: Numbers must only contain digits."   
    if len(d[0])>4 or len(d[2])>4:
      return "Error: Numbers cannot be more than four digits."

  # main ----------------------------
  



  arranged_problems = None
  return arranged_problems

