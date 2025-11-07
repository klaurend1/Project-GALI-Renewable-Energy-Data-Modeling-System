import time, random, csv
from datetime import datetime

TOTAL_TOKENS = 0
CSV_FILE = "ledger.csv"

with open(CSV_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "intensity", "tokens_minted", "total_tokens"])

print("Simulated Solar Tokenizer Starting...\n")

for i in range(10):
    intensity = random.randint(100, 1000)
    tokens = round(intensity / 100, 2)
    TOTAL_TOKENS += tokens
    timestamp = datetime.now().strftime("%H:%M:%S")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, intensity, tokens, TOTAL_TOKENS])

    print(f"[{timestamp}] Intensity: {intensity} → Minted: {tokens} ST | Total: {TOTAL_TOKENS}")
    time.sleep(1)

print("\n✅ Simulation complete! Data saved to ledger.csv")
