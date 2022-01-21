import discord

bot = discord.Client()

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.content == "help":
		await message.channel.send("Чтобы авторизироваться введите /login логин пароль\n"
								   "")


bot.run("OTM0MDE4OTEzMzYzMTg1Njg0.Yep-5g.RghntvqihzYhCXWld0-2teYzSoM")