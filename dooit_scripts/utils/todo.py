from dooit.api import Todo

"""
Helper functions related to dooit's Todo object
"""


def filter_todos(todos: list[Todo], attr: str, value) -> list[Todo]:
    """
    Takes in a list of Todo objects, a Todo attribute/property,
    and the value it should be.

    Returns a list of the Todo objects that match the attribute value.

    The matching is case insensitive.
    """

    result = []

    # Sanitized string
    fmt_value = str(value).strip().lower()

    for todo in todos:
        todo_value = getattr(todo, attr)
        fmt_todo_value = str(todo_value).strip().lower()

        if fmt_todo_value == fmt_value:
            result.append(todo)

    return result


def recurse_todo(todo: Todo) -> list[Todo]:
    """
    Given a Todo object, checks if it has subtodos.
    If so, this function recurses for each subtodo.

    Returns a list with the input Todo and all descendant Todo objects.
    """

    result = [todo]

    if len(todo.todos) > 0:
        for child in todo.todos:
            result += recurse_todo(child)

    return result
