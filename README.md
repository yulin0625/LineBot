# LineBot
2021計算理論project
## 創立主旨
因為自己及朋友常常會為了想要喝什飲料而煩惱，於是這次決定要做一個LineBot來解決我們的困擾。此聊天機器人提供三種服務：

* 飲料種類抽籤
* 提供5家熱門飲料店菜單
* 一鍵搜尋附近店家

## 介紹
### 基本資訊
名稱：喝飲料小幫手
ID:@552ofbhh (line ID搜尋)
![](https://i.imgur.com/A02oi6N.jpg)

### 使用方式
#### 加入好友
![](https://i.imgur.com/bFfF1if.png)
#### 使用方式說明
![](https://i.imgur.com/zFXc6fy.jpg)

#### 輸入 「抽」 來抽取飲料種類
![](https://i.imgur.com/KySckyR.jpg)

#### 點選 「下方選單」 選擇喜歡的飲料店
![](https://i.imgur.com/qN3rHvo.jpg)

#### 點選 「看菜單」
![](https://i.imgur.com/DWB7wcI.jpg)

#### 機器人傳送該店的菜單
![](https://i.imgur.com/SSc5AfW.jpg)

#### 點選 「返回」 回到店家頁面
![](https://i.imgur.com/hv1SbDl.jpg)

#### 點選 「搜尋附近店家」
![](https://i.imgur.com/kpq9DaF.jpg)

#### 機器人將傳送該店的Google地圖搜尋結果
![](https://i.imgur.com/gKDASL3.jpg)

## Finite State Machine
![](https://i.imgur.com/E31d0IF.jpg)

## Run Locally
You can using `ngrok` as a proxy.

### Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```
