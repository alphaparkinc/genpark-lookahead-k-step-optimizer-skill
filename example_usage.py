import sys
from client import LookaheadOptimizer

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def run():
    print(">>> Demonstrating Lookahead Optimizer...")
    lh = LookaheadOptimizer(k=3, alpha=0.5)
    lh.init_param(0, 10.0)

    # Step 1 & 2: Fast weights advance
    w1 = lh.step(9.0)
    assert w1 == 9.0
    w2 = lh.step(8.0)
    assert w2 == 8.0

    # Step 3: Synchronization occurs
    # slow = 10.0 + 0.5 * (7.0 - 10.0) = 8.5
    w3 = lh.step(7.0)
    print(f"Step 3 synchronized weight: {w3}")
    assert w3 == 8.5
    print("[PASS] Lookahead Optimizer verified.")

if __name__ == "__main__":
    run()
