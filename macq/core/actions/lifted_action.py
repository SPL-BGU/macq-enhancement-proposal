from typing import List, Set

from ..signature_parameter import SignatureParameter
from ..fluents.parameter_bound_literal import ParameterBoundLiteral

class LiftedAction:

    name: str
    params: List[SignatureParameter]
    positive_preconditions: Set[ParameterBoundLiteral]
    negative_preconditions: Set[ParameterBoundLiteral] | None
    add_effects: Set[ParameterBoundLiteral]
    delete_effects: Set[ParameterBoundLiteral]


    def __init__(self, name: str, params: List[SignatureParameter]):
        self.positive_preconditions = set()
        self.negative_preconditions = None
        self.add_effects = set()
        self.delete_effects = set()
        self.name = name
        self.params = params

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError