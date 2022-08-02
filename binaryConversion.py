class binary():
  def convertToDec(returnVal = False):
    ans = 0
    binaryInput = input("Binary number: ")
    count = -1
    for char in range(len(binaryInput) - 1, -1, -1):
      count += 1
      if binaryInput[char] == "1":
        ans += 2**count
    print(ans)
    if returnVal == True:
      return ans


  def convertToBaseN(decimal, base):
    pass
