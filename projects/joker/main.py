from joker import Joker


def prompt_for_topic():
    while True:
        topic = input("Enter the topic to tell a joke about: ").strip().lower()
        if not topic:
            print("Please enter a valid topic.")
            continue
        print(f"Selected topic: {topic}")
        return topic


def main():
    topic = prompt_for_topic()
    print(f"Generating a joke about: {topic}")
    joker = Joker(topic)
    joker.tell_a_joke()

if __name__ == "__main__":
    main()
