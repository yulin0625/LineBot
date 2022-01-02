import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, MessageTemplateAction, TemplateSendMessage, ButtonsTemplate


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_img_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url =url, preview_image_url = url))

    return "OK"

def send_button_message(reply_token, img, title, uptext, labels, texts): # id
    line_bot_api = LineBotApi(channel_access_token)
    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text = 'Buttons template',
        template = ButtonsTemplate(
            thumbnail_image_url=img,
            title = title,
            text=uptext,
            actions=acts
        )
    )
    
    line_bot_api.reply_message(reply_token, message)
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
