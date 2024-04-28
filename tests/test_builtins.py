from typing import Any, List, Optional, Set, Tuple, Union

import pytest

from stinky.noodle.utils.builtins import alphabetical, enumeration, falsy, length


@pytest.mark.parametrize(
    ("input_obj", "keyed_by", "result"),
    [
        (["a", "c", "b"], None, False),
        (["a", "b", "c"], None, True),
        (
            [
                {"key": 1, "val": "a"},
                {"key": 3, "val": "c"},
                {"key": 2, "val": "b"},
            ],
            "key",
            False,
        ),
        (
            [
                {"key": 1, "val": "a"},
                {"key": 3, "val": "b"},
                {"key": 2, "val": "c"},
            ],
            "val",
            True,
        ),
    ],
)
def test_builtins_alphabetical(input_obj: Any, keyed_by: Optional[str], result: bool):
    """Test the alphabetical builtin"""
    assert alphabetical(obj=input_obj, keyed_by=keyed_by) is result


@pytest.mark.parametrize(
    ("obj", "values", "result"),
    [
        (
            "a",
            (
                "a",
                "b",
            ),
            True,
        ),
        (
            "c",
            (
                "a",
                "b",
            ),
            False,
        ),
        (
            "a",
            {
                "a",
                "b",
            },
            True,
        ),
        (
            "c",
            {
                "a",
                "b",
            },
            False,
        ),
        ("a", [], False),
        ("c", [], False),
    ],
)
def test_builtins_enumeration(obj: Any, values: Union[Set, List, Tuple], result: bool):
    """Test the enumeration builtin"""
    assert enumeration(obj=obj, values=values) is result


@pytest.mark.parametrize(
    ("obj", "result"),
    [
        (False, True),
        (0, True),
        (1, False),
        ("anything", False),
    ],
)
def test_builtins_falsy(obj: Any, result: bool):
    """Test the falsy builtin"""
    assert falsy(obj=obj) is result


@pytest.mark.parametrize(
    ("obj", "min_arg", "max_arg", "result"),
    [
        ("", 0, 0, False),
        ("", 0, 1, True),
        ("", 2, 4, False),
        ("a", 0, 1, False),
        ("a", 1, 2, True),
    ],
)
def test_builtins_length(obj: Any, min_arg: int, max_arg: int, result: bool):
    """Test the length builtin"""
    assert length(obj=obj, min=min_arg, max=max_arg) is result
