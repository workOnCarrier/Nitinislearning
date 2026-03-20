Task 2: Generate NFT attribute combinations (and follow-ups)

You are given a set of NFT attributes, where each attribute category has a list of possible values.
Example input:
Background: ["Red", "Blue"]
Ears: ["Pointy", "Wide"]
Hat: ["Cap", "None"]
Part A: Enumerate all combinations
Generate all possible NFTs as combinations of choosing exactly one value from each category (i.e., the Cartesian product). Return the list of combinations.
Follow-up 1: Deduplication
If the input may contain duplicates (e.g., Ears: ["Pointy", "Pointy", "Wide"]) or different paths could create the same final combination, ensure the output contains unique combinations only.
Follow-up 2: Weighted/random generation
Now assume each value has an associated weight/probability (not necessarily uniform). Example:
Ears: Pointy=0.6, Wide=0.4
Design an algorithm to randomly generate an NFT (one combination) according to the specified weights per attribute category. Explain how you would implement the sampling step efficiently and how (if required) you would handle avoiding duplicates when generating many NFTs.
