import os

from agent.perceive import perceive
from agent.planner import plan
from agent.actions import act
from agent.observer import observe
from agent.logger import log_iteration
from agent.summarizer import generate_summary  # ✅ Added summarizer import
from config.settings import LOG_FILE, MAX_ITERATIONS, APP_NAME


def main():
    print("=" * 50)
    print(f"🤖 Welcome to {APP_NAME}")
    print("=" * 50)

    question = perceive()
    search_query = question  # ✅ Initialize search_query with the original question

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    max_iterations = MAX_ITERATIONS
    iteration = 1
    success = False

    while iteration <= max_iterations and not success:

        print(f"\n========== Iteration {iteration} ==========\n")

        thought, plan_result = plan(question)

        # ✅ act() now returns (page_content, source_url)
        page_content, source_url = act(search_query)

        # ✅ Keep original question for observation, pass page_content
        success, observation = observe(question, page_content)

        # ✅ Updated logging with page_content and source_url
        log_iteration(
            {
                "iteration": iteration,
                "question": question,
                "thought": thought,
                "plan": plan_result,
                "action": page_content,
                "source_url": source_url,
                "observation": observation,
                "success": success,
            }
        )

        if success:
            print("\n✅ Research Completed!")

            # ✅ Generate final summary
            final_answer = generate_summary(
                question,
                page_content,
                source_url
            )

            print("\n" + "=" * 50)
            print("📝 FINAL RESEARCH ANSWER")
            print("=" * 50)
            print(final_answer)

            break

        # ✅ Safely refine the search query based on observation
        if observation:
            search_query = observation
            print("\n❌ Not enough information. Trying again...")
            print(f"🔄 Refined search query: {search_query}")
        else:
            print("\n❌ Not enough information. Trying again...")
            print("🔄 Keeping the previous search query because the tool failed.")

        iteration += 1

    print("\n🏁 Agent Finished")


if __name__ == "__main__":
    main()