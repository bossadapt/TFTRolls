# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import numpy as nm
import pytesseract
import cv2
import pyautogui
from random import randint
from PIL import ImageGrab

# works with 3 digits
goldCords = (864, 884, 910, 909)
# champs
# 50 padding kinda
# 155 width kinda
c1NameCords = (482, 1045, 630, 1068)
c2NameCords = (690, 1045, 834, 1068)
c3NameCords = (884, 1045, 1035, 1068)
c4NameCords = (1089, 1045, 1240, 1068)
c5NameCords = (1294, 1045, 1435, 1068)
# card of chaps cords
c1CardCords = (482, 928, 630, 1068)
c2CardCords = (690, 928, 834, 1068)
c3CardCords = (884, 928, 1035, 1068)
c4CardCords = (1089, 928, 1240, 1068)
c5CardCords = (1294, 928, 1435, 1068)
#cords of the refresh button
refreshCords = (275, 1005, 459, 1066)

def buyChampByNumber(numb, delay):
    # click randomly in the space of the cards
    x = 0
    y = 0
    if numb == 1:
        x = randint(c1CardCords[0], c1CardCords[2])
        y = randint(c1CardCords[1], c1CardCords[3])
    elif numb == 2:
        x = randint(c2CardCords[0], c2CardCords[2])
        y = randint(c2CardCords[1], c2CardCords[3])
    elif numb == 3:
        x = randint(c3CardCords[0], c3CardCords[2])
        y = randint(c3CardCords[1], c3CardCords[3])
    elif numb == 4:
        x = randint(c4CardCords[0], c4CardCords[2])
        y = randint(c4CardCords[1], c4CardCords[3])
    elif numb == 5:
        x = randint(c5CardCords[0], c5CardCords[2])
        y = randint(c5CardCords[1], c5CardCords[3])
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def clickRefresh():
    x = randint(refreshCords[0], refreshCords[2])
    y = randint(refreshCords[1], refreshCords[3])
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

# cant see gold under 10
# cant see lux, vi
#todo figure out why short names are not read
def getSringFromCord(cords):
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    image = ImageGrab.grab(bbox=cords)
    image_string = pytesseract.image_to_string(cv2.cvtColor(nm.array(image), cv2.COLOR_BGR2GRAY), lang='eng')
    image_string = image_string.replace(" " and "\n", "")
    return image_string


def getCurrentShop():
    c1 = getSringFromCord(c1NameCords)
    c2 = getSringFromCord(c2NameCords)
    c3 = getSringFromCord(c3NameCords)
    c4 = getSringFromCord(c4NameCords)
    c5 = getSringFromCord(c5NameCords)
    gold = getSringFromCord(goldCords)
    return [c1, c2, c3, c4, c5, gold]


def rollDown(target_gold, champ_list):
    current_gold = int(getSringFromCord(goldCords))
    while int(target_gold) + 2 < int(current_gold):
        current_shop = getCurrentShop()
        print("Current shop =" + str(current_shop))
        current_gold = current_shop[5]
        for champ in champ_list:
            print("checking for "+ champ + "...")
            itemDeletionCount = 0
            while champ in current_shop:
                indexOfItem = current_shop.index(champ)
                buyChampByNumber(indexOfItem + 1 + itemDeletionCount, 0.1)
                print(champ + " purchased")
                del current_shop[indexOfItem]
                itemDeletionCount += 1
        print("Refreshing...")
        clickRefresh()



if __name__ == '__main__':
    animas = ["Sylas", "Nasus", "Riven", "Vayne", "Jinx", "Miss Fortune"]
    rollDown(15, animas)
    # print(str(getCurrentShop()))
    # print(getSringFromCord(c1NameCords))
    # buyChampByNumber(3, 1)
