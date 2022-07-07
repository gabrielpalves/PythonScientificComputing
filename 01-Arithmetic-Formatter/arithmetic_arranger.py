import re

def arithmetic_arranger(problems, showAns=False):
  if len(problems) > 5:
    #raise NameError('Error: Too many problems.')
    #print('Error: Too many problems.')
    arranged_problems = "Error: Too many problems."
    return arranged_problems

  operands = []
  fstarray = []
  secarray = []
  maxlen = []
  for problem in problems:
    txt = re.split(" ", problem)
    while " " in txt:
      txt.remove(" ")
    
    try:
      int(txt[0])
      int(txt[2])
    except:
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems
    
    if txt[1] != "+" and txt[1] != "-":
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems

    # Get the integers that will be printed in the first and second line
    second = False
    fstline = ""
    secline = ""
    for j in problem:
      if j == " ":
        continue
      elif j == "+" or j == "-":
        second = True
        operands.append(j)
      else: # this will be a number for sure
        if second:
          secline += j
        else:
          fstline += j

    fstarray.append(int(fstline))
    secarray.append(int(secline))
    maxlen.append(max(len(fstline),len(secline)))
    
  # Verify if there are numbers with more than four digits
  for i in maxlen:
    if i > 4:
      #print('Error: Numbers cannot be more than four digits.')
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems
    
  # Now prints the operations
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  for i in range(0,len(maxlen)):
    space1 = ' '
    space2 = operands[i]
    space3 = ''
    dashes = ''
    digit1 = str(fstarray[i])
    digit2 = str(secarray[i])
    if operands[i] == '+':
      digit3 = str(fstarray[i]+secarray[i])
    else:
      digit3 = str(fstarray[i]-secarray[i])

    if len(digit1) == maxlen[i]:
      space1 += ' '
      for j in range(0,maxlen[i]-len(digit2)+1):
        space2 += ' '
    else:
      for j in range(0,maxlen[i]-len(digit1)+1):
        space1 += ' '
      space2 += ' '
        
    totalchars = maxlen[i]+2
    for j in range(0,totalchars-len(digit3)):
      space3 += ' '

    for j in range(0,totalchars):
      dashes += '-'

    # join the strings
    line1 = line1+space1+digit1
    line2 = line2+space2+digit2
    line3 = line3+dashes
    line4 = line4+space3+digit3

    # 4 spaces between each operation
    if i != len(maxlen)-1:
      line1 += '    '
      line2 += '    '
      line3 += '    '
      line4 += '    '
  # make it right
  if showAns:
    arranged_problems = line1+'\n'+line2+'\n'+line3+'\n'+line4
  else:
    arranged_problems = line1+'\n'+line2+'\n'+line3
  #print(arranged_problems)
  return arranged_problems