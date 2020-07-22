import re

def arithmetic_arranger(problems, flagDisplay=False):
  # transform input data --------------
  # list of list with 3 elements in each sublist
  data = list() 
  for problem in problems:
    t = problem.split(' ')
    if(len(t)!=3):
      return "Wrong input format. Should be e.g.: 23 + 44."
    fi = 0  
    if flagDisplay: # calc + or -
      fi = 1
      f=1
      if t[1]=='-':
        f=-1
      t.append(str(int(t[0])+f*int(t[2])))

    # find longest string
    # ignore last if flag is true  
    m = 0  
    for i in range(len(t)-fi): 
      l = len(t[i])
      if l>m:
        m=l
   
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
  sep = '';
  between = '    '

  # all problems
  for di in range(len(data)):
    d = data[di]
    m = d[len(d)-1]

    # loop through special problem
    tmp = ''
    for i in range(len(d)-1):
      if i>=len(lines):
        lines.append("")
   
      # space: pre / post
      pre = ' ' * (m - len(d[i]))
      op = '  '

      if i==2: # operator
        op = d[i-1] + ' '
        pre = ' ' * (m - len(d[i]))

      # last row has other rules: there must
      # NOT be an extra space before operator
      if flagDisplay and i==len(d)-2:
        op = ''
        pre = ' ' * (len(tmp) - len(d[i]))

      tmp = op + pre  + d[i]
      lines[i] = lines[i] + tmp
      if di<len(data)-1:
        lines[i] = lines[i] + between

    sep = sep + (m+2)*'-'
    if di<len(data)-1:
      sep = sep + between

  sep.strip()

  if flagDisplay:
    lines = lines[:1] + lines[2:3] + [sep] + lines[3:]
  else:
    lines = lines[:1] + lines[2:3] + [sep]

  arranged_problems = "\n".join(lines)
  return arranged_problems

