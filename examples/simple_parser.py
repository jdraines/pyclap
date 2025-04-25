from pydantic import BaseModel, Field
from pyclap import parser


@parser
class SimpleModel(BaseModel):
    """
    Example model for demonstration.
    """
    name: str
    age: int = Field(default=30)
    hobby: str | None


if __name__ == "__main__":
    args = SimpleModel.parse()
    print(args)
    for arg, val in vars(args).items():
        print(f"    {arg} of type {type(val).__name__}: {val}")
