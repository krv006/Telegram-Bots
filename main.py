# import asyncio
# import logging
# import sys
# import os
#
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher, html, F
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.types import Message
#
# from buttons import generate_btn
#
# load_dotenv()
# TOKEN = os.getenv("BOT_TOKEN")
#
# dp = Dispatcher()
#
#
# class StateMenus(StatesGroup):
#     main = State()
#     one = State()
#     two = State()
#     three = State()
#     four = State()
#     five = State()
#     one_one = State()
#     one_two = State()
#     one_three = State()
#     one_four = State()
#
#
# @dp.message(StateMenus.one, F.text == "back")
# @dp.message(StateMenus.two, F.text == "back")
# @dp.message(StateMenus.three, F.text == "back")
# @dp.message(StateMenus.four, F.text == "back")
# @dp.message(StateMenus.five, F.text == "back")
# @dp.message(CommandStart())
# async def command_start_handler(message: Message, state: FSMContext) -> None:
#     btn_names = ("1", "2", "3", "4", "5")
#     design = (2, 2, 1)
#     await state.set_state(StateMenus.main)
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!",
#                          reply_markup=generate_btn(btn_names, design))
#
#
# @dp.message(StateMenus.one_one, F.text == "back")
# @dp.message(StateMenus.one_two, F.text == "back")
# @dp.message(StateMenus.one_three, F.text == "back")
# @dp.message(StateMenus.one_four, F.text == "back")
# @dp.message(StateMenus.main, F.text.in_(["1", "2", "3", "4", "5"]))
# async def main_handler(message: Message, state: FSMContext):
#     _map = {
#         "1": [("1.1", "1.2", "1.3", "1.4", "back"), (2, 2, 1), StateMenus.one],
#         "2": [("2.1", "2.2", "2.3", "2.4", "back"), (2, 2, 1), StateMenus.two],
#         "3": [("3.1", "3.2", "3.3", "3.4", "back"), (2, 2, 1), StateMenus.three],
#         "4": [("4.1", "4.2", "4.3", "4.4", "back"), (2, 2, 1), StateMenus.four],
#         "5": [("5.1", "5.2", "5.3", "5.4", "back"), (2, 2, 1), StateMenus.five],
#         StateMenus.one_one: "1",
#         StateMenus.one_two: "1",
#         StateMenus.one_three: "1",
#         StateMenus.one_four: "1"
#     }
#     value = _map.get(message.text) if _map.get(message.text) else _map[_map[await state.get_state()]]
#     await state.set_state(value.pop())
#     await message.answer("one menu", reply_markup=generate_btn(*value))
#
#
# @dp.message(StateMenus.one, F.text.in_(["1.1", "1.2", "1.3", "1.4"]))
# async def one_handler(message: Message, state: FSMContext):
#     _map = {
#         "1.1": [("1.1.1", "1.1.2", "1.1.3", "1.1.4", "back"), (2, 2, 1), StateMenus.one_one],
#         "1.2": [("1.2.1", "1.2.2", "1.2.3", "1.2.4", "back"), (2, 2, 1), StateMenus.one_two],
#         "1.3": [("1.3.1", "1.3.2", "1.3.3", "1.3.4", "back"), (2, 2, 1), StateMenus.one_three],
#         "1.4": [("1.4.1", "1.4.2", "1.4.3", "1.4.4", "back"), (2, 2, 1), StateMenus.one_four],
#     }
#     value = _map[message.text]
#     await state.set_state(value.pop())
#     await message.answer("one one menu", reply_markup=generate_btn(*value))
#
#
# async def main() -> None:
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
#
# """
# Keyboard Markup : [Inline , Reply]
# Finite State machine
# Force reply
# Dispatcher[handler function]
# Router
# Filtering
# Pydantic
# Middlewares
# Callbacks data
# Sending Files
# Payment
# telegram search
# Webhook
# tg account
# Sqlalchemy ORM
# Docker
# Server
#
# """


# import telebot
# import requests
# import json
# import urllib
#
# api = 'BOT TOKEN'
# bot = telebot.TeleBot(api)
#
#
# def cid(cid):
#     try:
#         cidlist = open('cid.txt', 'r')
#         if cid in cidlist:
#             cidlist.close()
#         else:
#             cidlist = open('cid.txt', 'a')
#             cidlist.write('\n{}'.format(cid))
#             cidlist.close()
#     except:
#         pass
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     try:
#         cid(str(message.chat.id))
#         text = '''
# Halo!! Selamat datang di bot kami. Silahkan kirimkan link untuk mulai mendownload.
# Join @BagusBotChannel untuk mendapat info terbaru dari bot bot kami.
#
# Dukung kami di https://saweria.co/gbagus
# 		'''
#         bot.send_message(message.chat.id, text)
#     except:
#         pass
#
#
# @bot.message_handler(content_types=["text"])
# def download(message):
#     try:
#         chat_id = message.chat.id
#         link = requests.get(
#             'https://godownloader.com/api/tiktok-no-watermark-free?url={}&key=godownloader.com'.format(message.text))
#         link = link.json()
#         desc = "{}\n\nDownloaded with @TTDownloaderNoWMbot".format(link["desc"].strip("@godownloader"))
#         bot.send_video(chat_id, link["video_no_watermark"], caption=desc)
#     except:
#         pass
#
#
# while True:
#     try:
#         print("bot running")
#         bot.polling()
#     except:
#         print('bot restart')
#         time.sleep(5)
#
#
# # todo https://github.com/gbagush/TikTokDownloaderBot/blob/main/main.py git hub
