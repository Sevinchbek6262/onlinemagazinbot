import logging
from aiogram import Bot,Dispatcher,executor,types
from main1 import TOKEN
from buttons import menu, Apple, Samsung,miqdor,Lenova,Acer
logging.basicConfig(level=logging.INFO)

bot= Bot( TOKEN)
dp =Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def do_start(message: types.message):
    username= message.from_user.username
    await message.answer(f'<b>Assalomu alekum\n@{username}</b>', parse_mode='html', reply_markup=menu)

@dp.message_handler(text='Savatcha')
async def get_savatcha(message: types.message):
    await message.answer('savatcha bosh')


@dp.message_handler(content_types=['Telefon Contact'])
async def get_cantact(message: types.message):
    await  message.answer(message.contact['phone_number'])
    await message.answer('Kantakt qabul qlindi:')




@dp.message_handler(text='Salom')
async def do_salom(message: types.message):
    await message.answer('<b>Voalokum Assalom</b>', parse_mode='html')


@dp.message_handler(text='Xayr')
async def do_salom(message: types.message):
    await message.answer('Asosiy sahifa')
 
 
@dp.message_handler(text='Apple')
async def do_phone(message: types.message):
    await message.answer('Bizning telefonlar',reply_markup=Apple)

@dp.message_handler(text='iphone 13 Pro Max')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/wc9156H',caption='''iPhone 13 Pro Max

Release Date: Released 2021, September 24
Dimension: 240g, 7.7mm thickness
OS: iOS 15, up to iOS 15.4.1
Storage: iOS 15, up to iOS 15.4.1''',reply_markup=miqdor)


@dp.message_handler(text='iphone 13 Pro')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/qk7fhX5',caption='''iPhone 13 Pro

Release Date: Released 2021, September 24
Dimension: 204g, 7.7mm thickness
OS: iOS 15, up to iOS 15.4.1
Storage: iOS 15, up to iOS 15.4.1''',reply_markup=miqdor)

@dp.message_handler(text='iphone 13 Min')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/ZSSvBts',caption='''iPhone 13 Min

Release Date: Released 2021, September 24
Dimension: 141g, 7.7mm thickness
OS: iOS 15, up to iOS 15.4.1
Storage: iOS 15, up to iOS 15.4.1''',reply_markup=miqdor)


@dp.message_handler(text='iphone 12 Pro Max')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/4gg3rZp',caption='''iPhone 12 Pro Max

Release Date: Released 2020, November 13
Dimension: 228g, 7.4mm thickness
OS: iOS 14.1, up to iOS 15.4.1
Storage: iOS 14.1, up to iOS 15.4.1''',reply_markup=miqdor)
 
@dp.message_handler(text='iphone 12 Pro')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/Msq5dZ1',caption='''iPhone 12 Pro

Release Date: Released 2020, October 23
Dimension: 189g, 7.4mm thickness
OS: iOS 14.1, up to iOS 15.4.1
Storage: iOS 14.1, up to iOS 15.4.1''',reply_markup=miqdor)
    
@dp.message_handler(text='iphone 12 Min')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/n6XGWSL',caption='''iPhone 12 Min

Release Date: Released 2020, October 23
Dimension: 164g, 7.4mm thickness
OS: iOS 14.1, up to iOS 15.4.1
Storage: iOS 14.1, up to iOS 15.4.1''',reply_markup=miqdor)
 
@dp.message_handler(text='iPhone 11 Pro Max')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/tQLM39F',caption='''iPhone 11 Pro Max

Release Date: Released 2019, September 20
Dimension: 226g, 8.1mm thickness
OS: iOS 13, up to iOS 15.4.1
Storage: iOS 13, up to iOS 15.4.1''',reply_markup=miqdor)
 
@dp.message_handler(text='iPhone 11 Pro')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/tQLM39F',caption='''iPhone 11 Pro

Release Date: Released 2019, September 20
Dimension: 188g, 8.1mm thickness
OS: iOS 13, up to iOS 15.4.1
Storage: iOS 13, up to iOS 15.4.1''',reply_markup=miqdor)
 
  
@dp.message_handler(text='iPhone 11 Min')
async def do_phone(message: types.message):
    await message.answer_photo(photo='https://ibb.co/yhLgHTt',caption='''iPhone 11 Min

Release Date: Released 2019, September 20
Dimension: 194g, 8.3mm thickness
OS: iOS 13, up to iOS 15.4.1
Storage: iOS 13, up to iOS 15.4.1''',reply_markup=miqdor)






@dp.message_handler(text='Samsung')
async def do_samsung(message: types.message):
    await message.answer('Bizning telefonlar', reply_markup=Samsung)


@dp.message_handler(text='Samsung S21 ultra')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/ZGdMXwB',caption='''Galaxy S21 Ultra 5G

Release Date: Released 2021, January 29
Dimension: 227g (Sub6), 229g (mmWave), 8.9mm thickness
OS: Android 11, One UI 3.1
Storage: Android 11, One UI 3.1''',reply_markup=miqdor)


@dp.message_handler(text='Samsung 20s ultra')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/PWQwHXC',caption='''Galaxy S20 FE 2022

Release Date: Released 2022, April 01
Dimension: 190g, 8.4mm thickness
OS: Android 12, One UI 4.1
Storage: Android 12, One UI 4.1''',reply_markup=miqdor)


@dp.message_handler(text='Samsung 10s plus')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/wN4zSsG',caption='''Samsung 10s puls

Release Date: Released 2022, March 24
Dimension: 189g, 8.1mm thickness
OS: Android 12, One UI 4.1
Storage: Android 12, One UI 4.1''',reply_markup=miqdor)


@dp.message_handler(text='Samsung 10s')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/6NDJcPC',caption='''Samsung 10s

Release Date: Released 2022, March 24
Dimension: 189g, 8.1mm thickness
OS: Android 12, One UI 4.1
Storage: Android 12, One UI 4.1''',reply_markup=miqdor)


@dp.message_handler(text='Samsung Note 10')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/cwsqx8R',caption='''Samsung Note 10

Release Date: Released 2020, August 21
Dimension: 208g, 8.1mm thickness
OS: Android 10, up to Android 11, One UI 3.0
Storage: Android 10, up to Android 11, One UI 3.0''',reply_markup=miqdor)


@dp.message_handler(text='Samsung Note 9')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/25BFyDL',caption='''Samsung Note 9

Release Date: Released 2020, August 21
Dimension: 208g, 8.1mm thickness
OS: Android 10, up to Android 11, One UI 3.0
Storage: Android 10, up to Android 11, One UI 3.0''',reply_markup=miqdor)


@dp.message_handler(text='Samsung Note 8')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/CP7vzbP',caption='''Samsung Note 8

Release Date: Released 2020, July 16
Dimension: 168g, 7.8mm thickness
OS: Android 9.0, up to Android 10, One UI 2.1
Storage: Android 9.0, up to Android 10, One UI 2.1''',reply_markup=miqdor)


@dp.message_handler(text='Samsung Note 7')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/9VckqpC',caption='''Samsung Note 7

Release Date: Released 2020, July 16
Dimension: 168g, 7.8mm thickness
OS: Android 9.0, up to Android 10, One UI 2.1
Storage: Android 9.0, up to Android 10, One UI 2.1''',reply_markup=miqdor)


@dp.message_handler(text='SamsungSM-A 51')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/yqWT02X',caption='''SamsungSM-A 51

Release Date: Released 2020, August 14
Dimension: 188.8g, 8.6mm thickness
OS: Android 10, One UI 2
Storage: Android 10, One UI 2''',reply_markup=miqdor)


@dp.message_handler(text='SamsungSM-A 41')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/1mN5DG8',caption='''SamsungSM-A 41

Release Date: Released 2020, October 16
Dimension: 191g, 8.9mm thickness
OS: Android 10, up to Android 11, One UI 3.1
Storage: Android 10, up to Android 11, One UI 3.1''',reply_markup=miqdor)


@dp.message_handler(text='SamsungSM-A 31')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/4SKbXCH',caption='''SamsungSM-A 31

Release Date: Released 2020, October 17
Dimension: 191g, 8.9mm thickness
OS: Android 10, One UI 2.0
Storage: Android 10, One UI 2.0''',reply_markup=miqdor)


@dp.message_handler(text='SamsungSM-A 21')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/FYsLBvb',caption='''SamsungSM-A 21

Release Date: Released 2020, October 16
Dimension: 191g, 8.9mm thickness
OS: Android 10, up to Android 11, One UI 3.1
Storage: Android 10, up to Android 11, One UI 3.1''',reply_markup=miqdor)



@dp.message_handler(text='Acer')
async def do_samsung(message: types.message):
    await message.answer('Bizning notebooklar', reply_markup=Acer)

@dp.message_handler(text='Acer CORE i11')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/nc7p6wJ',caption='''Processor: Intel® Celeron® N4020 Processor (2 Cores / 2 Threads, 1.10 GHz, up to 2.80 GHz, 4 MB Cache)

Operating System: Chrome OS
Memory: 4 GB Soldered LPDDR4 2400MHz
First Hard Drive: 64 GB eMMC 5.1
Warranty: 1 Year Premium Care''',reply_markup=miqdor)

@dp.message_handler(text='Acer CORE i9')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/VvZMw0c',caption='''Processor: 11th Generation Intel® Core™ i5-1135G7 Processor (4 Cores / 8 Threads, 2.40 GHz, up to 4.20 GHz with Turbo Boost, 8 MB Cache)

Operating System: Windows 10 Pro 64
Memory: 8 GB SDRAM SO-DIMM DDR4 3200MHz
First Hard Drive: 512 GB M.2 2242 SSD
Warranty: 1 Year Courier or Carry-in''',reply_markup=miqdor)

@dp.message_handler(text='Acer CORE i7')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/4ZSR5tj',caption='''Processor: 11th Generation Intel® Core™ i7-1165G7 Processor (4 Cores / 8 Threads, 2.80 GHz, up to 4.70 GHz with Turbo Boost, 12 MB Cache)

Operating System: Windows 11 Pro 64
Memory: 16 GB LPDDR4X-4266MHz (Soldered)
First Hard Drive: 512 GB SSD M.2 2280 PCIe Gen4 TLC
Warranty: Three Year Onsite''',reply_markup=miqdor)

@dp.message_handler(text='Acer CORE i5')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/BTWf7BY',caption='''Processor: 11th Generation Intel® Core™ i5-1130G7 Processor (4 Cores / 8 Threads, 1.80 GHz, up to 4.00 GHz with Turbo Boost, 8 MB Cache)

Operating System: Windows 10 Home 64
Memory: 16 GB Soldered LPDDR4x 4266MHz
First Hard Drive: 512 GB M.2 2242 SSD
Warranty: 3 Year Premier''',reply_markup=miqdor)

@dp.message_handler(text='Acer CORE i3')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/tBr3yQ5',caption='''Processor: 11th Generation Intel® Core™ i7-11800H Processor (8 Cores / 16 Threads, 2.30 GHz, up to 4.60 GHz with Turbo Boost, 24 MB Cache)

Operating System: Windows 10 Pro 64
Memory: 16 GB SO-DIMM DDR4 3200MHz
First Hard Drive: 512 GB M.2 2280 SSD
Warranty: 3 Year Premier''',reply_markup=miqdor)

@dp.message_handler(text='Acer CORE intel')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/hXzskc3',caption='''Color: Black

Battery Life: Up to 12 months
Weight: 60 g (0.13 lbs)
Special Design Features: Ambidextrous design
Mouse Sensor: Optical sensor''',reply_markup=miqdor)



@dp.message_handler(text='Lenova')
async def do_samsung(message: types.message):
    await message.answer('Bizning notebooklar', reply_markup=Lenova)

@dp.message_handler(text='Lenova CORE i11')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/3h1bnBW',caption='''Windows 10 Home, 15.6" inch FHD (1920x1080) IPS 400nits Glossy Touch Display

Intel 11th Generation Core i5-1135G7, Intel Iris Xe Graphics
8GB DDR4 3200MHz (soldered), 256GB Solid State Drive
1x USB 3.2 Type A, 1x USB Type C Charging Ports, 2x Thunderbolt Ports (Total) and 1x Headphone/microphone combo jack
Built-in fingerprint reader, Wireless-Ax Bluetooth 5.0, 65 watts 4 cell Lithium-polymer, Weight 4.18 pounds''',reply_markup=miqdor)

@dp.message_handler(text='Lenova CORE i9')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/V2vfyhc',caption='''Дисплей: 15.6" TN 1366x768

Процессор: Intel Celeron N4120 1.10 ГГц
Видеокарта: Intel UHD Graphics
Оперативная память: 4 Гб DDR4
Накопитель: SSD 128 Гб
Операционная система: Windows 10 Home
Подробнее''',reply_markup=miqdor)

@dp.message_handler(text='Lenova CORE i7')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/n1vq4vg',caption='''Дисплей: 15.6" TN 1366x768

Процессор: Intel Celeron N4120 1.10 ГГц
Видеокарта: Intel UHD Graphics
Оперативная память: 4 Гб DDR4
Накопитель: SSD 128 Гб
Операционная система: Windows 10 Home
Подробнее''',reply_markup=miqdor)

@dp.message_handler(text='Lenova CORE i5')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/NNqFrXL',caption='''Дисплей: 15.6" TN 1366x768

Процессор: Intel Celeron N4120 1.10 ГГц
Видеокарта: Intel UHD Graphics
Оперативная память: 4 Гб DDR4
Накопитель: SSD 128 Гб
Операционная система: Windows 10 Home
Подробнее''',reply_markup=miqdor)

@dp.message_handler(text='Lenova CORE i3')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/HgmW1bB',caption='''Дисплей: 15.6" TN 1366x768

Процессор: Intel Celeron N4120 1.10 ГГц
Видеокарта: Intel UHD Graphics
Оперативная память: 4 Гб DDR4
Накопитель: SSD 128 Гб
Операционная система: Windows 10 Home
Подробнее''',reply_markup=miqdor)

@dp.message_handler(text='Lenova CORE intel')
async def do_samsung(message: types.message):
    await message.answer_photo(photo='https://ibb.co/WyPM4C0',caption='''Дисплей: 15.6" TN 1366x768

Процессор: Intel Celeron N4120 1.10 ГГц
Видеокарта: Intel UHD Graphics
Оперативная память: 4 Гб DDR4
Накопитель: SSD 128 Гб
Операционная система: Windows 10 Home
Подробнее''',reply_markup=miqdor)




@dp.message_handler(text='Bosh menu')
async def go_menu(message: types.message):
    await message.answer('Siz asosiy saxifadasiz',reply_markup=menu)

@dp.message_handler(text='🔙 Ortga')
async def go_menu(message: types.message):
    await message.answer('Siz asosiy saxifadasiz',reply_markup=menu)

@dp.message_handler(text='Buyurtma 1')
async def go_menu(message: types.message):
    await message.answer('Sizngi buyurtmangiz qabul qilindi\nAloq uchun\n@Shomurotov_99',reply_markup=menu)

@dp.message_handler(text='Buyurtma 2')
async def go_menu(message: types.message):
    await message.answer('Sizngi buyurtmangiz qabul qilindi\nAloq uchun\n@Shomurotov_99',reply_markup=menu)

@dp.message_handler(text='Buyurtma 3')
async def go_menu(message: types.message):
    await message.answer('Sizngi buyurtmangiz qabul qilindi\nAloq uchun\n@Shomurotov_99',reply_markup=menu)

@dp.message_handler(text='Buyurtma 10+')
async def go_menu(message: types.message):
    await message.answer('Sizngi buyurtma (10+)\nMiqdorini kiriting (?)',reply_markup=menu)



@dp.message_handler()
async def miqdor1(message: types.message):
    try:
        if int(message.text) > 9:
            await message.answer(f'Siz {message.text} ta buyurtma berdiz!\nAloq uchun\n@Shomurotov_99')
        else:
            await message.answer("Miqdor noto'g'ri kiritildi\nBrend tanlang", reply_markup=menu)
    except Exception as e:
        await message.answer('Xotolik yuz berdi ')


@dp.message_handler(content_types='sticker')
async def get_stecker(message: types.message):
    sticker_id = message.sticker.file_id
    await message.answer_sticker(sticker_id)



if  __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

