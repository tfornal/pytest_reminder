def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

t = Task()
print(t)
