# software engineer
You are asked to implement an in-memory Recipe Management System (similar in difficulty to a simple banking/in-memory DB exercise). The system supports incremental feature “levels”. Design the data structures and implement the required APIs.
Data model

Assume each Recipe has at least:
recipeId (unique string or integer)
name (string)
size (integer; used only for sorting)
Assume each User has at least:
userId (unique)
userName
No persistence is required (everything is in memory).
Level 1: Basic CRUD for recipes

Implement the following operations:
addRecipe(recipe) : add a new recipe (reject or overwrite if recipeId already exists—state your choice clearly).
updateRecipe(recipeId, fields...) : update an existing recipe.
getRecipe(recipeId) : return the recipe or “not found”.
deleteRecipe(recipeId) : delete an existing recipe.
Define expected behavior for edge cases (e.g., updating/deleting a non-existent recipe).
Level 2: Search and list

Implement:
searchRecipes(query) : search recipes by name , case-insensitive (define whether it’s exact match or substring match; choose one and be consistent).
listRecipes(sortBy) : return all recipes sorted by either:
name (lexicographic, case-insensitive), or
size (numeric ascending)
Specify tie-breaker behavior (e.g., tie-break by recipeId).
Level 3: Add user

Implement:
addUser(user) : add a user (keep it simple—no extra features unless needed).
Define behavior on duplicate userId.
Level 4: Version history and rollback

Add versioning to support:
versionHistory() : return stored version metadata (at minimum, a monotonic versionId and what changed).
rollback(versionId) : restore the system state to exactly how it was at that versionId .
Guidance: treat each mutating operation (e.g., add/update/delete recipe, add user) as producing a new version; maintain whatever additional structures you need (e.g., a versionMap).
Constraints / expectations

Assume up to ~100k recipes/users.
Aim for clean APIs and reasonable time complexity.
You may implement this as a class/module with methods in your preferred language.