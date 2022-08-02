from romanNumerals import numerals


print("WARNING: NO EQUATION OR (2+ NESTED) BRACKETS YET")
print("If you are Roman, type \'#\' at the beginning of the sum. Use \'x\' for multiplication and \'X\' for 10")
print("Si Romanum estis, scribe \'#\' ante computo. \'x\' multiplicatio enim utare et \'X\' 10 enim")
print("If you are a computer, use \'@\' at the beginning of the sum")
print("Use \'=\' for bidmas and exclude \'=\' for sequence")


specialCases = ["(", ")"]
operators = ["^", "/", "x", "+", "-"]
operatorsExplained = ["a to the power of b", "a divided by b", "a multiplied by b", "a add b", "a subtract b"]

romanOperators = ["^", "/", "*", "+", "-"]
allRomanOperators = ["(", ")", "^", "/", "*", "+", "-"]


allOperators = ["(", ")", "^", "/", "x", "+", "-"]
operate = [lambda a, b:a**b, lambda a, b : a / b, lambda a, b : a * b, lambda a, b : a + b, lambda a, b : a - b]


def explainOperators():
  for i in range(0, len(operators)):
    print(f"a {operators[i]} b : {operatorsExplained[i]}")


def stringToList(string):
  string = list(string)
  for item in range(len(string) - 1, -1, -1):
    if string[item] in operators or string[item] == "=":
      string[item:item + 1] = ["|", string[item], "|"]
  string = "".join(string)
  string = string.split("|")
  if string[-1] == "":
    string.pop(-1)
  return string


def findBracketsNumber(sumList, valueReturn = None):
  numberOfPairs = 0
  openBracketNumber = 0
  openBracketPlacements = []
  closeBracketNumber = 0
  closeBracketPlacements = []
  returnableValues = [openBracketNumber, openBracketPlacements, closeBracketNumber, closeBracketPlacements]
  for item in range(0, len(sumList)):
    if "(" in str(sumList[item]):
      listOfItems = list(str(sumList[item]))
      for i in range(0, len(listOfItems)):
        if "(" in listOfItems[i]:
          openBracketNumber += 1
      openBracketPlacements.append(item)

    elif ")" in str(sumList[item]):
      listOfItems = list(str(sumList[item]))
      for i in range(0, len(listOfItems)):
        if ")" in listOfItems[i]:
          closeBracketNumber += 1
      closeBracketPlacements.append(item)


  if openBracketNumber == closeBracketNumber:
    numberOfPairs = 0
    counter = 0
    for term in range(0, len(sumList)):
      if "(" in str(sumList[term]):
        listOfItems = list(str(sumList[term]))
        for i in range(0, len(listOfItems)):
          if "(" in listOfItems[i]:
            counter += 1
      if ")" in str(sumList[term]):
        listOfItems = list(str(sumList[term]))
        for i in range(0, len(listOfItems)):
          if ")" in listOfItems[i]:
            counter -= 1
            if counter == 0:
              numberOfPairs += 1


  if valueReturn == "pairs":
    return numberOfPairs
  elif valueReturn != None:
    return returnableValues[valueReturn]
  else:
    return openBracketNumber, closeBracketNumber, openBracketPlacements, closeBracketPlacements


def findbidmas(sumList):
  firstBracket = "You messed up the brackets"
  lastBracket = "You messed up the brackets"
  order = []
  openBracketNumber, closeBracketNumber, openBracketPlacements, closeBracketPlacements = findBracketsNumber(sumList)
  if openBracketNumber == closeBracketNumber:
    if openBracketNumber == 0:
      for operator in range(2, len(allOperators)):
        if allOperators[operator] in sumList:
          for number in range(1, len(sumList) - 1, 2):
            if sumList[number] == allOperators[operator]:
              alist = [number, operator]
              order.append(alist)
    elif findBracketsNumber(sumList, "pairs") > 0:
      print(sumList)
      counter = 0
      for term in range(0, len(sumList)):
        counter = 0
        end = False
        openBrackets = []
        closeBrackets = []
        for term in range(0, len(sumList)):
          if "(" in str(sumList[term]):
            openBrackets.append(term)
            listOfItems = list(str(sumList[term]))
            for i in range(0, len(listOfItems)):
              if "(" in listOfItems[i]:
                counter += 1
          if ")" in str(sumList[term]):
            closeBrackets.append(term)
            listOfItems = list(str(sumList[term]))
            for i in range(0, len(listOfItems)):
              if ")" in listOfItems[i]:
                counter -= 1
                if counter == 0:
                  bracketedSection = sumList[openBrackets[0]:closeBrackets[-1] + 1]
                  bracketedSection[0] = list(bracketedSection[0])
                  bracketedSection[0].pop(0)
                  bracketedSection[0] = "".join(bracketedSection[0])
                  bracketedSection[-1] = list(bracketedSection[-1])
                  bracketedSection[-1].pop(-1)
                  bracketedSection[-1] = "".join(bracketedSection[-1])
                  bracketedSection.append("=")

                  bracketedSection = solve.sum.bidmas(bracketedSection)
                
                  sumList[openBrackets[0]:closeBrackets[-1] + 1] = [bracketedSection]

                  solve.sum.bidmas(sumList)
                  end = True
          if end == True:
            break

    else:
      print(sumList)
      for number in range(0, len(sumList) - 1):
        print(number)
        if "(" in sumList[number]:
          firstBracket = number
          print(firstBracket, end = "...\n")
          break
      number = len(sumList) - 1
      while True:
        number -= 1
        if ")" in sumList[number]:
          lastBracket = number
          print(lastBracket, end = "...\n")
          print(firstBracket, lastBracket, end = "\n\n\n")
          bracketedSection = sumList[firstBracket:lastBracket + 1]
          bracketedSection[0] = list(bracketedSection[0])
          bracketedSection[0].pop(0)
          bracketedSection[0] = "".join(bracketedSection[0])
          bracketedSection[-1] = list(bracketedSection[-1])
          bracketedSection[-1].pop(-1)
          bracketedSection[-1] = "".join(bracketedSection[-1])
          bracketedSection.append("=")
          bracketedSection = solve.sum.bidmasForBrackets(bracketedSection)
        
          sumList[firstBracket:lastBracket + 1] = [bracketedSection]
          solve.sum.bidmas(sumList)
          break


    return order
  else:
    raise ValueError("BRACKETS PLACEMENT INCORRECT")


class solve():
  class sum():
    def sequence(sumList):
      ans = []
      sumTotalNum = len(sumList)
      for number in range(0, sumTotalNum, 2):
        if sumList[number + 1] != "=":
          for operator in range(0, len(operators)):
            if operators[operator] == sumList[number + 1]:
              if number == 0:
                ans.append(operate[operator](float(sumList[0]), float(sumList[2])))
              else:
                ans.append(operate[operator](float(ans[-1]), float(sumList[number + 2])))
        else:
          return solveSumType(ans[-1])

    def bidmas(sumList):
      order = findbidmas(sumList)
      ans = []
      for operator in range(0, len(order)):
        print(sumList)
        a = float(sumList[order[operator][0] - 1])
        b = float(sumList[order[operator][0] + 1])
        ans.append(operate[order[operator][1] - 2](a, b))
        sumList[order[operator][0] - 1 : order[operator][0] + 2] = [ans[-1]]
        if operator == len(order) - 1:
          returnVal = list(map(int, str(ans[-1]).split(".")))
          if returnVal[1] == 0:
            answer = int(ans[-1])
          else:
            answer = ans[-1]
          answer = solveSumType(answer)
          print(answer)
          return answer

        for operator2 in range(0, len(order)):
          if order[operator2][0] > order[operator][0]:
            number = order[operator2][0] - 2
            order[operator2].pop(0)
            order[operator2].insert(0, number)

    def bidmasForBrackets(sumList):
      order = findbidmas(sumList)
      ans = []
      for operator in range(0, len(order)):
        print(sumList)
        a = float(sumList[order[operator][0] - 1])
        b = float(sumList[order[operator][0] + 1])
        ans.append(operate[order[operator][1] - 2](a, b))
        sumList[order[operator][0] - 1 : order[operator][0] + 2] = [ans[-1]]
        if operator == len(order) - 1:
          returnVal = list(map(int, str(ans[-1]).split(".")))
          if returnVal[1] == 0:
            answer = int(ans[-1])
          else:
            answer = ans[-1]
          answer = solveSumType(answer)
          print(answer)
          return answer

        for operator2 in range(0, len(order)):
          if order[operator2][0] > order[operator][0]:
            number = order[operator2][0] - 2
            order[operator2].pop(0)
            order[operator2].insert(0, number)
        
  def equation(sumList):
    pass

def solveSumType(answer):
  if numberSystem == "arabic":
    return answer
  elif numberSystem == "roman":
    if 0 < answer <= 3999:
      return numerals.convertFromDec(answer).upper()
    else:
      return answer
  elif numberSystem == "binary":
    if (answer >= 0):# and (type(answer) == "int"):
      try:
        answer = bin(int(answer))
#        answer = answer.split("b")   #if you want there to not be 0b in front of answer
#        answer = answer[-1]

      except:
        pass
      return answer


explainOperators()

while True:

  numberSystem = "arabic"


  vsum = input("\n\n>>> ").replace(" ", "")
  sumList = stringToList(vsum)

  if len(sumList) == 1:
    print("".join(sumList))

  else:
    if sumList[0][0] == "#":
      numberSystem = "roman"
      sumList[0] = list(sumList[0])
      sumList[0].pop(0)
      sumList[0] = "".join(sumList[0])
      for number in range(0, len(sumList), 2):
        if type(sumList[number]) != "int":
          sumList[number] = numerals.convertToDec(sumList[number])

    elif sumList[0][0] == "@":
      numberSystem = "binary"
      sumList[0] = list(sumList[0])
      sumList[0].pop(0)
      sumList[0] = "".join(sumList[0])
      for number in range(0, len(sumList), 2):
        if type(sumList[number]) != "int":
          sumList[number] = int(sumList[number], 2)

    if sumList[-1] == "=":
      answer = solve.sum.bidmas(sumList)

    elif "=" in sumList:
      answer = solve.equation(sumList)

    else:
      sumList.append("=")
      if findBracketsNumber(sumList, 0) == 0:
        answer = solve.sum.sequence(sumList)
        print(answer)
      elif findBracketsNumber(sumList, 0) >= 2 or findBracketsNumber(sumList, 1) >= 2:
        raise ValueError("NESTED BRACKETS")
      else:
        solve.sum.bidmas(sumList)