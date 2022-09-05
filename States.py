from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class encoder(StatesGroup):
    key = State()
    mess_or_answer = State()
    answer = State()
    mess = State()



