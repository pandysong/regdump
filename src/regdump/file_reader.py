import queue
# the generator which support a queue
# so that we could put a line back to generator so that next yiled will
# be able to generate the data which was put back to queue


def readline_from(fn, q, enc):
    """generator from a file
    it generates line by line, it also support put back an previously got line
    so that next call to 'next' will yield the line just put back
    """
    with open(fn, encoding=enc) as f:
        while True:
            if not q.empty():
                yield q.get()
            else:
                try:
                    yield next(f)
                except StopIteration:
                    # if the last data was put back
                    if not q.empty():
                        yield q.get()
                    break


def readlines(fn, enc):
    helper_queue = queue.Queue()
    lines = readline_from(fn, helper_queue, enc)
    return lines, helper_queue
