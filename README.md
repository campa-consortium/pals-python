# Meet Your Python PALS

This is a Python implementation for the Particle Accelerator Lattice Standard ([PALS](https://github.com/campa-consortium/pals)).

To define the PALS schema, [Pydantic](https://docs.pydantic.dev) is used to map to Python objects, perform automatic validation, and serialize/deserialize data classes to/from many modern file formats.
Various modern file formats (e.g., YAML, JSON, TOML, XML, etc.) are supported, which makes the implementation of the schema-following files in any modern programming language easy (e.g., Python, Julia, C++, LUA, Javascript, etc.).
Here, we do Python.


## Status

This project is a work-in-progress and evolves alongside the Particle Accelerator Lattice Standard ([PALS](https://github.com/campa-consortium/pals)).


## Approach

This project implements the PALS schema in a file-agnostic way, mirrored in data objects.
The corresponding serialized files (and optionally, also the corresponding Python objects) can be human-written, human-read, and automatically validated.

PALS files follow a schema and readers can error out on issues.
Not every PALS implementation needs to be as detailed as this reference implementation in Python.
Nonetheless, you can use this implementation to convert between differnt file formats or to validate a file before reading it with your favorite YAML/JSON/TOML/XML/... library in your programming language of choice.

This will enable us to:
- exchange lattices between codes;
- use common GUIs for defining lattices;
- use common lattice visualization tools (2D, 3D, etc.).


### FAQ

*Why use Pydantic for this implementation?*  
Implementing directly against a specific file format is possible, but cumbersome.
By using a widely-used schema engine, such as [Pydantic](https://docs.pydantic.dev), we can get serialization/deserialization to/from various file formats, conversion, and validation "for free".


## Roadmap

Preliminary roadmap:

1. Define the PALS schema, using Pydantic.
2. Document the API.
3. Reference implementation in Python.
3.1. Attract additional reference implementations in other languages.
4. Add supporting helpers, which can import existing MAD-X, Elegant, SXF files.  
4.1. Try to be as feature complete as possible in these importers.
5. Reuse the reference implementations and implement readers in community codes for beamline modeling (e.g., the [BLAST codes](https://blast.lbl.gov)).


## How to run the tests and examples locally

In order to run the tests and examples locally, please follow these steps:

1. Create a conda environment from the `environment.yml` file:
    ```bash
    conda env create -f environment.yml
    ```
2. Activate the conda environment:
    ```bash
    conda activate pals-python
    ```
   Please double check the environment name in the `environment.yml` file.
3. Run the tests locally:
    ```bash
    pytest tests -v
    ```
   The command line option `-v` increases the verbosity of the output.
   You can also use the command line option `-s` to display any test output directly in the console (useful for debugging).
   Please refer to [pytest's documentation](https://docs.pytest.org/en/stable/) for further details on the available command line options and/or run `pytest --help`.
4. Run the examples locally (e.g., `fodo.py`):
    ```bash
    python examples/fodo.py
    ```
