#!/usr/bin/env python3


import json
import openai
import os
from pathlib import Path

import cfg
import utils


# https://discord.gg/5N3zhMCh
openai.api_key = cfg.key_cattoGPT
openai.api_base = "https://free.catto.codes/v1"


def ai(prompt: str, messages = None, max_token: int = 2000, timeout: int = 180, model: str = 'gpt-3.5-turbo-16k-0613') -> str:
    """
    Generates a response from the cattoGPT model based on the given prompt and messages.

    Args:
        prompt (str): The user's prompt.
        messages (list, optional): A list of messages in the conversation. Defaults to None.
        max_token (int, optional): The maximum number of tokens in the generated response. Defaults to 2000.
        timeout (int, optional): The maximum time in seconds to wait for the response. Defaults to 180.
        model (str, optional): The name of the cattoGPT model. Defaults to 'gpt-3.5-turbo-16k-0613'.

    Returns:
        str: The generated response from the cattoGPT model.
    """
    assert openai.api_key != '', 'No key for cattoGPT'

    print(f'cattoGPT {model}', len(prompt))
    if messages == None:
        messages = [    {"role": "system",
                         "content": """Ты информационная система отвечающая на запросы юзера."""},
                         {"role": "user",
                         "content": prompt}
                    ]

    completion = openai.ChatCompletion.create(
        model=model,
        timeout=timeout,
        max_tokens=max_token,
        messages=messages
    )

    return completion.choices[0].message.content


def stt(audio_file: str) -> str:
    """
    Transcribes an audio file to text using OpenAI API.

    Args:
        audio_file (str): The path to the audio file.

    Returns:
        str: The transcribed text.

    Raises:
        FileNotFoundError: If the audio file does not exist.
    """

    assert openai.api_key != '', 'No key for cattoGPT'

    audio_file_new = Path(utils.convert_to_mp3(audio_file))

    audio_file_bytes = open(audio_file_new, "rb")

    translation = openai.Audio.transcribe("whisper-1", audio_file_bytes)

    try:
        audio_file_new.unlink()
    except PermissionError:
        pass

    return json.loads(json.dumps(translation, ensure_ascii=False))['text']


def image_gen(prompt: str, amount: int = 4, size: str ='1024x1024'):
    """
    Generates a specified number of images based on a given prompt.
    
    Parameters:
        - prompt (str): The text prompt used to generate the images.
        - amount (int, optional): The number of images to generate. Defaults to 10.
        - size (str, optional): The size of the generated images. Must be one of '1024x1024', '512x512', or '256x256'. Defaults to '1024x1024'.
        
    Returns:
        - list: A list of URLs pointing to the generated images.
    """
    assert openai.api_key != '', 'No key for cattoGPT'
    assert amount <= 10, 'Too many images to gen'
    assert size in ('1024x1024','512x512','256x256'), 'Wrong image size'
    response = openai.Image.create(
        prompt = prompt,
        n = amount,
        size=size,
    )
    return [x['url'] for x in response["data"]]


if __name__ == '__main__':

    #text = """Сегодня поговорим про новый беспарольный метод аутентификации по скейту. Условно можно сказать, что это совмещение пароля и второго фактора в виде мобильного телефона в одном девайсе. Собственно, в мобильном телефоне. Но на сайте, который популяризирует новую технологию, сказано, что это более защищенный путь, чем использование пароля и второго фактора. С этим можно поспорить, но давайте сначала разберемся, что это. Собственно, здесь же можно протестировать паскей, создав тестовый аккаунт. Указываете почту, это не открывает доступ к вашей почте, в принципе, можно указать любую липовую. Он говорит, что аккаунта нет, его нужно создать. И тут способы аутентификации. Можно использовать электронный USB-ключ, если есть, я почти уверен, что у вас нет. Можно использовать мобильные, которые привязаны к гугл-аккаунту уже, или любой другой мобильный, отсканировав на нем QR-код. Используем уже привязанный телефон, потом покажу, что делать с кодом. На телефон приходит уведомление, что кто-то пытается привязать этот телефон к аккаунту. Дальше пишут, что нужно поднести телефон к компьютеру. Не то, чтобы подносить, но телефон должен быть недалеко. Я отходил метров на десять, сработало. Показывают, к какому аккаунту, соглашаемся. И все, аккаунт создан. Теперь выходим из аккаунта и пытаемся авторизоваться с помощью passkey. Выбираем, куда отправить уведомление, то есть устройство, к которому passkey привязан, и на телефоне говорим «разблокировать». И все, мы зашли в аккаунт. Сейчас расскажу уже в практической плоскости, но сначала пара слов о технологии. Passkey не просто выкидывает пароль за ненадобностью, поскольку сейчас это выглядит просто как второй фактор. Например, при заходе в гугл вас также просят подтвердить свою личность с помощью пуш-уведомления на телефоне, но уже после ввода пароля. Тут на самом деле есть пароль, просто он зашит в passkey. Даже не пароль, а более защищенная система с парой ключей, открытым и закрытым. Обмен ключами происходит под капотом, а снаружи пользователю нужно лишь подтвердить свою личность привычным способом. С помощью отпечатка пальца, FaceID или пароля на разблокировку экрана. Скептиков прошу досмотреть до конца. Практическая плоскость. Пока немногие сервисы используют passkey, но используют, например, гугл, эппл, частично майкрософт. Посмотрим на гугл. Вам нужно управление аккаунтом, безопасность. Вот как раз отличный пример, почему надо использовать passkey. Если у вас не включена двухфакторка, а паролю уже 5 лет и он возможно присутствует в половине баз с засвеченными паролями. Меня оправдывает то, что это тестовый аккаунт. Значит, нам нужен ключ доступа, нужно ввести пароль от аккаунта, если устанавливаете впервые, создать ключ, использовать другое устройство. Я сейчас с ПК и он предлагает отсканировать QR-код. Никакие телефоны у меня к этому аккаунту пока не привязаны. На телефоне включаем сканер, сканируем код и говорим «Продолжить». Все. Ключ доступа создан. Выходим из аккаунта и пытаемся авторизоваться с помощью passkey. Он сразу предлагает этот способ. «Продолжить» и он отправляет уведомление на телефон. На телефоне соглашаемся, заходим. В чем преимущество? Вы можете создать несколько ключей. Например, используем QR-код, возьмем другой телефон, также отсканировали, зашли. И теперь у нас уже два устройства для захода в Гугл. Два физических устройства, мы можем посмотреть, когда и где они использовались для входа. Сейчас зайду с помощью второго. А вот, пишут, что последнее использование минуту назад. Ключи можно удалять. А в само устройство, например, совершенно не обязательно вставлять симку. Ну то есть, можно использовать какой-то старый телефон, который лежит у вас в надежном месте, и включаете вы его исключительно, чтобы авторизоваться с помощью passkey. Таким образом, это превращается в USB-флешку, один из самых надежных способов авторизации, поскольку никакие взломы, перехваты и подделка паролей и смс ей не страшны. Физический носитель в сундуке. Не защищает это всего вообще, ну это всего, что связано с интернетом. Только физическая кража со взломом вскроет ваш аккаунт. Ну еще ваш палец, но это дело наживное. Но при этом такая же схема с двухфакторкой, где приложение для двухфакторной аутентификации условно на телефоне без симки в сундуке, на мой взгляд, дает еще больше гарантий. Тогда злоумышленникам нужно не только выкрасть телефон и заполучить ваш палец, но и подобрать пароль. Все, любите друг друга, теперь это просто жизненно необходимо и помните, в конечном итоге все будет хорошо. Это говорю вам я Вова Ломов и теплица социальных технологий. ПОДПИСЫВАЙТЕСЬ!"""
    os.environ['all_proxy'] = cfg.all_proxy
    
    #image_prompt = 'автомобиль без колес вид сбоку. хищный вид. оформление для аватарки'
    #print(image_gen(image_prompt))
    
    print(stt('1.mp3'))

    #print(ai(open('1.txt', 'r').read()))

    #print(ai('hi'))
    #for i in openai.Model.list()['data']:
    #    print(i['id'])
