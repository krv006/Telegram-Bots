from aiogram import Router
from aiogram.filters import CommandStart, IS_ADMIN
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from filters import IsAdmin

from simple_bot.config import ADMIN_LIST

admin_router = Router()


@admin_router.message(CommandStart(), IsAdmin(ADMIN_LIST))
async def is_admin(message: Message):
    btn = [
        [KeyboardButton(text='user_list')],
        [KeyboardButton(text='admin_list')],

    ]
    rkb = ReplyKeyboardBuilder(btn)
    rkb.adjust(2)
    return message.answer("Siz adminsiz.", reply_markup=rkb.as_markup(resize_keyboard=True))
