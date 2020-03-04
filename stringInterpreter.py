

# Desc: Detect whether it' float
# Param: String
# Retval: True/ False
def isFloat(expression):
    # If expression is num. equal float , Example: 1.
    if len(expression) > 1:
        if (expression[0].isdigit()) & (expression[1] == '.'):
            return True
        else:
            return False
    else:
        return False


# Desc: Add space between characters of the string
#       (will not add if there are already space between character)
# Param: Expression to add spaces
# Retval: Expression with spaces between characters
def addSpaceBetweenCharacters(expression):
    elementNo = 0
    tempNo = 1
    expressionCopy = expression
    expressionLength = len(expression)
    while expressionLength != 1:    # Last character no need to check/ add
        if (expression[elementNo+1] != ' ') & (not isFloat(expression[elementNo] + expression[elementNo + 1])):
            expressionCopy = insertCharactersInString(' ', expressionCopy, elementNo+tempNo)    # Update the new string
            tempNo += 1
            elementNo += 1
        expressionLength -= 1
    return expressionCopy


# Decs: Insert string/ character at the specified location (index)
# Param: String/ character to add, Original string, index
# Retval: New string with added string/ character
# Ref: https://stackoverflow.com/questions/5254445/add-string-in-a-certain-position-in-python
def insertCharactersInString(characters, expression, index):
    return expression[:index] + characters + expression[index:]


# Desc: Check whether the string is number (int/ double/ float)
# Param: String
# Retval: True/ False
# Ref: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float/354130
def isNumber(expression):
    try:
        float(expression)
        return True
    except ValueError:
        return False


# Desc: Check whether the character is a operator for calculations
# Param: Character
# Retval: True/ False
def isOperator(expression):
    operatorList = ('+', '-', '*', '/', '(', ')')
    if len(expression) > 1:  # Raise exception when string is received
        raise ValueError("Exception: isOperator() received string as input parameter instead of character.")
    elif not type(expression) == str:  # Raise exception when non character is received
        raise ValueError("Exception: isOperator() received non character as input parameter instead of character.")
    else:  # Find whether parameter is match with operatorList, if yes then return True, else raise exception
        index = 0
        listLength = len(operatorList)
        while listLength != 0:
            if expression == operatorList[index]:
                return True
            else:
                index += 1
                listLength -= 1

        raise ValueError("Exception: isOperator() received invalid operator.")


# Desc: Convert String to Number
# Param: String
# Retval: Number (int or float)
def stringToNumber(expression):
    if isNumber(expression):
        return float(expression)
    else:
        raise ValueError("Exception: stringToNumber() received invalid parameter to be convert.")


# Desc: Move String to right (like moving pointer in c)
# Param: String, iteration to move the str
# Retval: Moved String
def moveStr(expression, iteration):
    newExpression = ""
    expressionLength = len(expression)
    noOfIterations = expressionLength - iteration
    while noOfIterations != 0:
        newExpression += expression[iteration]
        iteration += 1
        noOfIterations -= 1
    return newExpression


# Desc: Extract token from string
# Param: String
# Retval: Token
#def getTokenFromStr(expression):