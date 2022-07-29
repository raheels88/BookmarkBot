import discord
import os
from datetime import datetime
from replit import db


intents = discord.Intents.default()
intents.members = True
client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_raw_reaction_add(payload):
	message_id = payload.message_id
	channel_id = payload.channel_id
	channel = client.get_channel(channel_id)
	user = payload.member

	if isinstance(channel, discord.channel.DMChannel) == False:

		emoji = payload.emoji

		message = await channel.fetch_message(message_id)
		msg_auth = message.author

		if emoji.name == "🔖":
			x = datetime.now()
			embed = discord.Embed(title="Message",
														url=message.jump_url,
														description=message.content,
														color=0xFF5733)
			pfp = msg_auth.avatar_url
			embed.set_author(name=msg_auth, url=message.jump_url, icon_url=pfp)
			msg_sent = message.created_at
			embed.set_footer(text="Message sent " +
											 str(msg_sent.strftime("%H:%M, %d-%m-%Y")))

			send = await user.send("**Bookmark Created:** " +
														 str(x.strftime("%H:%M, %d-%m-%Y")) + "\n" +
														 message.jump_url,
														 embed=embed)

			await send.add_reaction("❌")
			'''dmchan = send.channel
			bookmarks = await dmchan.history().flatten()
			numBookmarks = len(bookmarks)

			if numBookmarks%10 == 0:
				gimme = await user.send("\nYou have saved " + str(numBookmarks) + " bookmarks!\n\nIf you've benefited from BookmarkBot, feel free to buy its creator a coffee here - https://www.buymeacoffee.com/raheelsbots 😃")
				await gimme.add_reaction("❌")'''

	if isinstance(channel, discord.channel.DMChannel) == True:
		dm_message_id = payload.message_id
		dm_channel_id = payload.channel_id
		dm_channel = client.get_channel(dm_channel_id)
		dm_message = await dm_channel.fetch_message(dm_message_id)
		dm_emoji = payload.emoji
		#print(client.user)
		#print(payload.user_id)
		#print(dm_message.author)

		if str(payload.user_id) != "836876877364461589":
			if dm_emoji.name == "❌":
				await dm_message.delete()

client.run(os.getenv('TOKEN'))