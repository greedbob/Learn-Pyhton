from collections import deque


def search(name, graph, seller):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == seller:
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
