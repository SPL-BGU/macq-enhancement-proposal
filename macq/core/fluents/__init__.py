from typing import TypeVar

from .lifted_fluent import LiftedFluent
from .parameter_bound_literal import ParameterBoundLiteral
from .grounded_fluent import GroundedFluent

"""package containes core elements of an action model.
    enabling lifted, parameter-bound and grounded fluent representations"""

FluentType = TypeVar("FluentType", bound=GroundedFluent)
__all__ = [
    "LiftedFluent",
    "ParameterBoundLiteral",
    "GroundedFluent",
]