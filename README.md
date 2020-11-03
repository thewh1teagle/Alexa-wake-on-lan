# Alexa-wake-on-lan
## "Alexa, turn on my pc" <img src="https://user-images.githubusercontent.com/61390950/95663640-9aa5b000-0b49-11eb-923a-a5442b8a78f8.jpg" alt="alt text" width="100" height="100">





### How to setup
1. Firstly, enable wol in your bios. You can use this [guide](https://www.howtogeek.com/70374/how-to-geek-explains-what-is-wake-on-lan-and-how-do-i-enable-it/)

You can test it with this [app](https://play.google.com/store/apps/details?id=co.uk.mrwebb.wakeonlan)

2. Install python3

3. Create new account in sinric.com And create new device

4. Clone the repo and change in app.py the mac of the pc you want to. grab token and device id from sinric.com and change them too.

5. Install dependencies and start the applications.
```shell
pip install -r requirements.txt && python3 app.py
```
