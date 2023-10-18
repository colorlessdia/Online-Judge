def solution(todo_list, finished):
    return [todo for todo, b in zip(todo_list, finished) if not b]