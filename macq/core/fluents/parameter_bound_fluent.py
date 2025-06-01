from typing import List

from ..planning_object import  PlanningObject


class ParameterBoundFluent:
    """Represents a parameter bound literal often refered as a parameter bound fluent, which is a structural element often used in
    planning domains to describe state properties over objects and their
    relationships"""
    name: str
    bounded_params: List[int]

    def __init__(self, name: str, bounded_params: List[int]):
        self.name = name
        self.bounded_params = bounded_params

    def __str__(self):
        string = f"{self.name + ' '.join(map(str,self.bounded_params))}"
        return string

    # todo implement
    def ground(self, objects: List[PlanningObject]):
        ...
        # return Fluent(self.name, objects)