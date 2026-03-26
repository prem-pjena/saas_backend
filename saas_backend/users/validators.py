def validate_user(data):
    if "username" not in data:
        return {"success": False, "error": "username is required"}

    if not isinstance(data["username"], str):
        return {"success": False, "error": "username must be string"}

    if "age" not in data:
        return {"success": False, "error": "age is required"}

    if not isinstance(data["age"], int):
        return {"success": False, "error": "age must be integer"}

    if data["age"] <= 0:
        return {"success": False, "error": "age must be greater than 0"}

    return {"success": True, "data": data}