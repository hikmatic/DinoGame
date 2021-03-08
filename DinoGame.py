from PIL import Image, ImageGrab
import pyautogui
import time

def click(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):
    for i in range(620, 680):
        for j in range(480,510):
            if data[i,j] < 100:
                click("up")
                return


    for i in range(620,650):
        for j in range(400,460):
            if data[i,j] < 171:
                click("down")
                return
    return

if __name__ == "__main__":
    time.sleep(5)
    click('up')

while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    isCollision(data)
    # for i in range(620, 690):
    #     for j in range(480, 510):
    #         data[i, j] = 100
    # image.show()

    # for i in range(600,650):
    #     for j in range(400,460):
    #         data[i,j] = 171
    #
    # image.show()
    #break