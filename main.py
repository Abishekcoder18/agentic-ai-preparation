import json
import os

LOG_FILE = "logs/agent_log.json"


def perceive():
    question = input("🔍 Enter your research question: ")
    return question


def plan(question):
    thought = f"I need to research '{question}' by searching reliable sources."
    print(f"🧠 Thought: {thought}")
    plan = "Search the web for relevant information"
    print(f"📌 Plan: {plan}")
    return thought, plan


def act():
    print("🛠️ Searching for information...")
    return "Search executed"


def observe():
    print("📋 Checking if enough information was found...")
    return False, "Information is still insufficient"


def log_iteration(log_data):
    os.makedirs("logs", exist_ok=True)
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    else:
        logs = []
    
    logs.append(log_data)
    
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)


def main():
    print("=" * 50)
    print("🤖 Welcome to ResearchMind")
    print("=" * 50)
    
    question = perceive()
    
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    
    max_iterations = 3
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