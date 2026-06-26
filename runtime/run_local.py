from rcsk.core.kernel import CognitiveSwarmKernel

def main():
    kernel = CognitiveSwarmKernel()
    print("🚀 RCSK v3 Kernel Started")
    
    intents = [
        "Analyze market trends for AI agents",
        "Design a self-improving memory system",
        "Simulate swarm coordination"
    ]
    
    for intent in intents:
        print(f"\nIntent: {intent}")
        result = kernel.step(intent)
        print(f"Result: {result.get('status', 'done')}")
    
    # Show observability
    print("\nRecent Events:")
    for event in kernel.get_ledger().get_recent(5):
        print(f"  [{event.timestamp:.2f}] {event.event_type}")

if __name__ == "__main__":
    main()
