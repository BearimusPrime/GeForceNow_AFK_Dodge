from time import sleep
import pygetwindow as gw
import pyautogui


if __name__ == "__main__":
    while True:
        geforce_window = 'tekst'
        lista = gw.getAllTitles()
        print(lista)
        for i in lista:
            if (i.__contains__('GeForce NOW')):
                geforce_window = gw.getWindowsWithTitle(i)[0]
        current_window = gw.getActiveWindow()
        mouse=pyautogui.position()
        print(mouse)
        geforce_window.minimize()
        geforce_window.maximize()
        pyautogui.moveTo(20,50)
        pyautogui.moveTo(900,900)
        pyautogui.moveTo(mouse)
        current_window.minimize()
        current_window.maximize()
        sleep(180)