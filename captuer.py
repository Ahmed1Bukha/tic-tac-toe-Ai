import pyautogui
from PIL import Image
import time

XY = [[156, 238], [858, 744]]

time.sleep(2)
game_board = pyautogui.screenshot()


left = XY[0][0]
top = XY[0][1]
right = XY[1][0]
bottom = XY[1][1]


game_board1 = game_board.crop((left, top, right, bottom))

game_board1.show()
