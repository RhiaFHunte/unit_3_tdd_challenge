def check_for_todo(task):
    if not isinstance(task, str):
        raise Exception("Value must be a string!")
    if task == "":
        raise Exception("String cant be empty!")
    return "#TODO" in task

