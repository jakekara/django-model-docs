# Generate docs for django models

## Dev quick start

```shell
# set up a virtual env however you like. here's what I like:
python -m venv venv 
. ./venv bin activate

# set up dev stuff
pip install -r requirements.txt

# install the package in editable mode
pip install -e .

# generate docs for model(s) in the demo app
cd demo_django_project
python manage.py generate_model_docs demo_django_app -o out.md
```

The `out.md` looks like this at the moment:

```markdown
# `demo_django_app`` app`

_This file was auto-generated Django Model Docs Generator.  Do not edit this file directly._

None

## `person` model

Person(id, first_name, last_name)

|    Field   |Description|  Data type |Nullable|Default|
|------------|-----------|------------|--------|-------|
|    `id`    |           |BigAutoField|  False |   -   |
|`first_name`|           |  CharField |  False |   -   |
| `last_name`|           |  CharField |  False |   -   |


```