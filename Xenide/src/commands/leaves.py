def leaves_command(ctx):
    user = ctx.author
    leave_message = f"{user.name} has left the server."
    # Here you can add logic to log the leave event or notify the server
    await ctx.send(leave_message)