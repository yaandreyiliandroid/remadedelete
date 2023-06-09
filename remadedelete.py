import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.content.startswith('$cr'):
            msg = await message.channel.send('я сейчас же тебя удалю>:)')
            await msg.delete()

            # this also works
            await message.channel.send('Попращайся через 3 секунды>:D.....', delete_after=3.0)

    async def on_message_delete(self, message):
        msg = f'{message.author} Удалил сообщение: {message.content}'
        await message.channel.send(msg)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')
