class Queue(object):
    """
    """
    def __init__(self):
        """
        """
        self.vals = []
        
    def insert(self, e):
        """
        insert an element in the queue
        """
        self.vals.append(e)
    
    def remove(self):
        """
        Remove an element for the queue, return an error if queue is empty
        """
        try:
            return self.vals.pop(0)
        except:
            raise ValueError()
        