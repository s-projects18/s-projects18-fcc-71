import re

def arithmetic_arranger(problems, flagDisplay=True):
  # transform input data --------------
  # list of list with 3 elements in each sublist
  data = list() 
  for problem in problems:
    t = problem.split(' ')
    if(len(t)!=3):
      return "Wrong input format. Should be e.g.: 23 + 44."
    if flagDisplay:
      f=1
      if t[1]=='-':
        f=-1
      t.append(str(int(t[0])+f*int(t[2])))
    m = 0  
    for s in t:
      if len(s)>m:
        m=len(s)
    t.append(m) # last = max-len
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
  lines = []
  for d in data:
    for i in range(len(d)-1):
      if i>=len(lines):
        lines.append("")
      if i==2:
        lines[i] = lines[i] + d[i-1] + ' '  
      lines[i] = lines[i] + d[i] + '    '
  lines = lines[:1] + lines[2:]
  print( '\n'.join(lines) )

  #todo: padd number / separator


  arranged_problems = None
  return arranged_problems

