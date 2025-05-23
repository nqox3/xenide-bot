def handle_joins_event(member):
    # This function handles user join events and displays relevant information.
    channel = member.guild.system_channel
    if channel is not None:
        welcome_message = f"Welcome {member.mention} to {member.guild.name}!"
        await channel.send(welcome_message)

async def joins_command(ctx):
    # This command retrieves and displays information about recent joins.
    guild = ctx.guild
    members = guild.members
    recent_joins = [member for member in members if member.joined_at > (datetime.utcnow() - timedelta(days=7))]
    
    if recent_joins:
        join_list = "\n".join([member.name for member in recent_joins])
        await ctx.send(f"Recent joins in {guild.name}:\n{join_list}")
    else:
        await ctx.send("No recent joins in this server.")