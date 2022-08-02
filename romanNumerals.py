numeralsVals = {
  "·" : 1/12,
  "··" : 2/12,
  "···" : 3/12,
  "····" : 4/12,
  "·····" : 5/12,
  ":" : 2/12,
  "∴" : 3/12,
  "∷" : 4/12,
  "⁙" : 5/12,
  "s" : 6/12,
  "s·" : 7/12,
  "s··" : 8/12,
  "s···" : 9/12,
  "s····" : 10/12,
  "s·····" : 11/12,
  "s:" : 8/12,
  "s∴" : 9/12,
  "s∷" : 10/12,
  "s⁙" : 11/12,
  "i" : 1,
  "v" : 5,
  "x" : 10,
  "l" : 50,
  "c" : 100,
  "d" : 500,
  "m" : 1000,
}

dots = ["·", "··", "···", "····", "·····", ":", "∴", "∷", "⁙"]
reverseNumeralsKeys = {v: k for k, v in numeralsVals.items()}
reverseNumeralsKeys = list(reversed(numeralsVals.keys()))

reverseNumeralsVals = {v: k for k, v in numeralsVals.items()}
reverseNumeralsVals = list(reversed(numeralsVals.values()))


class numerals():
  def getVal(letter):
    for key in numeralsVals.keys():
      if letter == key:
        return numeralsVals[key]
  

  def convertToList(numeral):
    numeral = list(numeral.lower())
    for value in range(len(numeral)-1, -1, -1):
      
      for dot in range(0, len(dots)):
        if dots[dot] in numeral[value]:
          if numeral[value-1] == "s" or numeral[value-1] == "·":
            numeral[value-1:value+1] = [numeral[value-1] + numeral[value]]
            break
    return numeral



  def convertToDec(numeral):
    numeral = numerals.convertToList(numeral)
    numeralVals = []
    for letter in range(0, len(numeral)):
      letterVal = numerals.getVal(numeral[letter])
      if letterVal == None:
        raise ValueError("INPUT CONTAINS NON-ROMAN NUMERALS")
      else:
        numeralVals.append(letterVal)
    
    previous = [0]
    for value in range(len(numeralVals)-1, 0, -1):
      if (numeralVals[value] > numeralVals[value - 1]) and (previous[-1] <= numeralVals[value]):
        previous.append(numeralVals[value - 1])
        numeralVals[value-1:value+1] = [numeralVals[value] - numeralVals[value - 1]]

    ans = sum(numeralVals)
    return ans

    
  def convertFromDec(decimal):
    ans = ""
    while decimal > 0:
      for value in range(0, len(reverseNumeralsVals)):
        if (decimal - reverseNumeralsVals[value]) >= 0:
          ans += reverseNumeralsKeys[value]
          decimal -=  reverseNumeralsVals[value]
          break
    return ans