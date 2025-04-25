from typing import TypeVar, Generic
import argparse
from pydantic import BaseModel, Field
from pydantic_core import PydanticUndefinedType

T = TypeVar('T', bound=type[BaseModel])


class Parser(Generic[T]):

    _model: T = None

    @classmethod
    def _init_parser(cls, model: T) -> argparse.ArgumentParser:
        """
        Initialize the argument parser.
        """
        parser = argparse.ArgumentParser(description=model.__doc__)
        for field_name, field in model.model_fields.items():
            _type = None
            # Check annotation to see if field is optional
            is_optional = _field_is_optional(field)
            if is_optional:
                _type = field.annotation.__args__[0]
            else:
                if isinstance(field.annotation, type):
                    _type = field.annotation
                else:
                    _type = None
            default = field.default
            if isinstance(default, PydanticUndefinedType):
                is_optional = True
                default = None
            elif default:
                is_optional = True
            parser.add_argument(
                f'--{field_name}',
                type=_type,
                default=default,
                required=(True if not is_optional else None),
                help=field.description or ''
            )
        return parser

    @classmethod
    def parse(cls):
        """
        Parse the command line arguments.
        """
        parser = cls._init_parser(cls._model)
        return parser.parse_args()


def parser(cls: T) -> Parser[T]:
    """
    Decorator to create a parser for a Pydantic model.
    """
    name = cls.__name__
    return type(name, (Parser,), {
        '_model': cls,
        '__doc__': cls.__doc__,
        '__module__': cls.__module__,
    })


def _field_is_optional(field: Field) -> bool:
    """
    Check if a field is optional.
    """
    return (
        field.annotation is not None and 
        hasattr(field.annotation, '__origin__') and
        field.annotation.__origin__ is Union and
        type(None) in field.annotation.__args__
    )