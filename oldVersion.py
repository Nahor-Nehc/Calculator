actions = ["operations"]
consequence = ["Operations:\n'*' (multiply)\n'/' (divide)\n'+' (add)\n'-' (subtract)\n'=' use at the end for a sum or in the middle for an equation"]

operations = ["*", "/", "-", "+", "=", "(", ")"]
brackets = ["(", ")"]

def main(sum):
  ctype = calctype(sum)
  emptyString = ""
  if ctype == "sum":
    count, countNumbers = findOperationAmount(sum)
    newSum = []
    start = 0
    for op in range(0, count):
      numbers = []
      positions = []
      for i2 in range(start, countNumbers[op]):
        numbers.append(sum[i2])
        positions.append(i2)
      start = int(countNumbers[op]) + 1
      numb = emptyString.join(numbers)
      newSum.append(numb)
      newSum.append(sum[countNumbers[op]])
    sum = newSum
    print(sum)
    bidmas(sum)



  elif ctype == "equation":
    print("Incomplete functionality")

def bidmas(sum):
  order = []
  pos = []
  ops = []
  char = 1
  while char < len(sum):
    ops.append(sum[char])
    char += 2
  for i in range(0, len(ops)):
    if ops[i] == "(":
      for i2 in range(i, len(ops)):
        pass
##        if#closing bracket search ---> if none, end process  |  use var to check at end
  

def findOperationAmount(sum):
  count = 0
  countNumbers = []
  for char in range(0, len(sum)):
    if sum[char] in operations:
      count += 1
      countNumbers.append(char)
  return count, countNumbers

def calculateMaths():
  pass

def calctype(sum):
  ctype = None
  if sum[-1] == "=":
    ctype = "sum"
  elif "=" in sum:
    ctype = "equation"
  return ctype



sum = input(">>> ")


if sum in actions:
  for i in range(0, len(actions)):
    if sum == actions[i]:
      print(consequence[i])
else:
  spaces = []
  sum = list(sum)
  sum2 = []
  for i2 in range(0, len(sum)):
    if sum[i2] != " ":
      sum2.append(sum[i2])
  sum = sum2
  main(sum)