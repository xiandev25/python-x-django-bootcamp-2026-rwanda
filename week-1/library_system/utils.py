from datetime import datetime

def track_access(method):
    def wrapper(*args, **kwargs):
        print(f"Accessing {method.__name__}")
        print(f"Args: {args[1:] if len(args) > 1 else 'No args'}")
        print(f"Kwargs: {kwargs}")
        method(*args, **kwargs)
        print(f"Returned from {method.__name__} at {datetime.now()}")
    return wrapper

def permission_check(required_role):
    def decorator(method):
        def wrapper(*args, **kwargs):
            if "admin" != required_role:
                raise PermissionError("You don't have permission to perform this action")
            method(*args, **kwargs)
        return wrapper
    return decorator