<h1 align="center">KCL — Kiyzen Console Log</h1>

<p align="center">
A simple Flask-based web console for viewing logs in real time.
</p>

<p align="center">
<img src="https://img.shields.io/github/license/kisaragi-kiyzen/KCL-Kiyzen_Console_Log">
<img src="https://img.shields.io/github/repo-size/kisaragi-kiyzen/KCL-Kiyzen_Console_Log">
<img src="https://img.shields.io/github/last-commit/kisaragi-kiyzen/KCL-Kiyzen_Console_Log">
<img src="https://img.shields.io/github/stars/kisaragi-kiyzen/KCL-Kiyzen_Console_Log">
</p>

---

## ✨ Features

- Real-time web console
- Flask backend
- JSON API
- Mobile-friendly interface
- Cloudflare Tunnel support

---

## 📋 Requirements

- Termux
- Internet connection

---

## 🚀 Installation

### Session 1 — Start the Server

```bash
pkg update -y && pkg upgrade -y && pkg install -y git python cloudflared && git clone https://github.com/kisaragi-kiyzen/KCL-Kiyzen_Console_Log.git && cd KCL-Kiyzen_Console_Log && pip install --upgrade pip flask && python app.py
```

Open your browser:

```text
http://localhost:5000
```

### Session 2 — Send Logs

```bash
echo 'alias send='\''f(){ curl -s -X POST -H "Content-Type: application/json" -d "{\"pesan\":\"$1\"}" http://127.0.0.1:5000/api/input; }; f'\''' >> ~/.bashrc && source ~/.bashrc
```

Example:

```bash
send "Bot Started"
send "Connected"
send "User Login"
```

---

## 🌐 Public Access

```bash
cloudflared tunnel --url http://127.0.0.1:5000
```

---

## 📡 API

| Endpoint | Method | Description |
|----------|:------:|-------------|
| `/api/input` | POST | Send a log |
| `/api/data` | GET | Get all logs |

### Example Request

```json
{
  "pesan": "Hello World!"
}
```

---

## 📝 Notes

- Logs are stored in memory only.
- Restarting the server clears all logs.
- Designed for lightweight logging and testing.

---

## 📄 License

This project is licensed under the **Apache License 2.0**.

See the [LICENSE](LICENSE) file for more information.
