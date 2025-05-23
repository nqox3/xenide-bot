def format_message(content):
    return f"**{content}**"

def handle_error(error_message):
    return f"Error: {error_message}"

def extract_user_id(user):
    return user.id if user else None

def is_admin(user):
    return user.guild_permissions.administrator if user else False

def format_user_list(users):
    return ', '.join([user.name for user in users]) if users else "No users found."