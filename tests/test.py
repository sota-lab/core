from typing import Dict
from dataclasses import dataclass, field

from sotalab.core import register


@register
@dataclass
class Test:
    s: str
    b: bool

    dict: Dict[str, float] = field(default_factory=dict)


def main():
    pass


if __name__ == "__main__":
    main()
