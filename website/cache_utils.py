
def task_list_cache_key(user):
    if user.role in [user.Role.ADMIN, user.Role.TEACHER]:
        return f"task_list_role_{user.role}"
    return f"task_list_user_{user.id}"