from PIL import Image


def main() -> None:
    print("Hello, World!")

    image = Image.open("img.png")
    print(image.size)
    print(1)
    print(int(input()) / 2)

    print(input() * 10)

    print("aboba")



if __name__ == '__main__':
    main()
