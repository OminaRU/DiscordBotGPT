from app.discord_bot.discordbot_api import client, discord_token


if __name__ == '__main__':
    client.run(discord_token)



##https://discord.com/api/oauth2/authorize?client_id=1070896486268813413&permissions=8&scope=bot