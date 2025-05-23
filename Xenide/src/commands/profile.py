def get_user_profile(user_id):
    # This function would typically retrieve user profile information from a database or API.
    # For demonstration purposes, we'll return a mock profile.
    return {
        "user_id": user_id,
        "username": "SampleUser",
        "join_date": "2023-01-01",
        "roles": ["Member", "Moderator"],
        "status": "Active"
    }

async def profile_command(ctx, user_id):
    profile = get_user_profile(user_id)
    
    embed = discord.Embed(title=f"Profile of {profile['username']}", color=0x00ff00)
    embed.add_field(name="User ID", value=profile['user_id'], inline=True)
    embed.add_field(name="Join Date", value=profile['join_date'], inline=True)
    embed.add_field(name="Roles", value=", ".join(profile['roles']), inline=True)
    embed.add_field(name="Status", value=profile['status'], inline=True)
    
    await ctx.send(embed=embed)