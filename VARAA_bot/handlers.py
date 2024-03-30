from http import HTTPStatus
from aiogram import Bot, types, F, Router
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods.send_animation import SendAnimation
from aiogram.methods import SendAnimation
from aiogram.types import URLInputFile



router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я Святополк! Готов поддержать твою гойду!")

@router.message(F.text == "Гойда")
async def message_handler(msg: Message, bot: Bot):
    await msg.answer("Гойда! Храбрый воин " + msg.from_user.full_name + " !!!")
    await msg.answer_video(video=URLInputFile(url="https://c.tenor.com/ND_8Z8BDk-wAAAAC/tenor.gif"))