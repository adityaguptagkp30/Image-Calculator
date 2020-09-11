# runner file for our program

import constants as cnst
import SmartCalciFunctions as sm
import imgToTextRecog as itr
import numpy as np
import cv2


print(cnst.intro)
while True:
    imgPath = input("Enter image name with extension: ")

    text = itr.getTextFromImage(imgPath)

    dataArr = sm.processedText(text)

    operands, operator = sm.operandsOperator(dataArr)

    if len(operator) == 1 and operator[0] == "shutDown":
        print(cnst.byeBye)
        break

    ans = sm.result(operands, operator)

    if type(ans) is int or type(ans) is float:
        print(cnst.successMsg)

        img = np.ones((300, 550, 1), np.uint8) * 255
        cv2.putText(img, "OUTPUT: " + str(ans), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
