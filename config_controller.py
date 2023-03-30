# Author Vodohleb04
from enum import Enum
from typing import Dict, NoReturn

import colors
import json

"""
screen_width = 800
screen_height = 600
background_image = './images/backgrounds/space.jpg'

frame_rate = 90

row_count = 6
brick_width = 60
brick_height = 20
brick_color = colors.RED1
offset_y = brick_height + 10

bowl_speed = 3
bowl_radius = 8
bowl_color = colors.GREEN

paddle_width = 80
paddle_height = 10
paddle_color = colors.ALICEBLUE
paddle_speed = 6

status_offset_y = 5

text_color = colors.YELLOW1
initial_lives = 3
lives_right_offset = 85
lives_offset = screen_width - lives_right_offset
score_offset = 5

font_name = 'Arial'
font_size = 20

effect_duration = 20
sounds_effects = dict(
    brick_hit='./sounds/sound_effects/brick_hit.mp3',
    paddle_hit='./sounds/sound_effects/paddle_hit.mp3',
    minus_hp="./sounds/sound_effects/minus_hp.mp3",
    death="./sounds/sound_effects/sound_of_dead.mp3",
    effect_done='./sounds/sound_effects/bonus_taken_effect.mp3',
    level_complete='./sounds/sound_effects/win_sound_1.mp3',
    bonus_taken='./sounds/sound_effects/bonus_taken_effect.mp3',
    start='./sounds/sound_effects/start_game.mp3',
    new_record='./sounds/sound_effects/new_record.mp3',
    win1='./sounds/sound_effects/win_sound_1.mp3',
    win2='./sounds/sound_effects/win_sound_2.mp3'
)

death_message_duration = 5
start_message_duration = 2
win_message_duration = 4

button_text_color = colors.WHITE,
button_normal_back_color = colors.INDIANRED1
button_hover_back_color = colors.INDIANRED2
button_pressed_back_color = colors.INDIANRED3

menu_offset_x = 20
menu_offset_y = 300
menu_button_w = 80
menu_button_h = 50
"""

GENERAL_CONFIGS_FILE = "./configs/general_configs.json"


class Levels(Enum):
    LEVEL1 = "./configs/levels/level1.json"
    LEVEL2 = "./configs/levels/level2.json"
    LEVEL3 = "./configs/levels/level3.json"
    LEVEL4 = "./configs/levels/level4.json"
    LEVEL5 = "./configs/levels/level5.json"


class ConfigController:

    def __init__(self):
        unpacked_data: Dict = self._load_json_config(GENERAL_CONFIGS_FILE)
        self._unpack_general_params(unpacked_data["general_params"])
        self._unpack_objects_params(unpacked_data["objects_params"])
        self._unpack_info_panels_params(unpacked_data["info_panels_params"])
        self._unpack_text_message_params(unpacked_data["text_message_params"])

    @staticmethod
    def _load_json_config(filename: str) -> Dict:
        if not filename.endswith('.json'):
            raise ValueError(f"Excepted .json file, got {filename} instead")
        with open(filename, 'r') as config_file:
            if config_file:
                return json.load(config_file)
            raise ValueError(f"No such file {filename}")

    def _unpack_general_params(self, unpacked_data: Dict) -> NoReturn:
        self.background_image = unpacked_data["background_image"]
        self.screen_width = unpacked_data["screen_width"]
        self.screen_height = unpacked_data["screen_height"]
        self.frame_rate = unpacked_data["frame_rate"]
        self.effect_duration = unpacked_data["effect_duration"]
        self.initial_lives = unpacked_data["initial_lives"]
        self.background_music_duration = unpacked_data["background_music_duration"]
        self.sounds_effects = unpacked_data["sounds_effects"]
        self.level_open_flags = unpacked_data["level_open_flags"]

    def _unpack_objects_params(self, unpacked_data: Dict) -> NoReturn:
        self.menu_offset_x = unpacked_data["menu_offset_x"]
        self.menu_offset_y = unpacked_data["menu_offset_y"]
        self.menu_button_w = unpacked_data["menu_button_w"]
        self.menu_button_h = unpacked_data["menu_button_h"]
        self.button_text_color = unpacked_data["button_text_color"]
        self.button_normal_back_color = unpacked_data["button_normal_back_color"]
        self.button_hover_back_color = unpacked_data["button_hover_back_color"]
        self.button_pressed_back_color = unpacked_data["button_pressed_back_color"]

        self.brick_width = unpacked_data["brick_width"]
        self.brick_height = unpacked_data["brick_height"]
        self.brick_color = unpacked_data["brick_color"]

        self.bowl_speed = unpacked_data["bowl_speed"]
        self.bowl_radius = unpacked_data["bowl_radius"]
        self.bowl_color = unpacked_data["bowl_color"]
        self.bowl_acceleration = unpacked_data["bowl_acceleration"]

        self.paddle_width = unpacked_data["paddle_width"]
        self.paddle_height = unpacked_data["paddle_height"]
        self.paddle_color = unpacked_data["paddle_color"]
        self.paddle_speed = unpacked_data["paddle_speed"]

    def _unpack_bricks_location_params(self, unpacked_data: Dict) -> NoReturn:
        self.row_count = unpacked_data["row_count"]
        self.brick_width = unpacked_data["brick_width"]
        self.offset_y = unpacked_data["offset_y"]

    def _unpack_info_panels_params(self, unpacked_data: Dict) -> NoReturn:
        self.status_offset_y = unpacked_data["status_offset_y"]
        self.text_color = unpacked_data["text_color"]
        self.lives_right_offset = unpacked_data["lives_right_offset"]
        self.lives_offset = unpacked_data["lives_offset"]
        self.score_offset = unpacked_data["score_offset"]

    def _unpack_text_message_params(self, unpacked_data: Dict) -> NoReturn:
        self.font_name = unpacked_data["font_name"]
        self.font_size = unpacked_data["font_size"]
        self.death_message_duration = unpacked_data["death_message_duration"]
        self.start_message_duration = unpacked_data["start_message_duration"]
        self.win_message_duration = unpacked_data["win_message_duration"]

    def load_level_info(self, level_number: Levels) -> NoReturn:
        if isinstance(level_number, Levels):
            self._unpack_bricks_location_params(self._load_json_config(level_number.value)["bricks_location_params"])
            self.bowl_acceleration_interval = self._load_json_config(level_number.value)["bowl_acceleration_interval"]
            self.level_records = self._load_json_config(level_number.value)["level_records"]
            self.level_records = dict(sorted(self.level_records.items(), key=lambda item: item[1], reverse=True))
            self.level_config_file = level_number.value
        else:
            raise ValueError(f"Unknown level {level_number}")

    def update_level_config(self) -> NoReturn:
        if not self.level_config_file.endswith('.json'):
            raise ValueError(f"Excepted .json file, got {self.level_config_file} instead")
        with open(self.level_config_file, 'w') as config_file:
            if config_file:
                new_config_data = {
                    "bowl_acceleration_interval": self.bowl_acceleration_interval,
                    "level_records": self.level_records,
                    "bricks_location_params": {
                        "row_count": self.row_count,
                        "brick_width": self.brick_width,
                        "offset_y": self.offset_y
                    }
                }
                return json.dump(new_config_data, config_file, indent='\t')
            raise ValueError(f"No such file {self.level_config_file}")

    def _pack_general_params(self):
        return {
            "background_image": self.background_image,
            "screen_width": self.screen_width,
            "screen_height": self.screen_height,
            "frame_rate": self.frame_rate,
            "effect_duration": self.effect_duration,
            "initial_lives": self.initial_lives,
            "background_music_duration": self.background_music_duration,
            "sounds_effects": self.sounds_effects,
            "level_open_flags": self.level_open_flags
        }

    def _pack_object_params(self):
        return {
            "menu_offset_x": self.menu_offset_x,
            "menu_offset_y": self.menu_offset_y,
            "menu_button_w": self.menu_button_w,
            "menu_button_h": self.menu_button_h,
            "button_text_color": self.button_text_color,
            "button_normal_back_color": self.button_normal_back_color,
            "button_hover_back_color": self.button_hover_back_color,
            "button_pressed_back_color": self.button_pressed_back_color,
            "brick_width": self.brick_width,
            "brick_height": self.brick_height,
            "brick_color": self.brick_color,
            "bowl_speed": self.bowl_speed,
            "bowl_radius": self.bowl_radius,
            "bowl_color": self.bowl_color,
            "bowl_acceleration": self.bowl_acceleration,
            "paddle_width": self.paddle_width,
            "paddle_height": self.paddle_height,
            "paddle_color": self.paddle_color,
            "paddle_speed": self.paddle_speed
        }

    def _pack_info_panels_params(self):
        return {
            "status_offset_y": self.status_offset_y,
            "text_color": self.text_color,
            "lives_right_offset": self.lives_right_offset,
            "lives_offset": self.lives_offset,
            "score_offset": self.score_offset
        }

    def _pack_text_message_params(self):
        return {
            "font_name": self.font_name,
            "font_size": self.font_size,
            "death_message_duration": self.death_message_duration,
            "start_message_duration": self.start_message_duration,
            "win_message_duration": self.win_message_duration
        }

    def update_general_config(self) -> NoReturn:
        new_config_data = {
            "general_params": self._pack_general_params(),
            "objects_params": self._pack_object_params(),
            "info_panels_params": self._pack_info_panels_params(),
            "text_message_params": self._pack_text_message_params()
        }
        with open(GENERAL_CONFIGS_FILE, 'w') as config_file:
            json.dump(new_config_data, config_file, indent='\t')

"""
if __name__ == "__main__":
    with open(GENERAL_CONFIGS_FILE, "w") as f:
        json.dump({
            "general_params": {
                "background_image": "./images/backgrounds/space.jpg",
                "screen_width": 800,
                "screen_height": 600,
                "frame_rate": 90,
                "effect_duration": 20,
                "initial_lives": 3,
                "sounds_effects": {
                    "brick_hit": "./sounds/sound_effects/brick_hit.mp3",
                    "paddle_hit": "./sounds/sound_effects/paddle_hit.mp3",
                    "minus_hp": "./sounds/sound_effects/minus_hp.mp3",
                    "death": "./sounds/sound_effects/sound_of_dead.mp3",
                    "effect_done": "./sounds/sound_effects/bonus_taken_effect.mp3",
                    "level_complete": "./sounds/sound_effects/win_sound_1.mp3",
                    "bonus_taken": "./sounds/sound_effects/bonus_taken_effect.mp3",
                    "start": "./sounds/sound_effects/start_game.mp3",
                    "new_record": "./sounds/sound_effects/new_record.mp3",
                    "win1": "./sounds/sound_effects/win_sound_1.mp3",
                    "win2": "./sounds/sound_effects/win_sound_2.mp3",
                    "background_music": "./sounds/background_music/menu_music.mp3"
                }
            },
            "objects_params": {
                "menu_offset_x": 20,
                "menu_offset_y": 300,
                "menu_button_w": 80,
                "menu_button_h": 50,
                "button_text_color": colors.WHITE,
                "button_normal_back_color": colors.INDIANRED1,
                "button_hover_back_color": colors.INDIANRED2,
                "button_pressed_back_color": colors.INDIANRED3,
                "brick_width": 60,
                "brick_height": 20,
                "brick_color": colors.RED1,
                "bowl_speed": 3,
                "bowl_radius": 8,
                "bowl_color": colors.GREEN,
                "paddle_width": 80,
                "paddle_height": 10,
                "paddle_color": colors.ALICEBLUE,
                "paddle_speed": 6
            },
            "info_panels_params": {
                "status_offset_y": 5,
                "text_color": colors.YELLOW1,
                "lives_right_offset": 85,
                "lives_offset": 715,
                "score_offset": 5
            },
            "text_message_params": {
                "font_name": "Arial",
                "font_size": 20,
                "death_message_duration": 5,
                "start_message_duration": 2,
                "win_message_duration": 4
            },
            "level_open_flags": {
                "LEVEL1": True,
                "LEVEL2": False,
                "LEVEL3": False,
                "LEVEL4": False,
                "LEVEL5": False
            }
        }, f, indent="\t")
"""
