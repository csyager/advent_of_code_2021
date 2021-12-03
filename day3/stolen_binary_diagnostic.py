# Import problem input
file = open("input.txt", "r")
input = []
for line in file:
  input.append(line.strip())


def oxigengeneratorrating(input, bit):
  if len(input)==1:
    print(input)
    return input
  else:
    ones = 0
    zeros = 0
    for data in input:
      if data[bit]=='1':
        ones+=1
      else: 
        zeros+=1
    
    filtered=[]
    if ones>=zeros:
      for data in input:
        if data[bit]=='1':
          filtered.append(data)
      return oxigengeneratorrating(filtered, bit+1)
    else:
      for data in input:
        if data[bit]=='0':
          filtered.append(data)
      return oxigengeneratorrating(filtered, bit+1)
    

def co2scrubberrating(input, bit):
  if len(input)==1:
    print(input)
    return input
  else:
    ones = 0
    zeros = 0
    for data in input:
      if data[bit]=='1':
        ones+=1
      else: 
        zeros+=1
    
    filtered=[]
    if ones>=zeros:
      for data in input:
        if data[bit]=='0':
          filtered.append(data)
      return co2scrubberrating(filtered, bit+1)
    else:
      for data in input:
        if data[bit]=='1':
          filtered.append(data)
      return co2scrubberrating(filtered, bit+1)
      
    
O2 = int(oxigengeneratorrating(input, 0)[0], 2)
CO2 = int(co2scrubberrating(input, 0)[0], 2)
lifesupportrating = O2*CO2
print(lifesupportrating)
