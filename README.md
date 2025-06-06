Quickparser
===========

Create lightweight CLI arg parsers from pydantic models.

This provides a clean, declarative way to create a command-line interface by
allowing you to define the interface using Pydantic models.

For example,

```python
from pydantic import BaseModel, Field
from quickparser import parser

@parser
class SimpleModel(BaseModel):
    """
    Example CLI for demonstration.
    """
    name: str
    age: int = Field(default=30)
    hobby: str | None
    employed: bool

args = SimpleModel.parse()
```

Is the equivalent of the following argparse code:

```python
import argparse

parser = argparse.ArgumentParser(description="Example CLI for demonstration.")
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--age", type=int, default=30)
parser.add_argument("--hobby", type=str, default=None)
parser.add_argument("--employed", action="store_true")
args = parser.parse_args()
```


Installation
------------

```bash
pip install quickparser
```

Usage
-----

We can take the example above and put it into an `example.py` script to demonstrate the basic usage:

```python
# example.py
from pydantic import BaseModel, Field
from quickparser import parser


@parser
class SimpleModel(BaseModel):
    """
    Example CLI for demonstration.
    """
    name: str
    age: int = Field(default=30)
    hobby: str | None
    employed: bool

if __name__ == "__main__":
    args = SimpleModel.parse()
    print(args)
```

This script can be run from the command line, and it will parse the arguments provided to it. For example:

```bash
python example.py --name John --age 25 --hobby "reading" --employed
```
This will output:

```
SimpleModel(name='John', age=25, hobby='reading', employed=True)
```

Built on top of `argparse`, the parser provided automatically includes a help message,
type casting based on type hints, default values, and required vs optional arguments.
Help can be accessed by running the script with the `--help` flag:

```bash
python example.py --help
```
