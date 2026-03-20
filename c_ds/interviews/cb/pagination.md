# software engineer
Problem C — Design and implement a pagination utility

Design an interface and implement a pagination helper over an in-memory collection.
Requirements
Input: a list/array of items (you can assume strings or objects with id ).
Support pageSize and returning items page-by-page.
Your design should specify function/class signatures (e.g., getPage(pageNumber) , or cursor-based next(cursor) returning (items, nextCursor) ), including inputs/outputs.
Constraints / considerations
Handle edge cases (empty list, last page, invalid page token).
Discuss tradeoffs between offset-based pagination and cursor-based pagination.
If you choose cursor-based pagination, define how the cursor is generated and validated.
