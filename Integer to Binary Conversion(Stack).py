class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
def convert_int_to_bin(dec_num):
  if dec_num==0:
    return 0
  s=Stack()
  while dec_num>0:
    remainder=dec_num%2
    s.push(remainder)
    dec_num//=2
  binnum=""
  while not s.is_empty():
    binnum+=str(s.pop())
  return int(binnum)

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(convert_int_to_bin(9))
