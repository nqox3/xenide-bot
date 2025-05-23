def get_banned_users(ctx):
    # This function retrieves and displays a list of banned users.
    banned_users = await ctx.guild.bans()
    if banned_users:
        banned_list = "\n".join([f"{user.name}#{user.discriminator}" for user, _ in banned_users])
        await ctx.send(f"Banned users:\n{banned_list}")
    else:
        await ctx.send("There are no banned users in this server.")