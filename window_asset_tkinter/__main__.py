"""
    File in charge of testing the window_asset_tkinter module
"""

from typing import Dict, Any

import os

import tkinter as tk

print(f"__name__ = {__name__}")

try:
    from window_tools import WindowTools
    from err_messages import ErrMessages
    from action_assets import ActionAssets
    from calculate_window_position import CalculateWindowPosition
except ModuleNotFoundError:
    from .window_tools import WindowTools
    from .err_messages import ErrMessages
    from .action_assets import ActionAssets
    from .calculate_window_position import CalculateWindowPosition
except ImportError:
    from .window_tools import WindowTools
    from .err_messages import ErrMessages
    from .action_assets import ActionAssets
    from .calculate_window_position import CalculateWindowPosition

__all__ = [
    "WindowTools",
    "ErrMessages",
    "ActionAssets",
    "CalculateWindowPosition"
]

if __name__ == "__main__":
    def test_the_error_message_class() -> None:
        """_summary_
        This is a function in charge of testing the error message class
        """
        LORE = False
        print("Please launch the main program")

        FILE_INFO: Dict[str, Dict[str, Any]] = {
            "err_message": {
                "width": 300,
                "height": 110,
                "min_width": 300,
                "min_height": 110,
                "max_width": 1000,
                "max_height": 1000,
                "window_position_x": 0,
                "window_position_y": 0,
                "resizable": True,
                "dark_mode_enabled": False,
                "full_screen": False,
                "dark_mode": {
                    "background": "#000000",
                    "foreground": "#FFFFFF"
                },
                "light_mode": {
                    "background": "#FFFFFF",
                    "foreground": "#000000"
                },
                "background": "#000000",
                "foreground": "#FFFFFF",
                "font_size": 12,
                "font_family": "Times New Roman",
                "debug_mode_enabled": False,
                "icon_path": f"{os.path.dirname(os.path.abspath(__file__))}/assets/favicon.ico",
                "button_width": 10,
                "button_height": 1,
                "error_icon_path": f"{os.path.dirname(os.path.abspath(__file__))}/assets/error_64x64.png",
                "warning_icon_path": f"{os.path.dirname(os.path.abspath(__file__))}/assets/warning_64x64.png",
                "information_icon_path": f"{os.path.dirname(os.path.abspath(__file__))}/assets/information_64x64.png",
                "image_width": 64,
                "image_height": 64
            }
        }
        PRINT_DEBUG = False
        if LORE is True:
            FILE_INFO["err_message"]["debug_mode_enabled"] = True
            PRINT_DEBUG = True

        BASE_WINDOW = tk.Tk()
        CWD = os.getcwd()
        EMI = ErrMessages(
            BASE_WINDOW,
            FILE_INFO,
            print_debug=PRINT_DEBUG,
            cwd=CWD
        )
        win = EMI.init_plain_window(BASE_WINDOW)
        win.update()
        EMI.simple_err_message(
            my_window=win,
            title="Test message error",
            message="This is a test message for the error message box",
            button=EMI.button_options["ok"],
            always_on_top=True,
            command=[win.destroy]
        )
        win = EMI.init_plain_window(BASE_WINDOW)
        EMI.simple_warning_message(
            my_window=win,
            title="Test message warning",
            message="This is a test message for the warning message box",
            button=EMI.button_options["ok"],
            always_on_top=True,
            command=[win.destroy]
        )
        EMI.window = EMI.init_plain_window(BASE_WINDOW)
        EMI.simple_information_message(
            my_window=EMI.window,
            title="Test message information",
            message="This is a test message for the inform message box",
            button=EMI.button_options["o/c"],  # button_options["c/a"],
            always_on_top=True,
            command=[EMI.window.destroy, EMI.window.destroy]
        )
        EMI.advanced_warning_message(
            parent_window=BASE_WINDOW,
            title="You have found a corps",
            message="You have found a rotting corps",
            button=EMI.button_options["ok"],
            always_on_top=True
        )
        RESPONSE = EMI.advanced_information_message(
            parent_window=BASE_WINDOW,
            title="Save corps?",
            message="Do you wish to save the rotting corpse to your inventory?",
            button=EMI.button_options["s/d/c"],
            always_on_top=True
        )
        EMI.err_message_print_debug(f"RESPONSE = {RESPONSE}")
        response_sentence = {
            0: "undefined",
            1: "save",
            2: "not save",
            3: "ignore"
        }
        if RESPONSE == 0:
            if LORE is True:
                window = EMI.init_plain_window()
            EMI.advanced_err_message(
                parent_window=BASE_WINDOW,
                title="Error",
                message="You have not chosen a response!\nThus, the corpse will be added to your inventory.\nTouth luck bud!",
                button=EMI.button_options["ok"],
                always_on_top=True
            )
        else:
            EMI.advanced_information_message(
                parent_window=BASE_WINDOW,
                title="Your corpsy response",
                message=f"You have chosen to {response_sentence[RESPONSE]} the corpse.",
                button=EMI.button_options["ok"],
                always_on_top=True
            )
        EMI.goodbye_message(parent_window=BASE_WINDOW)

    def test_window_position() -> None:
        """_summary_
        This is a function in charge of testing the window position
        """
        CWPI = CalculateWindowPosition(10, 10, 1, 1)
        test_input = {
            CWPI.top_left: (0, 0),
            CWPI.top_center: (4, 0),
            CWPI.top_right: (9, 0),
            CWPI.bottom_left: (0, 9),
            CWPI.bottom_center: (4, 9),
            CWPI.bottom_right: (9, 9),
            CWPI.left_center: (0, 4),
            CWPI.center: (4, 4),
            CWPI.right_center: (9, 4),
            "gobbledygook": (0, 0)
        }
        for key, value in test_input.items():
            print(f"Testing: CPI.re_router({key}):", end="")
            response = CWPI.re_router(key)
            if response == value:
                print("[OK]")
            else:
                print(f"[KO]: Got {response} but expected {value}")

    print("Testing the calculate window position class")
    test_window_position()
    print("Testing the message boxes")
    test_the_error_message_class()
