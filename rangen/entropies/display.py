import pyautogui
import random


class Display:
    @staticmethod
    def get_random_value_from_region(region):
        screenshot = pyautogui.screenshot(region=region)
        rgb_image = screenshot.convert("RGB")
        pixel_data = list(rgb_image.getdata())
        average_pixel_value = sum(sum(pixel) for pixel in pixel_data) / len(pixel_data)
        random_value = random.uniform(average_pixel_value / 2, average_pixel_value)
        return random_value

    @staticmethod
    def generate_random_region(screen_width, screen_height, max_width_percentage, max_height_percentage):
        max_region_width = int(screen_width * max_width_percentage / 100)
        max_region_height = int(screen_height * max_height_percentage / 100)

        x = random.randint(1, screen_width - 1)
        y = random.randint(1, screen_height - 1)

        width = random.randint(1, min(max_region_width, screen_width - x))
        height = random.randint(1, min(max_region_height, screen_height - y))

        return x, y, width, height

    def return_value(self):
        screen_width, screen_height = pyautogui.size()
        return self.get_random_value_from_region(self.generate_random_region(screen_width, screen_height, 70, 70))
