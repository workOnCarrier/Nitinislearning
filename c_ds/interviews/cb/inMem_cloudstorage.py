Problem

Implement an in-memory cloud storage service that supports multiple users, per-user storage quotas, changing quotas with eviction, and file compression/decompression.
You are given a list of queries. Each query is an array of strings where the first element is the operation name. Return an array of strings—one result per query.
Data model
Each user has:
a unique userId
an integer capacity (maximum total size of that user’s files)
zero or more files
Each file belongs to exactly one user and has:
fileName (string)
size (positive integer)
File names are unique per user .
Operations
All operations are scoped to a user unless stated otherwise.
1) ADD_USER userId capacity
Create a new user.
If userId already exists: return "false" .
Otherwise: create the user with the given capacity and return "true" .
2) ADD_FILE userId fileName size
Add a new file for a user.
If the user does not exist: return "false" .
If a file with that name already exists for the user: return "false" .
If adding the file would make the user’s total used size exceed the user’s capacity: return "false" .
Otherwise add the file and return "true" .
3) GET_FILE_SIZE userId fileName
Return the size of a file.
If the user or file does not exist: return "" (empty string).
Otherwise return the file size as a string.
4) UPDATE_CAPACITY userId newCapacity
Update a user’s capacity. If after the update the user is over capacity, you must delete existing files until the total used size is within capacity.
Eviction rule:
Repeatedly delete the user’s largest file.
If multiple files tie for largest size, delete the one with the lexicographically largest fileName to make the behavior deterministic.
Stop once total used size 
≤
≤ newCapacity .
Return:
If the user does not exist: return "-1" .
Otherwise return the number of files deleted (as a string). (If no deletion needed, return "0" .)
5) COMPRESS_FILE userId fileName
Compress an existing file.
Compression renames the file from fileName to fileName + ".compressed" .
The compressed file size becomes size / 2 using integer division .
Rules:
If user does not exist: return "false" .
If fileName does not exist: return "false" .
If fileName already ends with .compressed : return "false" .
If the target name fileName + ".compressed" already exists for that user: return "false" .
Otherwise perform the rename and size change and return "true" .
Note: Compression reduces used space, so it will never violate capacity.
6) DECOMPRESS_FILE userId compressedName
Decompress an existing compressed file.
Decompression renames compressedName to the original name by removing the .compressed suffix.
The decompressed file size becomes size * 2 .
Rules:
If user does not exist: return "false" .
If compressedName does not exist: return "false" .
If compressedName does not end with .compressed : return "false" .
Let originalName be compressedName with the final .compressed removed. If a file named originalName already exists: return "false" .
If decompressing would make the user exceed capacity: return "false" (and do not change anything).
Otherwise perform the rename and size change and return "true" .
Input/Output format
Input: queries , a list of string arrays.
Output: list of strings, one per query.
Constraints (you may assume)
Number of queries up to ~10^5.
File sizes and capacities fit in 32-bit signed integers.
userId and fileName are non-empty strings.
Example (illustrative)
Queries:
["ADD_USER","alice","10"] → "true"
["ADD_FILE","alice","a.txt","6"] → "true"
["COMPRESS_FILE","alice","a.txt"] → "true" (now a.txt.compressed size 3)
["DECOMPRESS_FILE","alice","a.txt.compressed"] → "true" (back to size 6)
["UPDATE_CAPACITY","alice","4"] → must delete largest files until used ≤ 4 return number deleted.