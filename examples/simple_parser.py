from pydantic import BaseModel, Field
from quickparser import parser


@parser
class SimpleModel(BaseModel):
    """
    Example CLI for demonstration.
    """
    name: str
    age: int = Field(default=40)
    hobby: str | None
    employed: bool 


if __name__ == "__main__":
    args = SimpleModel.parse()
    print(args)
    for arg, val in vars(args).items():
        print(f"    {arg} of type {type(val).__name__}: {val}")

    # $ python examples/simple_parser.py --name John --employed
    # Namespace(name='John', age=40, hobby=None, employed=True)
    #     name of type str: John
    #     age of type int: 40
    #     hobby of type NoneType: None
    #     employed of type bool: True
