## What is a Virtual Environment

Virtual environments are meant to keep things isolated from each other.

For example, let's say you are working on two different projects and both of them require different versions of the same package. In this case, you can create two different virtual environments for the two projects and install the required packages in the respective environments.

## How to create a Virtual Environment

You can create two different virtual environments for the two projects.. For project1:

```python
python3 -m venv ./venv1
source ./venv1/bin/activate
```

And both the environments can have different/same packages installed. For example, let's say you installed `numpy` and `pandas` in `venv1` and `numpy` and `matplotlib` in `venv2`
