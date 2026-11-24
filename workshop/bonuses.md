# Optional island puzzles

These four puzzles are unscored. Run them from your workshop clone whenever you like.

## Top explorer

Use `python3 fieldkit/explorer.py "SELECT ..."`. Inspect the tables in `fieldkit/data/explorers.sql`, join each explorer to their assessment scores and find the highest total. Who leads the expedition?

## The final journal entry

Use the same query runner to find the winning explorer’s most recent journal entry. Use the observation timestamp to identify it.

## Island hopping

Read the `islands` coordinate pairs in `fieldkit/data/chart.json`. Each unit is a kilometer. Calculate the Euclidean distance between the first two stops and round once to the nearest kilometer.

## The traveling sailor

Visit all six stops exactly once. You can start and finish anywhere. Find the shortest open route using the same coordinates, adding unrounded distances and rounding only the final sum. You can check every ordering with Python’s `itertools.permutations`.
