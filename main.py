from highrise import *
from highrise.models import *
from asyncio import run as arun
from flask import Flask
from threading import Thread
from highrise.__main__ import *
import random
import asyncio
import time
from mesajlar import*

class Bot(BaseBot):
    def __init__(self):
        super().__init__()


    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")

    async def is_user_allowed(self, user: User) -> bool:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        return user_privileges.moderator or user.username in ["karainek", "karinca12"]
      
    async def on_chat(self, user: User, message: str) -> None:
        if message.lower() == "random" and await self.is_user_allowed(user):
            try:
                message_list = random.choice([espiri_mesaj, laf_mesaj, sarki_mesaj, rizz_mesaj])
                message = random.choice(message_list)
                await self.highrise.chat(message)
            except Exception as e:
                print(f"Caught Random Message Error: {e}")

  
    async def run(self, room_id, token) -> None:
        await __main__.main(self, room_id, token)
class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()
    
class RunBot():
    room_id = "662269a6f45635a7fe994c30"

  
    bot_tokens = [  
      "d34208ee64037319622f2090c4b5e55257424c94c4d540eaf9dd33168f5b95c0",
    "c79678b2c6e200c188b85d033c8d0129bd0eafbb6cff8082c76e97e0a2e55f66",
    "1d9a38ad5c9695a6bd06ff6efef9ba866110fa6966c990f6453543ca490b0242",
    "585bd844c2c9b9fe7129790a3c34d1c0a15b7311392dac2f7df1766d67f72441",
    "bd7cb335b9e58c50fc7e2c10eae3c5207442303581320aa19588e9329052c186",
    "a0b0d408826911aa2cf69fbd4767fcdb9ebf3eb7b4b91a95b1dc519f316c7429",
    "67dd0e2f29be83c08551c7794a461a28696e43983434a325d03ea86f9403a35b",
    "6986f5798ef1f6e43548557b16081995163dec3202039797267b873bc0f84fa8",
    "ff32e266f24af79f59bbdbe57c4d52313a96481ae37841c7392e19c3ad7aaa71",
    "04b72b9612c93589f2882617baa2845e18dd14a609455c38a175139c9e00f7d2",
    "4a719f6ebc12aa6d64156e7e1ee678301c2c392c3c6d1071c885da1ee373e246",
    "4138543249879d9a209db0d63232b56eec14c7bea879b0c9ae49d4fe4a31b4db",
    "095fb6a6fac0570741221df116d6a35e3f8d9ff3fdc9a173210ae2a1d7dca1a7",
    "b84348f314053ed943b065cd50c20d8b0570635a9f3d39c2916cd31830ecf247"
    ]

    bot_file = "main"
    bot_class = "Bot"

    def __init__(self) -> None:
        self.definitions = []
        for bot_token in self.bot_tokens:
            self.definitions.append(
                BotDefinition(
                    getattr(import_module(self.bot_file), self.bot_class)(),
                    self.room_id, bot_token)
            )
              
    def run_loop(self) -> None:
        while True:
            try:
                arun(main(self.definitions))
            except Exception as e:
                import traceback
                print("Caught an exception:")
                traceback.print_exc()
                time.sleep(1)
                continue


if __name__ == "__main__":
    WebServer().keep_alive()
    RunBot().run_loop()