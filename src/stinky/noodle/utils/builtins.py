import re
from typing import Any, Dict, List, Optional, Set, Tuple, Union

FALSY = (False, "", 0, None)
TRUTHY = (True, "", 1)
CASE_PATTERNS = {
    "camel": "^{0:s}[a-zA-Z]+({1:s}[A-Z][a-z]+)+$",
    "pascal": "^{0:s}[A-Z][a-z]+({1:s}[A-Z][a-z]+)+$",
    "snake": "^{0:s}[a-z]+({1:s}[a-z]+)+$",
    "kebab": "^{0:s}[a-z]+({1:s}[a-z]+)+$",
    "cobol": "^{0:s}[A-Z]+({1:s}[A-Z]+)+$",
    "flat": "^{0:s}[a-z{1:s}]+$",
}


def alphabetical(obj: Any, keyed_by: Optional[str] = None):
    if keyed_by is not None:
        return sorted(obj, key=keyed_by) == obj

    return sorted(obj) == sorted


def enumeration(obj: Any, values: Union[Set, List, Tuple], **kwargs):
    return obj in values


def falsy(obj: Any, **kwargs):
    return obj in FALSY


def length(obj: Any, min: int, max: int):
    return min <= len(obj) < max


def pattern(obj: Any, match: Optional[str] = None, not_match: Optional[str] = None):
    """_summary_

    Args:
        obj (Any): _description_
        match (Optional[str], optional): _description_. Defaults to None.
        not_match (Optional[str], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    if obj is None:
        return False
    cond = True
    if match is not None:
        cond &= re.match(match, obj)
    if match is not None:
        cond &= not re.match(not_match, obj)
    return cond


def casing(
    obj: str,
    type: str,
    disallow_digits: Optional[bool] = False,
    separator: Optional[Dict] = None,
):
    """Detect the use of different casings.

    Args:
        obj (Any): The object we're applying the matching on.
        type (str): Type of casing.
        disallow_digits (Optional[bool], optional): Whether digits are allowed at all. Defaults to False.
        separator (Optional[Dict], optional): a dict containing char (str) and allow_leading (bool). Defaults to None.
    """

    if disallow_digits and re.match(r"[0-9]", obj):
        return False

    if type == "camel":
        sep = ""
        patt = CASE_PATTERNS["camel"]
    elif type == "pascal":
        sep = ""
        patt = CASE_PATTERNS["pascal"]
    elif type == "snake":
        sep = "_"
        patt = CASE_PATTERNS["snake"]
    elif type == "kebab":
        sep = "-"
        patt = CASE_PATTERNS["kebab"]
    elif type == "flat":
        sep = ""
        patt = CASE_PATTERNS["flat"]
    elif type == "cobol":
        sep = "-"
        patt = CASE_PATTERNS["cobol"]
    elif type == "macro":
        sep = "_"
        patt = CASE_PATTERNS["macro"]
    else:
        raise ValueError(f"Case type {type} is not recognized.")

    if separator is not None:
        sep = separator.get("char", sep)
        leading = separator.get("allow_leading", False)
        leading_sep = ""
        if leading:
            leading_sep = sep

    patt = patt.format(leading_sep, sep)
    return obj & re.match(patt, obj) | False


def schema(obj: Any, **kwargs):
    pass


def truthy(obj: Any, **kwargs):
    return not falsy(obj)


def undefined(obj: Any):
    return obj is None


def defined(obj: Any):
    return not undefined(obj)


def unreferencedReusableObject(obj: Any):
    pass


def xor(obj: Any, properties: List[str]):
    return len(defined(obj.get(prop) for prop in properties)) == 1
