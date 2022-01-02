import random
from transitions.extensions import GraphMachine

from utils import send_text_message, send_img_message, send_button_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_draw(self, event):
        text = event.message.text
        return text == "抽"

    def go_back(self, event):
        text = event.message.text
        return text == "返回"

    def is_going_to_store1(self, event):
        text = event.message.text
        return text == "可不可熟成紅茶" or text == "可不可"

    def is_going_to_store2(self, event):
        text = event.message.text
        return text == "50嵐"

    def is_going_to_store3(self, event):
        text = event.message.text
        return text == "清心福全" or text == "清心"

    def is_going_to_store4(self, event):
        text = event.message.text
        return text == "迷客夏" or text == "milkshop"

    def is_going_to_store5(self, event):
        text = event.message.text
        return text == "麻古茶坊" or text == "麻古" or text =="macu"

    def watch_menu(self, event):
        text = event.message.text
        return text == "菜單"

    def search_store(self, event):
        text = event.message.text
        return text == "搜尋附近店家"

    def on_enter_draw(self, event):
        msg = random.choice(["茶類", "奶類", "鮮果汁", "咖啡"])
        reply_token = event.reply_token
        send_text_message(reply_token, msg)

    def on_enter_user(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "不知道要喝什麼嗎？\n輸入「抽」來抽飲料吧!")

    def on_enter_store1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        img = 'https://www.kebuke.com/wp-content/uploads/2020/12/fb-banner.png'
        title = '可不可熟成紅茶'
        uptext = '想做什呢？'
        labels = ['看菜單', '搜尋附近店家', '返回']
        texts = ['菜單', '搜尋附近店家', '返回']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_menu1(self, event):
        print("I'm entering menu1")
        reply_token = event.reply_token
        send_img_message(reply_token, "https://1.bp.blogspot.com/-ACZo5VAz4ds/YQYZnlc6K3I/AAAAAAAAanw/zHwvIPd4qloD1mFj441_gTV0cG4enQ9TwCLcBGAsYHQ/s2048/%25E3%2580%2590%25E5%258F%25AF%25E4%25B8%258D%25E5%258F%25AF%25E7%2586%259F%25E6%2588%2590%25E7%25B4%2585%25E8%258C%25B6%25E3%2580%25912021%25E8%258F%259C%25E5%2596%25AE%25E5%2583%25B9%25E7%259B%25AE%25E8%25A1%25A8.png")

    def on_enter_search1(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com/maps/search/%E5%8F%AF%E4%B8%8D%E5%8F%AF%E7%86%9F%E6%88%90%E7%B4%85%E8%8C%B6/")

    def on_enter_store2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        img = 'https://cdn-order.nidin.shop/nidin2/statics/50lan/share.png'
        title = '50嵐'
        uptext = '想做什呢？'
        labels = ['看菜單', '搜尋附近店家', '返回']
        texts = ['菜單', '搜尋附近店家', '返回']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_menu2(self, event):
        print("I'm entering menu2")

        reply_token = event.reply_token
        send_img_message(reply_token, "https://twcoupon.com/images/menu/p_50lan_20140730.jpg")

    def on_enter_search2(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com/maps/search/50%E5%B5%90/")

    def on_enter_store3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        img = 'https://sites.google.com/site/qwefgh1487/_/rsrc/1466077042506/qing-xinlogo/%E4%B8%8B%E8%BC%89.png'
        title = '清心福全'
        uptext = '想做什呢？'
        labels = ['看菜單', '搜尋附近店家', '返回']
        texts = ['菜單', '搜尋附近店家', '返回']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_menu3(self, event):
        print("I'm entering menu3")

        reply_token = event.reply_token
        send_img_message(reply_token, "https://twcoupon.com/images/menu/p_chingshin.jpg")

    def on_enter_search3(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com/maps/search/%E6%B8%85%E5%BF%83%E7%A6%8F%E5%85%A8/")

    def on_enter_store4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        img = 'https://ap-south-1.linodeobjects.com/nidin-production/brand/icons/2_1784e0af64ea9f22.png'
        title = '迷客夏'
        uptext = '想做什呢？'
        labels = ['看菜單', '搜尋附近店家', '返回']
        texts = ['菜單', '搜尋附近店家', '返回']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_menu4(self, event):
        print("I'm entering menu4")

        reply_token = event.reply_token
        send_img_message(reply_token, "https://www.milkshoptea.com/upload/price/2111020819100000002.jpg")

    def on_enter_search4(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com/maps/search/%E8%BF%B7%E5%AE%A2%E5%A4%8F/")

    def on_enter_store5(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        img = 'https://www.findcoupon.tw/uploads/logo/1000/1150.png'
        title = '麻古茶坊'
        uptext = '想做什呢？'
        labels = ['看菜單', '搜尋附近店家', '返回']
        texts = ['菜單', '搜尋附近店家', '返回']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def on_enter_menu5(self, event):
        print("I'm entering menu5")

        reply_token = event.reply_token
        send_img_message(reply_token, "https://twcoupon.com/images/menu/p_maculife_s.jpg")

    def on_enter_search5(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com/maps/search/%E9%BA%BB%E5%8F%A4%E8%8C%B6%E5%9D%8A/")    

if __name__ == "__main__":
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

    img = machine.get_graph().draw("fsm.png", prog="dot", format="png")
    img = img.save("fsm.jpg")