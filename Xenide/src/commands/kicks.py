def kick_user(ctx, user: str):
    """Kicks a user from the server."""
    member = ctx.guild.get_member_named(user)
    if member:
        await member.kick(reason="Kicked by command.")
        await ctx.send(f"{user} has been kicked from the server.")
    else:
        await ctx.send(f"User {user} not found.")

def setup(bot):
    """Adds the kick command to the bot."""
    @bot.command(name='kicks')
    async def kicks_command(ctx, user: str):
        await kick_user(ctx, user)