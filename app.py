import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
    transitions=[
        # drow lots
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
            "dest": "draw",
            "conditions": "is_going_to_draw",
        },
        # goto store
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
            "dest": "store1",
            "conditions": "is_going_to_store1",
        },
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
            "dest": "store2",
            "conditions": "is_going_to_store2",
        },
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
            "dest": "store3",
            "conditions": "is_going_to_store3",
        },
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
            "dest": "store4",
            "conditions": "is_going_to_store4",
        },
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "draw", "menu1", "menu2", "menu3", "menu4", "menu5", "search1", "search2", "search3", "search4", "search5"],
            "dest": "store5",
            "conditions": "is_going_to_store5",
        },
        # menu
        {
            "trigger": "advance",
            "source": "store1",
            "dest": "menu1",
            "conditions": "watch_menu",
        },
        {
            "trigger": "advance",
            "source": "store2",
            "dest": "menu2",
            "conditions": "watch_menu",
        },
        {
            "trigger": "advance",
            "source": "store3",
            "dest": "menu3",
            "conditions": "watch_menu",
        },
        {
            "trigger": "advance",
            "source": "store4",
            "dest": "menu4",
            "conditions": "watch_menu",
        },
        {
            "trigger": "advance",
            "source": "store5",
            "dest": "menu5",
            "conditions": "watch_menu",
        },
        # search
        {
            "trigger": "advance",
            "source": "store1",
            "dest": "search1",
            "conditions": "search_store",
        },
        {
            "trigger": "advance",
            "source": "store2",
            "dest": "search2",
            "conditions": "search_store",
        },
        {
            "trigger": "advance",
            "source": "store3",
            "dest": "search3",
            "conditions": "search_store",
        },
        {
            "trigger": "advance",
            "source": "store4",
            "dest": "search4",
            "conditions": "search_store",
        },
        {
            "trigger": "advance",
            "source": "store5",
            "dest": "search5",
            "conditions": "search_store",
        },
        # go back
        {
            "trigger": "advance",
            "source": ["user", "store1", "store2", "store3", "store4", "store5", "store6", "draw"],
            "dest": "user",
            "conditions": "go_back",
        },
        {
            "trigger": "advance",
            "source": ["menu1", "search1"],
            "dest": "store1",
            "conditions": "go_back",
        },
        {
            "trigger": "advance",
            "source": ["menu2", "search2"],
            "dest": "store2",
            "conditions": "go_back",
        },
        {
            "trigger": "advance",
            "source": ["menu3", "search3"],
            "dest": "store3",
            "conditions": "go_back",
        },
        {
            "trigger": "advance",
            "source": ["menu4", "search4"],
            "dest": "store4",
            "conditions": "go_back",
        },
        {
            "trigger": "advance",
            "source": ["menu5", "search5"],
            "dest": "store5",
            "conditions": "go_back",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請輸入正確指令")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
