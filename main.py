import os

from agent.perceive import perceive
from agent.planner import plan
from agent.actions import act
from agent.observer import observe
from agent.logger import log_iteration
from config.settings import LOG_FILE, MAX_ITERATIONS, APP_NAME


def main():
    print("=" * 50)
    print(f"🤖 Welcome to {APP_NAME}")
    print("=" * 50)

    question = perceive()

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    max_iterations = MAX_ITERATIONS
    iteration = 1
    success = False

    while iteration <= max_iterations and not success:

        print(f"\n========== Iteration {iteration} ==========\n")

        thought, plan_result = plan(question)

        action_result = act()

        success, observation = observe()

        log_iteration(
            {
                "iteration": iteration,
                "question": question,
                "thought": thought,
                "plan": plan_result,
                "action": action_result,
                "observation": observation,
                "success": success,
            }
        )

        if success:
            print("\n✅ Research Completed!")
            break

        print("\n❌ Not enough information. Trying again...")

        iteration += 1

    print("\n🏁 Agent Finished")


if __name__ == "__main__":
    main()