from ctypes import windll, Structure, c_long, byref
 
import time
import cv2
import mss
import numpy as np
 
import pyautogui
import keyboard


class POINT(Structure): #В этом классе отслеживаем положение курсора
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition(): #В этой функции мы передаём положение курсора
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y} 

def click(): 
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()




mss = mss.mss()
last_time = time.time()


while True:

    if keyboard.is_pressed("o"):
        quit()
    elif time.time() - last_time < 1: #Задерживаем основной цикл
        print(1)
        continue

    cur = queryMousePosition() #Получаем координаты курсора и грабим часть монитора по координатам мышки

    mon = {
    "top": cur['y'] -10,
    "left": cur['x'] -10,
    "width": 10, 
    "height": 10
    }
    img = np.asarray(mss.grab(mon))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Меняем палитру RGB на HSV
    cv2.imshow('img', img) #Отображаем то что видит программа
        
       

    lower_color = np.array([10,50,15])
    upper_color = np.array([18,255,255])
    mask = cv2.inRange(hsv, lower_color, upper_color) #Создаём маску из спектра цветов
 
  

    # check
    hasColor = np.sum(mask)
    if hasColor > 0:
        print("detected!")
        
    else:
        print("NOT detected!")

        time.sleep(0.3)
        click()
 
        time.sleep(1)
        click()
 
        last_time = time.time()