# KCL --- Kiyzen Console Log

A simple Flask-based web console for viewing logs in real time.

------------------------------------------------------------------------

## Requirements

-   Termux
-   Internet connection

------------------------------------------------------------------------

# Installation

### Session 1 --- Start the Server

``` bash
pkg update -y && pkg upgrade -y && pkg install -y git python cloudflared && git clone https://github.com/kisaragi-kiyzen/KCL-Kiyzen_Console_Log.git && cd KCL-Kiyzen_Console_Log && pip install --upgrade pip flask && python app.py
```

The server will start at:

    http://127.0.0.1:5000

------------------------------------------------------------------------

### Session 2 --- Send Logs

Create a `send` command:

``` bash
echo 'alias send='\''f(){ curl -s -X POST -H "Content-Type: application/json" -d "{\"pesan\":\"$1\"}" http://127.0.0.1:5000/api/input; }; f'\''' >> ~/.bashrc && source ~/.bashrc
```

Send a log:

``` bash
send "Hello World!"
```

Example:

``` bash
send "Bot Started"
send "Connected"
send "User Login"
```

------------------------------------------------------------------------

## Public Access (Optional)

Expose the local server using Cloudflare Tunnel:

``` bash
cloudflared tunnel --url http://127.0.0.1:5000
```

Cloudflare will generate a public URL similar to:

    https://xxxxxxxx.trycloudflare.com

Open the generated URL in your browser.

------------------------------------------------------------------------

## API

### Send Log

`POST /api/input`

``` json
{
  "pesan": "Hello World!"
}
```

### Get Logs

`GET /api/data`

Returns all stored logs in JSON format.

------------------------------------------------------------------------

## Notes

-   Logs are stored in memory only.
-   Restarting the server will clear all logs.
-   This project is intended for lightweight logging and testing.
