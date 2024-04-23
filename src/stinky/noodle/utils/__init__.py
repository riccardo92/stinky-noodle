def sanitize_func_name(name: str) -> str:
    """_summary_

    Args:
        name (str): _description_

    Returns:
        str: _description_
    """
    return name.replace("-", "_").lower()
