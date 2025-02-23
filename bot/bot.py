#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

from pyrogram import Client, enums, __version__
from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 
from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="file_to_link",  # Corrected variable name
            session_string="BQD-9WAAjJiCaAYI-MF7tp42DWqwjXC_A16fA2AhPUwbFj259Y82VuiVuDlECInPHpfkM9IYEAc0tBAIUmcClbnf6FFg7KzjahrOrrsKr__JRaSUXh-Ww43bDCzCa8UmnfemLnPiPg50d8vydakYJ7GMdxRjWkIyL4nq2NTe3O3UP3fcJ-GSYv2FWNKplsvBf56bv1otjsomKx-2ClhhYzJZITUzVa8NpSukBwQNjpG9AQpXRESIMorqjHbtCjAhAPLSWcZDBDJXu3hn0_rVEMKF7EYZYtDi2UfDJPZhJXFk1vvJn6OfgAqG2EFIxc5978D7lYJsEOohWqc8qrKSnCRRuoQzSwAAAAFGz15EAA",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "bot/plugins"},
            workers=200,
            sleep_threshold=10
)


        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

from pyrogram import Client, enums, __version__
from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 
from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="file_to_link",
            session_string="BQD-9WAAjJiCaAYI-MF7tp42DWqwjXC_A16fA2AhPUwbFj259Y82VuiVuDlECInPHpfkM9IYEAc0tBAIUmcClbnf6FFg7KzjahrOrrsKr__JRaSUXh-Ww43bDCzCa8UmnfemLnPiPg50d8vydakYJ7GMdxRjWkIyL4nq2NTe3O3UP3fcJ-GSYv2FWNKplsvBf56bv1otjsomKx-2ClhhYzJZITUzVa8NpSukBwQNjpG9AQpXRESIMorqjHbtCjAhAPLSWcZDBDJXu3hn0_rVEMKF7EYZYtDi2UfDJPZhJXFk1vvJn6OfgAqG2EFIxc5978D7lYJsEOohWqc8qrKSnCRRuoQzSwAAAAFGz15EAA",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "bot/plugins"},
            workers=200,
            sleep_threshold=10
        )

import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "OK", 200  # ✅ Ensures Koyeb health check passes

def run_server():
    port = int(os.getenv("PORT", 8080))  # Read PORT from env
    print(f"Starting Flask server on port {port}...")
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()

    # Start Telegram bot
    bot = Bot()
    bot.run()


