from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from States import encoder
from keyboards import interface, interface_m, en, de
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import token_list
import cesar_ciphr
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=token_list.API_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help'], state="*")
async def send_welcome(message: types.Message):
    """
    Сообщение приветствия для команд `/start` и `/help`
    """
    await message.answer("Это шифратор, он может шифровать и расшифровывать сообщения по ключу.")
    await encoder.key.set()
    await message.answer("Введите или сгенерируйте ключ (целое положительное число):", reply_markup=interface)


@dp.message_handler(state=encoder.key)
async def set_key(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["key"] = message.text
    await message.answer("Вы хотите зашифровать или расшифровать?", reply_markup=interface_m)
    await encoder.mess_or_answer.set()


@dp.message_handler(state=encoder.mess_or_answer, commands=[en.text[1:], de.text[1:]])
async def mess_or_answer(message: types.Message, state: FSMContext):
    if message.text == en.text:
        await message.reply("Введите сообщение:")
        await encoder.mess.set()

    if message.text == de.text:
        await message.reply("Введите шифр:")
        await encoder.answer.set()


@dp.message_handler(state=encoder.mess)
async def set_mess(message: types.Message, state: FSMContext):
    await message.answer("Шифр:")
    async with state.proxy() as data:
        await message.reply(cesar_ciphr.encoder(int(data["key"]), message.text))
    await state.finish()


@dp.message_handler(state=encoder.answer)
async def set_mess(message: types.Message, state: FSMContext):
    await message.answer("Сообщение:")
    async with state.proxy() as data:
        await message.reply(cesar_ciphr.decoder(int(data["key"]), message.text))
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
