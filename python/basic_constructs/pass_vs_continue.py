


def use_pass():
    pass

def use_continue():
    for index in range(4):
        pass
        print("before continue")
        if index % 2 == 0:
            continue
        print(f"after continue for {index}")

    
if __name__ == "__main__":
    use_pass()
    use_continue()