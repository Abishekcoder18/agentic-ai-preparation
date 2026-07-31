def perceive():
    question = input("🔍 Enter your research question: ")
    return question


def plan(question):
    print(f"\n🧠 Planning how to research: '{question}'")


def act():
    print("🛠️ Searching for information...")


def observe():
    print("📋 Checking if enough information was found...")


def main():
    print("=" * 50)
    print("🤖 Welcome to ResearchMind")
    print("=" * 50)

    question = perceive()

    print("\nStarting Agent Loop...\n")

    plan(question)
    act()
    observe()

    print("\n✅ Agent Finished")


if __name__ == "__main__":
    main()