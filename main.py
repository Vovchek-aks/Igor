from PIL import Image


def main() -> None:
    print("Hello, World!")

    total = 1 + 1
    print(total)

    image = Image.open("img.png")
    print(image.size)


if __name__ == '__main__':
    main()
