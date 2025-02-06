# Meet Your Python PALS

This is a Python implementation for the Particle Accelerator Lattice Standard (PALS).

To define the PALS schema, [Pydantic](https://docs.pydantic.dev) is used to map to Python objects, perform automatic validation, and to (de)serialize data classes to/from many modern file formats.
Various modern file formats (e.g., YAML, JSON, TOML, XML, ...) are supported, which makes implementation of the schema-following creates files in any modern programming language easy (e.g., Python, Julia, LUA, C++, Javascript, ...).
Here, we do Python.


## Status

This project is a work-in-progress and evolves alongside the Particle Accelerator Lattice Standard (PALS) documents.


## Approach

This project implements the PALS schema in a file agnostic way, mirrored in data objects.
The corresponding serialized files (and optionally, also the corresponding Python objects) can be human-written, human-read, and automatically be validated.

PALS files follow a schema and readers can error out on issues.
Not every PALS implementation needs to be as detailed as this reference implementation in Python.
Nonetheless, you can use this implementation to convert between differnt file formats (see above) or to validate a file before reading it with your favorite YAML/JSON/TOML/XML/... library in your programming language of choice.

So let's go, let us use the element descriptions we love and do not spend time anymore on parsing differences between code conventions.

This will enable us to:
- exchange lattices between codes
- use common GUIs for defining lattices
- use common lattice visualization tools (2D, 3D, etc.)


### FAQ

*Why do you use Pydantic for this implementation?*  
Implementing directly against a specific file format is possible, but cumbersome.
By using widely-used schema engine, we can get the "last" part, serialization and deserialization to various file formats (and converting between them, and validating them) for free.


## Roadmap

Preliminary roadmap:

1. Define the PALS schema, using Pydantic  
2. Document the API well.
3. Reference implementation in Python  
3.1. attract additional reference implementations in other languages.
4. Add supporting helpers, which can import existing MAD-X, Elegant, SXF files.  
4.1. Try to be pretty feature complete in these importers (yeah, hard).
5. Implement readers in active community codes for beamline modeling.
   Reuse the reference implementations: e.g., we will use this project for the [BLAST codes](https://blast.lbl.gov).


## Examples

### YAML

```yaml
line:
- ds: 1.0
  element: drift
  nslice: 1
- ds: 0.5
  element: sbend
  nslice: 1
  rc: 5.0
- ds: 0.0
  element: marker
  name: midpoint
- line:
  - ds: 1.0
    element: drift
    nslice: 1
  - ds: 0.0
    element: marker
    name: otherpoint
  - ds: 0.5
    element: sbend
    name: special-bend
    nslice: 1
    rc: 5.0
  - ds: 0.5
    element: sbend
    nslice: 1
    rc: 5.0
```

### JSON

```json
{
    "line": [
        {
            "ds": 1.0,
            "element": "drift",
            "nslice": 1
        },
        {
            "ds": 0.5,
            "element": "sbend",
            "nslice": 1,
            "rc": 5.0
        },
        {
            "ds": 0.0,
            "element": "marker",
            "name": "midpoint"
        },
        {
            "line": [
                {
                    "ds": 1.0,
                    "element": "drift",
                    "nslice": 1
                },
                {
                    "ds": 0.0,
                    "element": "marker",
                    "name": "otherpoint"
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "name": "special-bend",
                    "nslice": 1,
                    "rc": 5.0
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "nslice": 1,
                    "rc": 5.0
                }
            ]
        }
    ]
}
```

### Python Dictionary

```py
{
    "line": [
        {
            "ds": 1.0,
            "element": "drift",
            "nslice": 1
        },
        {
            "ds": 0.5,
            "element": "sbend",
            "nslice": 1,
            "rc": 5.0
        },
        {
            "ds": 0.0,
            "element": "marker",
            "name": "midpoint"
        },
        {
            "line": [
                {
                    "ds": 1.0,
                    "element": "drift",
                    "nslice": 1
                },
                {
                    "ds": 0.0,
                    "element": "marker",
                    "name": "otherpoint"
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "name": "special-bend",
                    "nslice": 1,
                    "rc": 5.0
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "nslice": 1,
                    "rc": 5.0
                }
            ]
        }
    ]
}
```

### Python Dataclass Objects

```py
line=[
    Drift(name=None, ds=1.0, nslice=1, element='drift'),
    SBend(name=None, ds=0.5, nslice=1, element='sbend', rc=5.0),
    Marker(name='midpoint', ds=0.0, element='marker'),
    Line(line=[
        Drift(name=None, ds=1.0, nslice=1, element='drift'),
        Marker(name='otherpoint', ds=0.0, element='marker'),
        SBend(name='special-bend', ds=0.5, nslice=1, element='sbend', rc=5.0),
        SBend(name=None, ds=0.5, nslice=1, element='sbend', rc=5.0)
    ])
]
```
