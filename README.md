# TG Listener Bot
This bot will listen to all messages you receive on telegram and aggregate it to a single group/channel. The bot allows filtering messages from specific groups & users


# Requirements
- Python3 

# Installation & Running

###Clone this repository
```
git clone https://github.com/daedlock/tg-listener-py
```

### Install dependencies
```
pip3 install -r requirements.txt
```

### Update config
Update the `config.toml` file to your liking. 
*Note: you can get api_id and api_hash from https://my.telegram.org/

### Running the bot
In your terminal, make sure you are in the tg-listener-py directory then run:
```
python main.py
```