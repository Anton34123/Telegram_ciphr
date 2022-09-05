from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import random

k = KeyboardButton(str(random.randint(0, 5000)))


en = KeyboardButton("/Зашифровать")
de = KeyboardButton("/Расшифровать")

interface = ReplyKeyboardMarkup()
interface.add(k)

interface_m = ReplyKeyboardMarkup()
interface_m.add(en).add(de)
