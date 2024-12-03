from dooit.api import Workspace, Todo
import formats as fmt


def parse_single_todo(todo: Todo, show_due: bool = True) -> str:
    """
    Takes in a dooit Todo object and returns a string in Markdown format.
    """

    indent = " " * (todo.nest_level * 4)
    checkbox = fmt.checkbox(todo)

    text = indent + checkbox + todo.description

    if show_due:
        due_date = fmt.due_date(todo.due)
        text += due_date

    return text


def parse_todo(todo: Todo) -> list[str]:
    """
    Takes in a dooit Todo object and formats it with parse_single_todo().

    If it has children, this function recurses and adds the children's
    lines to the output.
    """

    lines: list[str] = []

    parent = parse_single_todo(todo)
    lines.append(parent)

    if len(todo.todos) > 0:
        for child in todo.todos:
            lines += parse_todo(child)

    return lines


def parse_workspaces(
    workspaces: list[Workspace], index: int = 0, first: bool = True
) -> list[str]:
    """
    Iterates over a list of dooit Workspace objects.

    Returns a Markdown formatted heading and task list for each Workspace.
    """

    if index >= len(workspaces):
        return []

    ws = workspaces[index]

    lines = []

    # Only get workspaces with todos
    if len(ws.todos) > 0:
        heading = fmt.heading(ws.nest_level, ws.description)

        todo_lines: list[str] = []
        for i in ws.todos:
            todo_lines += parse_todo(i)

        if first:
            lines = [heading, ""] + todo_lines
        else:
            lines = ["", heading, ""] + todo_lines

    return lines + parse_workspaces(workspaces, index + 1, first=False)