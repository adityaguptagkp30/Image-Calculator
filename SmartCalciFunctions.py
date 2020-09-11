# Math Perfroming Python file for our Program/Project

import constants as cnst
import numpy as np
import  cv2


# function to process the input string so that we can separate each word and number in a list and return it
def processedText(text):
    newText = ''

    for ch in text:
        if ch == ',' or ch == ' ':
            if len(newText) != 0 and newText[-1] != ' ':
                newText += ' '

        elif ch == '+' or ch == '-' or ch == '/' or ch == '*' or ch == '%' or ch == '^' or ch == '=' or ch == '?':
            if newText[-1] != ' ':
                newText += ' '
            newText += (ch + ' ')


        elif ord(ch) >= 65 and ord(ch) <= 90:
            newText += chr(ord(ch) + 32)

        else:
            newText += ch

    return newText.split()


# function to return operands and operator from list
def operandsOperator(dataArr):
    operands = []
    operator = []

    isFrom = False

    for ele in dataArr:
        if ele in cnst.fromSub:
            isFrom = True

        elif ele in cnst.add:
            operator.append("+")

        elif ele in cnst.subtract:
            operator.append("-")

        elif ele in cnst.difference:
            operator.append("difference")

        elif ele in cnst.multiply:
            operator.append("*")

        elif ele in cnst.divide:
            operator.append("/")

        elif ele in cnst.remainder:
            operator.append("%")

        elif ele in cnst.power:
            operator.append("**")

        elif ele in cnst.introduction:
            operator.append("introduction")

        elif ele in cnst.shutDown:
            operator.append("shutDown")

        else:
            try:
                operands.append(float(ele))
            except:
                pass

    if len(operator) == 1 and operator[0] == "-" and isFrom is True:
        operator.pop()
        operator.append("fromSubtract")

    return operands, operator


# function to get result using multiple operator
def multiOperatorCalci(operands, operator):
    if len(operands) - len(operator) != 1:
        ans = "Sorry, but either the number of operands is more or number of operators is less"
        return ans

    text = ""
    i = 0
    while True:
        text += str(operands[i])

        if i >= len(operator):
            break

        text += str(operator[i])
        i += 1

    try:
        return eval(text)

    except:

        img = np.ones((150, 900, 1), np.uint8) * 255
        cv2.putText(img, "OUTPUT: DIVIDING BY ZERO ERROR ", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2,
                    cv2.LINE_AA)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        return


def result(operands, operator):
    if len(operator) == 0:
        return cnst.unable

    elif len(operator) == 1:

        if operator[0] == '+':
            ans = sum(operands)

        elif operator[0] == "fromSubtract":
            if len(operands) == 2:
                ans = operands[1] - operands[0]
            else:
                ans = "Sorry, but we can find subtraction of two numbers only..."

        elif operator[0] == "difference":
            if len(operands) == 2:
                ans = operands[0] - operands[1]
                ans = max(ans, 0 - ans)
            else:
                ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

        elif operator[0] == '*':
            ans = 1
            for num in operands:
                ans *= num

        elif operator[0] == 'introduction':
            ans = cnst.intro

        else:
            ans = multiOperatorCalci(operands, operator)

    else:
        ans = multiOperatorCalci(operands, operator)

    if type(ans) == float and ans % 1 == 0:
        ans = int(ans)

    return ans

# function to get result using single operator
# def singleOperatorCalci(operands, operator):
#     ans = ""
#     if operator == "+":
#         ans = sum(operands)

#     elif operator == "-":
#         if len(operands) == 2:
#             ans = operands[0] - operands[1]
#         else:
#             ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

#     elif operator == "fromSubtract":
#         if len(operands) == 2:
#             ans = operands[1] - operands[0]
#         else:
#             ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

#     elif operator == "*":
#         ans = 1
#         for num in operands:
#             ans *= num

#     elif operator == "/":
#         if len(operands) == 2:
#             if operands[1] == 0:
#                 ans = "Sorry but dividing by 0 is not possible"
#             else:
#                 ans = operands[0] / operands[1]
#         else:
#             ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

#     elif operator == "difference":
#         if len(operands) == 2:
#             ans = operands[0] - operands[1]
#             ans = max(ans, 0 - ans)
#         else:
#             ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

#     elif operator == "%":
#         if len(operands) == 2:
#             ans = operands[0] % operands[1]
#         else:
#             ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

#     elif operator == "**":
#         if len(operands) == 2:
#             if operands[0] == 0 and operands[1] < 0:
#                 ans = "Sorry, but negative power of 0 is a Maths error"
#             else:
#                 ans = operands[0] ** operands[1]
#         else:
#             ans = "Sorry, but we can find " + str(operator) + " of two numbers only..."

#     elif operator == "introduction":
#         ans = cnst.intro

#     if type(ans) == float and ans % 1 == 0:
#         ans = int(ans)

#     return ans