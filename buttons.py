from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def generate_btn(btn_names, design):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text=i) for i in btn_names])
    rkb.adjust(*design)
    return rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)


btn_names = ["Tugma 1", "Tugma 2", "Tugma 3", "Tugma 4"]
design = [2, 2]

keyboard = generate_btn(btn_names, design)
