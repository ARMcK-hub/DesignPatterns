from typing import Any, Tuple


class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> None:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        elif any([len(args) != 0, len(kwargs) != 0]):
            raise SingletonConstructionError(cls.__name__, args)
        return cls._instances[cls]


class SingletonConstructionError(Exception):
    def __init__(self, class_name: str, *args: Tuple) -> None:
        msg = f"""
        Illegal Singleton Construction:
            Attempted to construct instance of {class_name} where one already exists.
            Existing instances should be called without constructor arguments.
            Modification of existing instances should be managed through non-constructing methods.
            Illegal (args, kwargs): {args}"""
        super().__init__(msg)
