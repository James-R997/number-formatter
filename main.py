from utils import prettify

def main():
    usernum = input("enter a number: ")

    pretty = prettify(usernum)

    print(f"\nprttify()-------> {pretty}\nstring format---> {int(usernum):,}\n")

if __name__ == "__main__":
    main()