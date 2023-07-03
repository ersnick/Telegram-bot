from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


def start_inline_keyboard() -> InlineKeyboardMarkup:
    create_statement_btn = InlineKeyboardButton('Подать заявку на добавление', callback_data='create_statement')
    help_btn = InlineKeyboardButton('Помощь', callback_data='help')
    return InlineKeyboardMarkup(row_width=2).add(create_statement_btn, help_btn)


async def start_message(message: Message):
    await message.answer(f'Привет, я бот института информационных технологий. Я помогу тебе узнать свое расписание и '
                         f'буду сообщать тебе о главных мероприятиях института. Нажми "Подать заявку на добавление" и'
                         f' заполни форму.', reply_markup=start_inline_keyboard())


def create_statement_inline_keyboard() -> InlineKeyboardMarkup:
    create_statement_btn = InlineKeyboardButton('Назад', callback_data='cancel')
    help_btn = InlineKeyboardButton('Отправить заявку', callback_data='send_statement')
    return InlineKeyboardMarkup(row_width=2).add(create_statement_btn, help_btn)


def help_inline_keyboard() -> InlineKeyboardMarkup:
    create_statement_btn = InlineKeyboardButton('Подать заявку на добавление', callback_data='create_statement')
    return InlineKeyboardMarkup(row_width=2).add(create_statement_btn)


async def help_message(message: Message):
    await message.answer(f'Чем могу помочь?', reply_markup=help_inline_keyboard())


async def create_statement(message: Message):
    await message.answer('Пример заявки...', reply=True)


async def callback_query_statement(call: CallbackQuery):
    await call.message.edit_text(text='Пример заявки на добавление...',
                                 reply_markup=create_statement_inline_keyboard())


async def callback_query_help(call: CallbackQuery):
    await help_message(call.message)


async def callback_query_send_statement(call: CallbackQuery):
    await call.message.edit_text(text='Заявка успешно отправлена!')
