# Телеграм бот для автопереводов и распознавания текста с скриншотов и голосовых сообщений

Чат бот отзывается на кодовое слово `бот`(можно сменить командой /name) `бот расскажи про биткоин`

Кодовое слово `гугл`(нельзя изменить) позволит получить более актуальную информацию, бот будет гуглить перед ответом `гугл, сколько людей на земле осталось`

Кодовое слово `бинг`(нельзя изменить) позволит получить более актуальную информацию, бот будет дооолго гуглить перед ответом `бинг курс биткоина`

В привате можно не писать кодовые слова для обращения к боту

Если он забился в угол и не хочет отвечать то возможно надо почистить ему память командой `бот забудь`

Кодовое слово `нарисуй` и дальше описание даст картинки сгенерированные по описанию. В чате надо добавлять к этому обращение `бот нарисуй на заборе неприличное слово`

В чате бот будет автоматически переводить иностранные тексты на русский и распознавать голосовые сообщения, отключить это можно кодовым словом `бот замолчи`, включить обратно `бот вернись`

Если отправить текстовый файл в приват или с подписью `прочитай` то попытается озвучить его как книгу, ожидает .txt utf8 язык пытается определить автоматически (русский если не получилось)

Если отправить картинку или .pdf с подписью `прочитай` то вытащит текст из них.

Если отправить ссылку в приват то попытается прочитать текст из неё и выдать краткое содержание.

Если отправить текстовый файл или пдф с подписью `что там` или `перескажи` то выдаст краткое содержание.

Команды и запросы можно делать голосовыми сообщениями, если отправить голосовое сообщение которое начинается на кодовое слово то бот отработает его как текстовую команду.


Доступные команды:
```
/help - Справка
/tts - Преобразует текст в речь и отправляет аудиосообщение, с указанием языка и скорости (/tts [ru|en|uk|...] [+|-50%] hello all)
/ttsmale - Переключает голос на мужской
/ttsfemale - Переключает голос на женский (по умолчанию)
/trans - Переводит текст на другой язык (/trans en привет как дела)
/image - (или img) рисует картинки по текстовому описанию
/images - (или imgs) показывает что было нарисовано ранее
/gallery - (или gal) показывает html галерею всех сгенерированных ранее изображений
/google - бот будет гуглить перед ответом
/name - меняет кодовое слово для обращения к боту (только русские и английские буквы и цифры после букв, не больше 10 всего)
/style - меняет стиль общения, 1 - формальный, 2 - нормальный, 3 - токсичный и можно задать любой свой написав текст с инструкцией что бот должен делать и как
/last - выводит краткое содержание истории чата, последние X сообщений или все какие помнит /last [X]
/sum - делает выжимку из текста по ссылке (сумморизацию текста) /sum URL
/sum2 - то же что и /sum но не берет ответы из кеша, повторяет запрос заново
/mem - показывает содержимое своей памяти, в отладочных целях
```

![Пример1](pics/pic1.png)
![Пример2](pics/pic2.png)
![Пример3](pics/pic6.png)
![Пример4](pics/pic5.png)
![Пример5](pics/pic4.png)
![Пример6](pics/pic3.png)
![Пример7](pics/pic7.png)
![Пример8](pics/pic8.jpg)

## Установка

Для установки проекта выполните следующие шаги:

1. Установите Python 3.8+.
2. Установите утилиту trans `sudo apt-get install translate-shell`
3. Установите утилиту tesseract. В убунте 22.04.х (и дебиане 11) в репах очень старая версия тессеракта, надо подключать репозиторий с новыми версиями или ставить из бекпортов
    ```
    sudo apt-get update && \
    sudo apt-get install -y software-properties-common && \
    sudo add-apt-repository -y ppa:alex-p/tesseract-ocr5 && \
    sudo apt-get update && \
    sudo apt install tesseract-ocr tesseract-ocr-eng \
    tesseract-ocr-rus tesseract-ocr-ukr tesseract-ocr-osd
    ```
4. Установите словари и прочее `sudo apt install aspell aspell-en aspell-ru aspell-uk enchant-2 ffmpeg chromium-browser chromium-chromedriver python3-venv sox`
5. Клонируйте репозиторий с помощью команды:

   ```
   git clone https://github.com/theurs/tb1.git
   
   python -m venv .tb1
   source ~/.tb1/bin/activate
   
   ```
   
4. Перейдите в директорию проекта:

   ```
   cd tb1
   ```
   
5. Установите зависимости, выполнив команду:

   ```
   pip install -r requirements.txt
   ```

6. Создайте файл cfg.py и добавьте в него строку
```
token = 'токен телеграм бота'
key = 'openai api key'
# второй ключ для больших запросов, если нет то можно просто продублировать
key2 = 'openai api key'

# ключ для рисования через сайт химеры (рисует кандинский)
#https://discord.gg/BfwvN8Dy
#ChimeraGPT - The best API for chat completions with free GPT-4 access! Friendly community, free GPT-4, etc. only here! | 2510 members
#cfg.key_chimeraGPT = ''
key_chimeraGPT = 'xxx'

# разпознавание голоса, виспер лучше но требует много памяти и мощного процессора или видеокарту
stt = 'whisper'
whisper_model = 'medium' # ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large']
#stt = 'vosk'

# если хочется иметь канал(не группа) в котором будут все сгенерированные фотки то надо добавить туда бота
# id телеграм канала куда скидываются все сгенерированные картинки
pics_group = xxx
pics_group_url = 'https://t.me/yyy'

# размер буфера для поиска в гугле, чем больше тем лучше ищет и отвечает
# и тем больше токенов жрет
# для модели с 4к памяти
max_request = 1800
max_google_answer = 1000
# для модели с 16к памяти
#max_request = 15000
#max_google_answer = 2000

# насколько большие сообщения от юзера принимать
# если у gpt всего 4к памяти то 1500
#max_message_from_user = 4000
max_message_from_user = 1500



# 16k
#max_hist_lines = 18
#max_hist_bytes = 12000
#max_hist_compressed=1500
#max_hist_mem = 4000

# 4k
max_hist_lines = 10
max_hist_bytes = 2000
max_hist_compressed=700
max_hist_mem=300



# используем другой сервер, openai нас не пускает и ключей не продает, приходится заходить черз задний вход
# бесплатные ключи у дискорд бота https://github.com/PawanOsman/ChatGPT#use-our-hosted-api-reverse-proxy
# To use our hosted ChatGPT API, you can use the following steps:
# * Join our Discord server.
# * Get your API key from the #Bot channel by sending /key command.
# * Use the API Key in your requests to the following endpoints.
# * Присоединитесь к нашему серверу Discord.
# * Получите свой API-ключ в канале #Bot, отправив команду /key.
# * Используйте API-ключ в ваших запросах к следующим конечным точкам.
# * Если у бота поменялся адрес надо в дискорде боту написать /resetip

#openai_api_base = 'https://api.pawan.krd/v1'
# x2 price :(
openai_api_base = 'https://api.pawan.krd/unfiltered/v1'


# отдельный второй гейт если есть иначе продублировать. нужен для.. больших запросов в гугл
# https://discord.gg/cattogpt
# команда /info боту что бы получить ключ и статистику
# дают до 8т запросов
openai_api_base2 = 'https://api.cattto.repl.co/v1'


#https://discord.gg/BfwvN8Dy
#ChimeraGPT - The best API for chat completions with free GPT-4 access! Friendly community, free GPT-4, etc. only here! | 2510 members
#openai_api_base = 'https://chimeragpt.adventblocks.cc/v1'
#openai_api_base2  = 'https://chimeragpt.adventblocks.cc/v1'


# local poe.com proxy
# должен быть настроен и запущен https://github.com/juzeon/poe-openai-proxy
#openai_api_base = 'http://127.0.0.1:3700/v1'

model = 'gpt-3.5-turbo-16k'
#model = 'gpt-3.5-turbo-8k'
#model = 'gpt-3.5-turbo'
#model="Sage"
#model = 'Claude-instant'

# запасной прокси и ключ на случай если основной упал, если не то продублировать. должен быть совместим с основным
reserve_openai_api_base = 'xxx'
reserve_key = 'yyy'
```

Для работы распознавания голосовых сообщений надо установить vosk сервер.

`https://github.com/alphacep/vosk-server`

В докере.

`docker run -d -p 2700:2700 --name kaldi-ru --restart always -v /home/ubuntu/vosk/vosk-model-small-ru-0.22:/opt/vosk-model-en/model alphacep/kaldi-en:latest` тут путь заменить и модель скачать в эту папку

Eсли на сервере много оперативки то можно по другому

`docker run -d -p 2700:2700 --name kaldi-ru --restart always  alphacep/kaldi-ru:latest`

Надо несколько 4+ гигабайт на диске и несколько гигабайт оперативной памяти (не знаю сколько но много).

Что бы работал бинг аи надо сохранить свои куки с сайта bing.com раздел чат, попасть туда можно только с ип приличных стран и с аккаунтом в микрософте.
Сохранить куки можно с помощью браузерного расширения cookie editor. Формат json, имя cookies.json



7. Запустить ./tb.py

Можно собрать и запустить докер образ. Ну или нельзя Ж) давно не проверял.

В докер файл можно добавить свой файл cfg.py
Как в него засунуть vosk сервер я не знаю.


```
docker build  -t tb1 .
или
docker build --no-cache -t tb1 .
или
docker build --no-cache -t tb1 . &> build.log

docker run -d --env TOKEN='xxx' --name tb1 --restart unless-stopped tb1
или
docker run --env TOKEN='xxx' --name tb1 --restart unless-stopped tb1
или
docker run -d --env TOKEN='xxx' --env OPENAI_KEY='yyy' -e TZ=Asia/Vladivostok --name tb1 --restart unless-stopped tb1
```


## Использование

Перед тем как приглашать бота на канал надо в настройке бота у @Botfather выбрать бота, затем зайти в `Bot Settings-Group Privacy-` и выключить. После того как бот зашел на канал надо включить опять. Это нужно для того что бы у бота был доступ к сообщениям на канале.

## Лицензия

Лицензия, под которой распространяется проект.
