import discord
import datetime
from time import gmtime, strftime
from datetime import date
import time
import asyncio
import os

num = 60
token = os.environ.get('BOT_TOKEN')
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def time_check():
	print("Running time check")
	await bot.wait_until_ready()
	print("Bot ready")
	print(bot.is_closed)
	while not bot.is_closed():
		print("Inside loop")
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		print(current_time)
		today = date.today()
		# print(today)
		d = today.strftime("%a")
		# print(d)
		channel = bot.get_channel(764596098437349401)
		if d == "Mon" or d == "Tue" or d == "Wed" or d == "Thu" or d == "Fri":
			if d == "Wed" and current_time >= "7:55:00" and current_time <= "8:20:00":
				await channel.send( "FBLA is starting in a minute.")
			if current_time >= "8:33:30" and current_time <= "8:34:30":
				await channel.send("Period 1 is starting is a minute.")
			if current_time >= "9:29:30" and current_time <= "9:30:30":
				await channel.send("Period 2 is starting is a minute.")
			if current_time >= "10:21:30" and current_time <= "10:21:30":
				await channel.send("Period 3 is starting is a minute.")
			if current_time >= "11:13:30" and current_time <= "11:14:30":
				await channel.send("Period 4 is starting is a minute.")
			if current_time >= "12:05:30" and current_time <= "12:06:30":
				await channel.send("Period 5 is starting is a minute.")
			if current_time >= "12:57:30" and current_time <= "12:58:30":
				await channel.send("Period 6 is starting is a minute.")
			if current_time >= "13:49:30" and current_time <= "13:50:30":
				await channel.send("Period 7 is starting is a minute.")
			if current_time >= "14:41:30" and current_time <= "14:42:30":
				await channel.send("Period 8 is starting is a minute.")
			if d == "Mon" and current_time >= "15:43:30" and current_time <= "15:44:30":
				await channel.send("Computer Science Club is starting in a minute.")
			if d == "Mon" and current_time >= "16:30:00" and current_time <= "16:31:00":
				await channel.send("School is over.")
			if d == "Thu" and current_time >= "15:28:30" and current_time <= "15:29:30":
				await channel.send("History Bee/Bowl is starting in a minute.")
			if d == "Thu" and current_time > "16:30:00" and current_time < "16:40:00":
				await channel.send("School is over.")
			if (d == "Tue" or d == "Wed" or d == "Fri") and current_time >= "15:20:00" and current_time <= "15:21:00":
				await channel.send("School is over.")
			await asyncio.sleep(60)
		elif d == "Sat" or d == "Sun":
			print("Weekend")
			await asyncio.sleep(1800)
async def on_message(message):
	if message.content == "!schedule":
		await message.channel.send("Daily Schedule:\nPeriod 1      |     8:35 - 9:16\nPeriod 2     |     9:31 - 10:08\nPeriod 3     |     10:23 - 11:00\nPeriod 4     |     11:15 - 11:52\nPeriod 5     |     12:07 - 12:44\nPeriod 6     |     12:59 - 1:36\nPeriod 7     |     1:51 - 2:28\nPeriod 8     |     2:43 - 3:20")
	if message.content == "!club":
		await message.channel.send("Clubs:\nMonday            |     Computer Science Club (3:45 - 4:30)\nWednesday     |     FBLA (7:55 - 8:20)\nThursday          |     History Bee/Bowl (3:30 - 4:30)")

bot.loop.create_task(time_check())
#bot.loop.create_task(on_message(message))
bot.run(token)
