## N
## Idea, approach and time complexity:
'''
The `BrowserHistory` class is designed to emulate a browser's navigation history using a doubly linked list structure, where each node represents a webpage. The `Node` 
class facilitates the storage of each page's URL alongside pointers to the previous and next pages, allowing easy traversal in both directions. Upon initializing with a 
homepage, the `visit` method creates a new node for the URL being visited and updates the current node to this new page, effectively pushing it onto the navigation stack.
The `back` method allows users to navigate back through the history by moving the current node pointer to its previous node, decrementing the steps counter until either 
the desired number of steps is reached or the beginning of the history is hit. Conversely, the `forward` method does the same but in the opposite direction, allowing 
movement back towards the more recent pages. Each of these operations—visiting, going back, and moving forward—runs in O(1) time, as it involves simple pointer updates 
and condition checks. Thus, this design provides efficient navigation through a dynamic browser history while maintaining an intuitive structure for user interactions.
'''

class Node:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr=Node(homepage)

    def visit(self, url: str) -> None:
        self.curr.next=Node(url,self.curr)
        self.curr=self.curr.next

    def back(self, steps: int) -> str:
        while(self.curr.prev and steps>0):
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while(self.curr.next and steps>0):
            self.curr=self.curr.next
            steps-=1
        return self.curr.val