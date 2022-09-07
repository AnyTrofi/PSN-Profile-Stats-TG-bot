# PSN-Profile-Achivment
Parsing achievements and games from the PSN profile


To get information on the PSN profile: 

1) Run the 'main' function in the 'parse.py', passing the PSN ID there

2) Run the 'app.py' file and make a POST request: 'requests.post('http://127.0.0.1:5000/', json='Your PSN ID').text'

3) Run telegram bot('TG.py') and send PSN ID to TG bot

Parsing does not work in the Russian region, so use a VPN to work from the Russian region
