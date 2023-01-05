#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

names = dir(hidden_4)
for name in names:
    # don't print names starting with __
    if name[:2] != "__":
        print(name)
