Virtual environments are meant to keep things isolated from each other.

- If one project is a dependency of the other one, then they have to be installed in the same environment.
- If two projects have dependencies that conflict with each other, then they have to be installed in different environments.
- If two projects are meant to be run on different versions of the Python interpreter, then they have to be installed in different environments.

That's basically the rules (I can think of). And then the rest is a mix of best practices, personal opinions, common sense, technical limitations, and so on.

> [!NOTE]
>
> - You don't need to create a virtual environment every time You start a new project.

You can create two different virtual environments for the two projects.. For project1:

```python
python3 -m venv ./venv1
source ./venv1/bin/activate
```

For project2:

```python
python3 -m venv ./venv2
source ./venv2/bin/activate
```

And both the environments can have different/same packages installed. For example, let's say you installed `numpy` and `pandas` in `venv1` and `numpy` and `matplotlib` in `venv2`
