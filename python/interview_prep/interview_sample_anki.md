## When processing intraday trade feeds, how would you choose between Python lists, tuples, and arrays for storing price snapshots?

* Lists are the most flexible mutable containers, tuples are immutable and hashable so they fit keys/cached records, while `array`/NumPy arrays provide contiguous numeric storage and vectorized math.
* For millions of price points I prefer NumPy arrays for cache-friendly math;
* lists serve better for heterogeneous records and tuples for dictionary keys or ensuring snapshots are read-only.


## Explain Python's data model around `__iter__` and `__next__` and how it helps when streaming executions from a broker.

* An object is iterable if it implements `__iter__` returning an iterator; the iterator implements `__next__` to produce successive items and raises `StopIteration` to end the stream.
* This lets me wrap a socket feed in a custom iterator so any consumer (for loops, comprehensions, `itertools`) can treat the broker data stream uniformly.