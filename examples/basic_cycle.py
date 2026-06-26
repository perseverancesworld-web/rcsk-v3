from rcsk.core.kernel import CognitiveSwarmKernel

if __name__ == "__main__":
    kernel = CognitiveSwarmKernel()
    result = kernel.step("Test cognitive cycle")
    print("Basic cycle completed:", result)
