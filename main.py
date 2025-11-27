from PIL import Image


def main() -> None:
    print("Hello, World!")

    image = Image.open("img.png")
    print(image.size)


if __name__ == '__main__':
    main()
