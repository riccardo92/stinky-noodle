import re
from typing import Any, Dict, List, Optional, Set, Tuple, Union

FALSY = (False, "", 0, None)
TRUTHY = (True, "", 1)
CASE_PATTERNS = {
    # "<type>": ("<patt>", "<default_separator>")
    "camel": ("^{0:s}[a-z]+({1:s}[A-Z][a-z]+)+$", ""),
    "pascal": ("^{0:s}[A-Z][a-z]+({1:s}[A-Z][a-z]+)+$", ""),
    "snake": ("^{0:s}[a-z]+({1:s}[a-z]+)+$", "_"),
    "kebab": ("^{0:s}[a-z]+({1:s}[a-z]+)+$", "-"),
    "cobol": ("^{0:s}[A-Z]+({1:s}[A-Z]+)+$", "-"),
    "macro": ("^{0:s}[A-Z]+({1:s}[A-Z]+)+$", "_"),
    "flat": ("^{0:s}[a-z{1:s}]+$", ""),
}


def alphabetical(obj: Any, keyed_by: Optional[str] = None) -> bool:
    if obj is None:
        raise ValueError("obj cannot have value None")

    if keyed_by is not None:
        return sorted(obj, key=lambda obj: obj[keyed_by]) == obj

    return sorted(obj) == obj


def enumeration(obj: Any, values: Union[Set, List, Tuple], **kwargs) -> bool:
    if obj is None:
        raise ValueError("obj cannot have value None")

    return obj in values


def falsy(obj: Any, **kwargs) -> bool:
    return obj in FALSY


def length(obj: Any, min: int, max: int) -> bool:
    if obj is None:
        raise ValueError("obj cannot have value None")

    return min <= len(obj) < max


def pattern(
    obj: str, match: Optional[str] = None, not_match: Optional[str] = None
) -> bool:
    """Apply a regex pattern or negated regex pattern to a string input.

    Args:
        obj (Any): The object we're applying the matching on.
        match (Optional[str], optional): Pattern we want to find a match for.
            Defaults to None.
        not_match (Optional[str], optional): Pattern we don't want to find a
            math for. Defaults to None.

    Returns:
        bool: Whether we matched what was specified in the match arg or
        we didn't match what was in the not_match arg.
    """
    if obj is None:
        raise ValueError("obj cannot have value None")

    cond = True
    if match is not None:
        cond &= re.match(match, obj) is not None
    if not_match is not None:
        cond &= not (re.match(not_match, obj) is not None)
    return cond


def casing(
    obj: str,
    type: str,
    disallow_digits: Optional[bool] = False,
    separator: Optional[Dict] = None,
) -> bool:
    """Detect the use of different casings.

    Args:
        obj (Any): The object we're applying the matching on.
        type (str): Type of casing.
        disallow_digits (Optional[bool], optional): Whether digits are allowed at all. Defaults to False.
        separator (Optional[Dict], optional): a dict containing char (str) and allow_leading (bool). Defaults to None.
    """

    if obj is None:
        raise ValueError("obj cannot have value None")

    if disallow_digits and re.match(r"[0-9]", obj):
        return False

    try:
        patt, sep = CASE_PATTERNS[type]
    except KeyError:
        raise ValueError(f"Case type {type} is not recognized.")

    leading_sep = ""
    if separator is not None:
        sep = re.escape(separator.get("char", sep))
        leading = separator.get("allow_leading", False)
        if leading:
            leading_sep = sep

    patt = patt.format(leading_sep, sep)
    return re.match(patt, obj) is not None


def schema(obj: Any, **kwargs):
    pass


def truthy(obj: Any, **kwargs) -> bool:
    return obj in TRUTHY


def undefined(obj: Any) -> bool:
    return obj is None


def defined(obj: Any) -> bool:
    return not undefined(obj)


def unreferencedReusableObject(obj: Any):
    pass


def xor(obj: Any, properties: List[str]) -> bool:
    return len(defined(obj.get(prop) for prop in properties)) == 1
