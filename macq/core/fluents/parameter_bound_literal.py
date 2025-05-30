from typing import List

from ..planning_object import  PlanningObject


class ParameterBoundLiteral:
    """Represents a parameter bound literal often refered as a parameter bound fluent, which is a structural element often used in
    planning domains to describe state properties over objects and their
    relationships"""
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
        pass
        # return Fluent(self.name, objects)