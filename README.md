# KCL-Kiyzen_Console_Log
A boring web development project.

# Termux.

First session.
```bash
pkg update -y && pkg upgrade -y && pkg install -y git python cloudflared && git clone https://github.com/kisaragi-kiyzen/KCL-Kiyzen_Console_Log && cd KCL-Kiyzen_Console_Log && pip install --upgrade pip flask && python app.py

```

Second session.
```bash
echo "alias kirim='f() { curl -X POST -H \"Content-Type: application/json\" -d \"{\\\"pesan\\\":\\\"\$1\\\"}\" http://127.0.0.1:5000/api/input; }; f'" >> ~/.bashrc && source ~/.bashrc && kirim "<message>"
```
