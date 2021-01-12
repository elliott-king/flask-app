import time


def main():
    for i in range(60):
        print(f'Waiting... ({i + 1}/60)')
        time.sleep(1)


if __name__ == "__main__":
    main()
