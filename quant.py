import time, sys, random, os

def slowprint(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(task, duration=2.5):
    bar_len = 30
    slowprint(f"[BOOT] {task}")
    for i in range(bar_len + 1):
        filled = "█" * i
        empty = "░" * (bar_len - i)
        percent = (i / bar_len) * 100
        sys.stdout.write(f"\r[{filled}{empty}] {percent:5.1f}%")
        sys.stdout.flush()
        time.sleep(duration / bar_len)
    print("\n")

def divider():
    print("─" * 70)

os.system("clear" if os.name == "posix" else "cls")
divider()
slowprint("▶ INITIALIZING QUANT CORE SYSTEM v9.42 …")
divider()

loading_bar("Loading covariance matrix kernels …")
loading_bar("Encrypting proprietary alpha streams …")
loading_bar("Deploying neural-genetic optimizer …")

slowprint("[AUTH] User detected: OUTSIDER", 0.05)
time.sleep(0.7)
slowprint("[ACCESS] Quant Knowledge Repository: CLASSIFIED 🔒", 0.05)
divider()

slowprint(">>> ACCESS REQUEST: open_source_protocols.py", 0.04)
time.sleep(1)
slowprint(">>> RESPONSE: ⛔ DENIED", 0.04)
slowprint("Reason: Intellectual Alpha reserves under NDA §∞", 0.04)
divider()

time.sleep(0.5)
slowprint("LOADING REASONS…", 0.05)
reasons = [
    "→ Reinforcement signals proprietary",
    "→ Regime filters classified",
    "→ Kalman covariance self-learning — PRIVATE",
    "→ Genetic optimizer locked in secure enclave",
]
for r in reasons:
    slowprint(r, 0.05)
    time.sleep(0.3)
divider()

loading_bar("Encrypting source code in 2048-bit lattice shell …", 2)
loading_bar("Obfuscating alpha decay parameters …", 1.8)
loading_bar("Deploying decoy repo: “open_source_is_love.zip” (0 KB)", 1.2)

divider()
slowprint("██████████████████████████████████████████████████████████████", 0.002)
slowprint("   💾  PRIVATE RESEARCH VAULT SEALED  💾", 0.01)
slowprint("██████████████████████████████████████████████████████████████", 0.002)
divider()

slowprint('> echo "Sorry, no leaks today."', 0.05)
slowprint('> ./quant_mind --mode=stealth --share=FALSE', 0.05)
time.sleep(0.5)
slowprint("[LOG]  Proprietary intellect secured.", 0.04)
slowprint("[LOG]  All requests for “open source” redirected to /dev/null.", 0.04)
divider()
time.sleep(0.5)

banner = """
       ░░░   ACCESS DENIED: ALPHA IS A PRIVILEGE   ░░░
──────────────────────────────────────────────────────────────
"""
slowprint(banner, 0.002)

slowprint("System will auto-lock in 3...", 0.07)
time.sleep(0.7)
slowprint("2...", 0.6)
slowprint("1...", 0.6)
slowprint("Vault sealed.", 0.05)
divider()
slowprint("Session terminated.", 0.05)
