# Импортируем библиотеки
import discord
from discord.ext import commands
from discord import app_commands
import psutil
import asyncio
import re
from datetime import datetime

# Задаем интенты
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


# Смена статусов
@bot.event
async def on_ready():
    bot.remove_command('help')
    f = open('log.txt', 'a')
    f.write(f'\n\n----------\n БОТ ЗАПУЩЕН ({datetime.now()})\n')
    f.close()
    print(f'Бот запущен и готов к работе!')
    while True:
        await bot.change_presence(activity=discord.Game(name="пасьянс"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на лютый движ в холле"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="гослото суперприз 1.000.000.000"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Сталин в Столеее"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на Отчеты Турникета"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="косынку"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="60 минут"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Пусть Говорят на Первом"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="змейку"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="супердискотека 70-х"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="шоу Андрея Малахова"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="симулятор поломойки"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="розыгрыш мультиварки леомакс"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на бабка стойка вахта крики визги"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="обсуждение всех окружающих"))
        await asyncio.sleep(10)



# Эмбед .неизвестная команда
error_embed = discord.Embed(
    title="🛑 Ошибка",
    description=f"""Ой...
    > Введенной команды не существует. Все доступные команды можно посмотреть, введя команду `.хелп`.""",
    color=0x2d2b31
)

# Эмбед ошибки
error_embed = discord.Embed(
    title="Ой... Что-то сломалось...",
    description=f"""Ой...
    > Введенной команды не существует. Все доступные команды можно посмотреть, введя команду `.хелп`.""",
    color=0x2d2b31
)


# Неизвестная команда
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=error_embed)
        f = open('log.txt', 'a')
        f.write(f'[ЛОГ] Пользователь {ctx.author} попыталcя вызвать неизвестную команду ""  ({datetime.now()})\n')
        f.close()
        print(f'[ЛОГ] Пользователь {ctx.author} попыталcя вызвать неизвестную команду "" ({datetime.now()})')


# Эмбед .инфо
info_embed = discord.Embed(
    title="ℹ Информация о боте",
    description="""Бот-вахтерша, который почти ничего не умеет. Был сделан за пару вечеров говнокодинга и листания стаковерфлох <:stack:1113012139985223740>.""",
    color=0x2d2b31
)

# Эмбед .хелп
help_embed = discord.Embed(
    title="📚 Все команды бота",
    description="""
    > `.инфо` — инфо о боте
    > `.хелп` — помощь с командами
    -----
    > `.получитьпропуск` — получить пропуск
    -----
    > `.статус`  — нагрузка аппарата жизнеобеспечения людочки
    > `.обнова` — узнать чего нового добавили в бота""",
    color=0x2d2b31
)

# Эмбед .статус
status_embed = discord.Embed(
    title="🌡 Состояние аппарата жизнеобеспечения",
    description=f"""
        > <:procesor:1113129126895833258> Процессор: *`использовано {psutil.cpu_percent()}%`*
        > <:operativka:1113129125419417681> Оперативная память: *`использовано {psutil.virtual_memory().percent}%`*
        > <:pingg:1113129123234197615> Пинг: *`{bot.latency}`*
        > <:aptaim:1113129121598423110> Аптайм: *`-1`*
        > <:databaze:1113129118633041943> База Данных: *`MySQL_ludabot`*""",
    color=0x2d2b31
)

# Эмбед .обнова
update_embed = discord.Embed(
    title="📋 Чейнжлог",
    description="""**Чего нового в новой вкерсии 3.2 (БЕТА):**

        > - Ботиха не перенесена на слеш-команды,
        > - Добавлен вывод команды об ошибке,
        > - Добавлено логирование в .txt,
        > - Убраны команды `.вход`, `.выход`, `.свалить`, `.словарь`, `.репорт`,
        > - Добавлена команда `.получитьпропуск` и автозасирание админ-чата,
        > - Добавлено приветствие новобранцев в <#1032324906488176721> и отсылка отчета в <#956198114186919937>,
        > - Добавлено дохрена статусов.
        """,
    color=0x2d2b31, )

# Эмбед .получитьпропуск
getpass_embed = discord.Embed(
    title="🛑 Ошибка!",
    description="""**Кажется, вертель на пипиське был занят и жарил шаурму, вместо того чтобы писать говнокод в своем висуалсекстудио.
          
            > Админ чат уже засран пингами, а значит они скоро придут.
        """,
    color=0x2d2b31, )

# Эмбед позвать админа
passhorn_embed = discord.Embed(
    title="🔔 Тревога!",
    description=f"""**<@1096973456786063370>, БОЕВАЯ ТРЕВОГА**
            
            > Какому-то идиоту срочно требуется помощь:
            > Выдать пропуск и проверить вступил ли он на сервер спонсора!
            > Также, не забудьте нахамить — у нас строгое заведение!11!1111!!!11!!!
        """,
    color=0x2d2b31, )

#Эмбед обнова
newversion_embed = discord.Embed(
    title="🎉 Я обновилясъ!",
    description=f"""Ого, вертель на пипиське отложил жарку шаурмы, и пошел говнокодить в своем висуалсекстудио. Давайте посмотрим че он там надристал:
        
        > - Ботиха не перенесена на слеш-команды (не потому что я ленивый);
        > - Всякие идиоты больше не смогут засирать мой архив, и теперь если я не знаю че вы от меня хотите я буду посылать вас на большой хуй (можно с Вазелином, но это платно уже);
        > - Все ваши деяния записываются в `log.txt`, и автоматически отправляются в ФСБ;
        > - Разучилась выполнять команды `.вход`, `.выход`, `.свалить`, `.словарь`, `.репорт` ибо я вам не турникет;
        > - Я научилась поднимать лютую шумиху в кабинете отдела ~~*с*~~асу, ведь мне довериил ключи. Кстати, команда `.получитьпропуск` это и делает;
        > - Добавлено приветствие новобранцев в <#1032324906488176721> и отсылка отчета в кабинет отдела ~~*с*~~асу (<#956198114186919937>),
        > - Расширен кругозор, и теперь я не только участвую в розыгрыше мультиварки леомакс но еще и страдаю 15-ю хернями
        """,
    color=0x2d2b31, )

# Кнопка позвать админа
class calladmin_btns(discord.ui.View):  # класс описывает набор кнопок
    @discord.ui.button(style=discord.ButtonStyle.blurple, label='🔔 Позвать админов')
    async def click_me_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        for i in range(10):
            callchannel = bot.get_channel(956198114186919937)
            await callchannel.send(embed=passhorn_embed)
            asyncio.sleep(5)


# Команда .инфо
@bot.command()
async def инфо(ctx):
    await ctx.send(embed=info_embed)
    f = open('log.txt', 'a')
    f.write(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".инфо" ({datetime.now()})\n')
    f.close()
    print(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".инфо" ({datetime.now()})')


# Команда .хелп
@bot.command()
async def хелп(ctx):
    await ctx.send(embed=help_embed)
    f = open('log.txt', 'a')
    f.write(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".хелп" ({datetime.now()})\n')
    f.close()
    print(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".хелп" ({datetime.now()})')


# Команда .статус
@bot.command()
async def статус(ctx):
    await ctx.send(embed=status_embed)
    f = open('log.txt', 'a')
    f.write(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".статус" ({datetime.now()})\n')
    f.close()
    print(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".статус" ({datetime.now()})')


# Команда .обнова
@bot.command()
async def обнова(ctx):
    await ctx.send(embed=update_embed)
    f = open('log.txt', 'a')
    f.write(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".обнова" ({datetime.now()})\n')
    f.close()
    print(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".обнова" ({datetime.now()})')

# Команда .получитьпропуск
@bot.command()
async def получитьпропуск(ctx):
    await ctx.send(embed=getpass_embed)
    f = open('log.txt', 'a')
    f.write(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".получитьпропуск" ({datetime.now()})\n')
    f.close()
    print(f'[ЛОГ] Пользователь {ctx.author} вызвал команду ".получитьпропуск" ({datetime.now()})')
    for i in range(50):
            callchannel = bot.get_channel(956198114186919937)
            await callchannel.send(embed=passhorn_embed)
            asyncio.sleep(5)
    f = open('log.txt', 'a')
    f.write(f'  ╚ Админ-чат засран пинками ({datetime.now()})\n')
    f.close()
    print(f'  ╚ Админ-чат засран пинками ({datetime.now()})\n')

'''
# Команда .объява
@bot.command()
async def объява(ctx):
    newschannel = bot.get_channel(1002503810171797535)
    await newschannel.send("@everyone")
    await newschannel.send(embed=newversion_embed)
'''

bot.run('MTA5Nzg5Nzg0MzM4MzA4NzIyNQ.GVUrxF.Iy6mhfq8jOWDxcdBtU-32fwZehMu6YZg6XD5pw')