from typing import Any, Callable
from dataclasses import dataclass, field


@dataclass
class Pipeline:
    name: str
    module: Any
    transform: Callable[[list[dict]], list[dict]]
    schema: list[dict]
    options: dict = field(default_factory=dict)
