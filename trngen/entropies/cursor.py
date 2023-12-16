import pyautogui


class Cursor:
    @staticmethod
    def return_value():
        cursor_x, cursor_y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()
        return (cursor_x * screen_height / screen_width ** 2) + (cursor_y * screen_width / screen_height ** 2)
