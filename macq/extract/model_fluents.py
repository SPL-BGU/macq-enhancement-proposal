from typing import List
from .signature_parameter import SignatureParameter
from macq.trace.fluent import PlanningObject, Fluent

# use the grounded prefix over the fluent class name to simplify the
# meaning when a new contributor needs to understand different fluent classes.


class LiftedFluent:
    """Represents a lifted fluent, which is a structural element often used in
    planning domains to describe state properties over objects and their
    relationships.

    A lifted fluent is characterized by its name and parameters. It can be
    hashed, printed as a string, or compared with other instances based on
    its name and parameters.

    Attributes:
        name (str): The name of the lifted fluent, indicating its identity
            in the planning domain.
        parameters (List[SignatureParameter]): A list of parameters that
            define the schema of the lifted fluent.
    """
    name: str
    parameters: List[SignatureParameter]

    def __init__(self, name: str, parameters: List[SignatureParameter]):
        self.name = name
        self.parameters = parameters

    def __hash__(self):
        return hash(self.name) + hash(tuple(self.parameters))

    def __str__(self):
        return self.name + ' '.join(map(str,self.parameters))

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, LiftedFluent) and hash(self) == hash(other)


    

class ParameterBoundLiteral:
    name: str
    bounded_params: List[str]

    def __init__(self,
                 name: str,
                 bounded_params: List[str]):
        
        self.name = name
        self.bounded_params = bounded_params


    def __str__(self):
        string = f"({self.name + ' '.join(self.bounded_params)})"
        return string

    def ground(self, objects: List[PlanningObject]):
        return Fluent(self.name, objects)


class GroundedFluent:

    name: str
    objects: List[PlanningObject]

    def __init__(self, name: str, objects: List[PlanningObject]):
        self.name = name
        self.objects = objects
