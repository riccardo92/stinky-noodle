from convert_case import snake_case


def sanitize_callable_name(name: str) -> str:
    """Sanitzation for the JS callable name.

    Args:
        name (str): name of the callable

    Returns:
        str: sanitzed python compatible callable name
    """
    return snake_case(name)
