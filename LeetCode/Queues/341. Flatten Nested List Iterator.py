from collections import deque



class NestedIterator:
    def __init__(self, nestedList):
        self.dq=deque()
        self.dq.extend(nestedList)



    def next(self) -> int:

        element= self.dq.popleft()

        if element.isInteger():
            return element
        else:
            self.extendTheDqToLeft(element)

        return self.dq.popleft()


    def hasNext(self) -> bool:
        return len(self.dq) > 0

    def extendTheDqToLeft(self, element):
        element=element.getList()
        for elem in reversed(element):
            if elem.isInteger():
                self.dq.appendleft(elem)
            else:
                self.extendTheDqToLeft(elem)