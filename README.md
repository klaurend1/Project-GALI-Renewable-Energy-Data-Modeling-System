# Project GALI: Renewable Energy Data Modeling System

A Python based simulation that converts sunlight intensity readings into digital tokens, demonstrating how renewable energy can be quantified and recorded using blockchain inspired logic.

## How It Works
- Generates random sunlight intensity values (0–1000)
- Converts each reading into tokens using the formula:
tokens = intensity / 100

Copy code
- Saves all readings and token values in a CSV file named `ledger.csv`

## How to Run
1. Clone this repository:
 ```bash
 git clone https://github.com/klaurend1/Project-GALI-Renewable-Energy-Data-Modeling-System.git
 cd Project-GALI-Renewable-Energy-Data-Modeling-System

//Run the simulation:
Copy code
python3 main.py
View results in the terminal and open ledger.csv to see recorded data.
```
## Example Output
Copy code
```bash
Simulated Solar Tokenizer Starting...

[17:25:41] Intensity: 876 → Minted: 8.76 ST | Total: 8.76
[17:25:42] Intensity: 542 → Minted: 5.42 ST | Total: 14.18

Simulation complete! Data saved to ledger.csv.
```
```
```
## Future Work
-Replace simulated values with real data from an Arduino solar cell.
- Connect to a blockchain for verified energy tokenization.

## Author
Keith Laurendine

## License
MIT License
