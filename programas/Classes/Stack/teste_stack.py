from stack import Stack

def main():
    stack = Stack()
    try:
        for i in range (0, 3):
            stack.push(i)
            print(stack.print_stack())
        for i in range (0, 3):
            print(stack.print_stack())
            stack.pop()
    except Exception:
        exit()
if __name__ == "__main__":
    main()
