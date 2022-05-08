from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Salom'), KeyboardButton(text='Telefon Contact',request_contact=True)],
        [KeyboardButton(text='Apple'),KeyboardButton(text='Samsung ')],
        [KeyboardButton(text='Acer'),KeyboardButton(text='Lenova')],
        [KeyboardButton(text='Lokatsiya', request_location=True),KeyboardButton(text='Xayr')],
        [KeyboardButton(text='Savatcha')]
    ],
    resize_keyboard=True,
)


Samsung = ReplyKeyboardMarkup(resize_keyboard=True)
Samsung.row('Samsung S21 ultra','Samsung Note 10','SamsungSM-A 51')
Samsung.row('Samsung 20s ultra','Samsung Note 9','SamsungSM-A 41')
Samsung.row('Samsung 10s plus','Samsung Note 8','SamsungSM-A 31')
Samsung.row('Samsung 10s','Samsung Note 7','SamsungSM-A 21')
Samsung.row('Bosh menu', '🔙 Ortga'),

Apple = ReplyKeyboardMarkup(resize_keyboard=True)
Apple.row('iphone 13 Pro Max', 'iphone 12 Pro Max','iPhone 11 Pro Max')
Apple.row('iphone 13 Pro ', 'iphone 12 Pro','iPhone 11 Pro')
Apple.row('iphone 13 Min ', 'iphone 12 Min','iPhone 11 Min')
Apple.row('Bosh menu','🔙 Ortga')

miqdor= ReplyKeyboardMarkup(resize_keyboard=True)
miqdor.row('Buyurtma 1','Buyurtma 2','Buyurtma 3')
miqdor.row('Buyurtma 10+')
miqdor.row('Bosh menu','🔙 Ortga')

Acer = ReplyKeyboardMarkup(resize_keyboard=True)
Acer.row('Acer CORE i11', 'Acer CORE i5', )
Acer.row('Acer CORE i9', 'Acer CORE i3')
Acer.row('Acer CORE i7', 'Acer CORE intel')
Acer.row('Bosh menu','🔙 Ortga')


Lenova = ReplyKeyboardMarkup(resize_keyboard=True)
Lenova.row('Lenova CORE i11', 'Lenova CORE i5')
Lenova.row('Lenova CORE i9', 'Lenova CORE i3')
Lenova.row('Lenova CORE i7', 'Lenova CORE intel')
Lenova.row('Bosh menu','🔙 Ortga')