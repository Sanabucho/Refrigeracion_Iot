#from django_tgbot.decorators import processor
#from django_tgbot.state_manager import message_types, update_types, state_types
#from django_tgbot.types.update import Update
#from .bot import state_manager
#from .models import TelegramState
#from .bot import TelegramBot

#@processor(state_manager, from_states=state_types.Reset, message_types=[message_types.Text])
#def hello_world(bot: TelegramBot, update: Update, state: TelegramState):
#    type = update.type()
#    if type == update_types.Message:
#        bot.sendMessage(update.get_chat().get_id(), 'xao noma')
#        print(update.get_chat().get_id())
#    else:
#        print(type)
from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot
from apiv1.models import DataTS


state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states=state_types.Reset, message_types=[message_types.Text])
def send_keyboards(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = str(update.get_message().get_text())
    if str(chat_id)!="-828088180":
        bot.sendMessage(
            chat_id,
            text='Elija alguna de las opciones disponibles',
            reply_markup=InlineKeyboardMarkup.a(
                inline_keyboard=[
                    [
                        InlineKeyboardButton.a('Grafico', url='https://21b9-190-46-253-155.sa.ngrok.io/api'),
                        InlineKeyboardButton.a('Reporte', url='https://21b9-190-46-253-155.sa.ngrok.io/api/data/report/')],
                        [InlineKeyboardButton.a('Temperatura Actual', callback_data=str(DataTS.objects.latest('timestamp').value))
                    ]
                ]
            )
        )


@processor(state_manager, from_states=state_types.All, update_types=[update_types.CallbackQuery])
def handle_callback_query(bot: TelegramBot, update, state):
    callback_data = update.get_callback_query().get_data()
    chat_id = update.get_chat().get_id()
    bot.sendMessage(
        chat_id,
        callback_data+'°C'
    )
