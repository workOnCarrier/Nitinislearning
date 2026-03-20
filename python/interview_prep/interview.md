## When processing intraday trade feeds, how would you choose between Python lists, tuples, and arrays for storing price snapshots?

* Lists are the most flexible mutable containers, tuples are immutable and hashable so they fit keys/cached records, while `array`/NumPy arrays provide contiguous numeric storage and vectorized math.
* For millions of price points I prefer NumPy arrays for cache-friendly math; lists serve better for heterogeneous records and tuples for dictionary keys or ensuring snapshots are read-only.


## Explain Python's data model around `__iter__` and `__next__` and how it helps when streaming executions from a broker.

* An object is iterable if it implements `__iter__` returning an iterator; the iterator implements `__next__` to produce successive items and raises `StopIteration` to end the stream.
* This lets me wrap a socket feed in a custom iterator so any consumer (for loops, comprehensions, `itertools`) can treat the broker data stream uniformly.


## Why are generator functions a good fit for cleansing tick data, and how do they differ from list comprehensions?

* Generators lazily yield values one by one without allocating the full collection, so they can filter/transform an endless tick stream with small memory footprint.
* List comprehensions build an entire list eagerly; generators produced with `yield` (or generator comprehensions) maintain state between yields and pause execution, ideal for streaming ETL.


## Describe how `yield from` simplifies working with nested market data generators.

* `yield from <subgen>` delegates iteration to another generator, propagating sent values, exceptions, and the return value.
* When composing multiple cleansing stages it avoids manual for-loops and preserves the inner generator's behavior, making pipeline stacking concise.


## What is the Global Interpreter Lock (GIL) and how does it influence leveraging threads for CPU-heavy risk analytics?

* CPython enforces a single executing bytecode thread via the GIL, so CPU-bound threads time-slice rather than run in parallel, limiting speedups.
* For compute-heavy analytics I'd use multiprocessing, native extensions, or Numba/Cython; threads remain useful for IO-bound tasks such as waiting on exchanges or databases.


## Contrast `threading`, `multiprocessing`, and `asyncio` for building a trade enrichment service.

* `threading` shares memory and is lightweight but blocked by the GIL for CPU work; it shines on IO waits.
* `multiprocessing` spawns separate processes with independent GILs, giving true parallelism at the cost of IPC overhead.
* `asyncio` is single-threaded cooperative scheduling using awaitables, so it's ideal when most work is awaiting network calls (e.g., reference data lookups) while keeping memory usage low.


## How do futures/executors (`concurrent.futures`) help batch-processing corporate action adjustments?

* Executors abstract thread or process pools with a simple submit/map API returning futures, so I can dispatch batch jobs, collect results as they complete, and handle exceptions centrally.
* It decouples scheduling from work functions, enabling CPU tasks to use `ProcessPoolExecutor` while IO tasks leverage `ThreadPoolExecutor`.


## Outline how you'd profile and optimize a slow Python loop that enriches client positions.

* First reproduce under `cProfile` or `pyinstrument` to find hot functions, then inspect algorithms and data structures.
* I might replace repeated lookups with dict caches, move heavy math to NumPy/pandas vectorization, eliminate Python-level loops via comprehensions, or use `functools.lru_cache` for deterministic reference data calls.
* Finally reprofile to confirm gains.


## What are `dataclasses`, and when would you prefer them over `namedtuple` or plain classes for trade objects?

* `dataclasses` auto-generate init/eq/ordering/repr methods for attribute declarations, support defaults, type hints, and mutability control.
* They're preferable when I need mutable trade records with validation hooks (`__post_init__`) or default factories.
* `namedtuple` is lightweight/immutable but lacks defaults; plain classes require manual boilerplate.


## Explain how descriptors power `@property` and why they matter for computed attributes such as delta exposure.

* Descriptors implement `__get__`, `__set__`, `__delete__` and live on the class; the attribute access protocol checks for descriptors and delegates.
* `@property` creates a descriptor wrapping getter/setter logic, enabling computed attributes that feel like fields.
* This keeps call sites clean (`trade.delta`) while encapsulating calculation logic and validation.


## Describe how `__slots__` helps when modeling millions of lightweight objects like fills.

* Declaring `__slots__` replaces per-instance `__dict__` with a static layout, shrinking memory and speeding attribute lookups.
* For massive homogeneous objects (fills) it's a clear win, though it removes dynamic attribute assignment and needs care with inheritance.


## When would you reach for `typing.Protocol` versus traditional abstract base classes in a pricing engine?

* `Protocol` (structural typing) defines required methods/attributes without inheritance, so any class matching the signature satisfies the type checker.
* It's ideal when I need duck-typed components (e.g., pricers from different teams).
* ABCs enforce nominal inheritance and can register virtual subclasses; they're useful when runtime checks or shared mixins are needed.


## Give an example of using `functools.singledispatch` in an equity swaps allocation tool.

* `@singledispatch` lets me write a generic `serialize(position)` function and register type-specific implementations for `EquitySwap`, `CashPosition`, etc.
* When the allocator emits mixed instrument objects we get clean extensibility without modifying core logic.


## How does `functools.lru_cache` aid pricing repeated what-if scenarios, and what caveats exist?

* It memoizes pure function outputs keyed by arguments, so recalculating identical what-if requests is O(1).
* Caveats: inputs must be hashable, cached values persist (watch memory), and side effects must be absent.
* For mutable market data I'd pair caches with explicit invalidation when snapshots change.


## When handling FX conversions, why might you choose `decimal.Decimal` over floats?

* `Decimal` provides base-10 exact arithmetic with configurable precision and rounding, avoiding binary float rounding drift that's unacceptable in cash calculations.
* It's slower, so I'd only use it where monetary accuracy matters, leaving analytics to floats/NumPy.


## Explain the difference between shallow vs deep copies and a scenario where the wrong choice causes a bug.

* Shallow copy duplicates the container but keeps references to the same inner objects; deep copy recursively clones everything.
* If I shallow copy a list of mutable leg dictionaries and mutate one, both copies reflect the change, possibly corrupting audit trails.
* Deep copy ensures independence when the nested objects must not be shared.


## How do context managers (`with`) help ensure reliable settlement file delivery?

* Context managers implement `__enter__`/`__exit__` to guarantee cleanup even on exceptions.
* Using them for file handles, network sockets, locks, or temporary directories ensures we flush/close resources and log failures, reducing operational risk when handing off files to downstream teams.


## Describe two ways to create custom context managers.

* Implement a class with `__enter__`/`__exit__`, or use the `contextlib` helpers like `@contextmanager` generator functions and `contextlib.ExitStack`.
* ExitStack is great when composing dynamic resources such as multiple temporary files per client batch.


## When parsing massive CSV trade files, how can `memoryview` and the buffer protocol reduce copies?

* `memoryview` exposes a zero-copy slice of bytes-like objects (e.g., `bytes`, `bytearray`, NumPy) following the buffer protocol.
* By parsing using `memoryview` slices we avoid allocating intermediate substrings, improving throughput for huge files.


## Explain how `bisect` is useful for time-series interpolation of borrow rates.

* `bisect` maintains a sorted list by finding insertion points in O(log n).
* I can locate the two surrounding timestamps quickly to interpolate rates without scanning, which is valuable when answering intraday borrow queries.


## How does Python's `sorted` leverage the Timsort algorithm, and what does its stability guarantee buy us for order books?

* Timsort merges sorted runs, performing well on partially ordered data (common in streaming order books).
* Its stability preserves the original order of equal keys, so when sorting by price, same-price orders stay FIFO, matching exchange semantics.


## Contrast `list.sort(key=...)` with `key=attrgetter(...)` and why `attrgetter` can be faster.

* Instead of lambdas, `operator.attrgetter` generates a C-level callable that avoids Python frame creation, giving lower overhead per comparison.
* When sorting millions of rows by multiple attributes (e.g., desk, symbol) the micro-optimization matters.


## What are enums (`enum.Enum`) and how do they help with legal entity classifications?

* Enums define symbolic names bound to constant values with type safety.
* They prevent typos, enable iteration over allowed values, and integrate with serialization.
* In risk reports I can represent clearing statuses or settlement systems as enums rather than magic strings.


## Explain `@staticmethod` vs `@classmethod` and provide a use case for each in a position class.

* `@staticmethod` behaves like a plain function namespaced on the class (no implicit args), e.g., helper to normalize symbols.
* `@classmethod` receives the class and suits alternative constructors (`Position.from_trade(trade)`) that need class identity for subclassing.


## How does `super()` enable cooperative multiple inheritance, and where is that useful in enterprise frameworks?

* `super()` follows the method resolution order (MRO) to call the next implementation, letting mixins share initialization without duplicating base classes.
* In a logging mixin plus persistence subclass, calling `super().__init__()` ensures each layer sets up correctly.


## When would you implement a metaclass in Python for an analytics infrastructure?

* Metaclasses customize class creation, so I'd use one to auto-register pricing models, enforce interface compliance, or inject config metadata at class definition time.
* They are advanced tools reserved for framework-level problems, not day-to-day logic.


## How do you guard against circular imports in a large risk platform?

* Keep modules focused, move shared types/interfaces to dedicated modules, and use local imports only when necessary to break cycles.
* Sometimes splitting functionality into packages or leveraging type-checking-only imports (`if TYPE_CHECKING`) prevents runtime cycles.


## Describe Python's module/package layout best practices for a reusable trade analytics library.

* Use `src/` layout with `pyproject.toml`/`setup.cfg`, keep an explicit `__all__`, place business logic under packages (e.g., `analytics/pricing.py`), separate config, tests, and scripts.
* Document dependencies and expose CLI entry points via console scripts.


## What purpose does `if __name__ == "__main__"` serve in scripts that schedule reports?

* It prevents the scheduling logic from running when the module is imported elsewhere (e.g., tests).
* I can keep functions importable for reuse while ensuring cron entry points only execute when explicitly run.


## How do `argparse` and dataclasses combine for CLI-driven operational tools?

* Parse CLI args with `argparse`, validate/convert them, then load into a dataclass that represents the job configuration.
* This gives type-checked, documented config objects that can be re-used in tests.


## Explain the difference between `raise` and `raise from` when handling downstream API errors.

* `raise` rethrows the current exception or raises a new one; `raise from` chains exceptions, preserving the original context (`__cause__`).
* When wrapping vendor API failures, `raise CustomError from exc` keeps the root cause for debugging.


## How would you design logging so it scales across multiple pods processing trades?

* Use the standard logging module, configure structured JSON formatters, set contextual data via `LoggerAdapter` or `structlog`, and ensure handlers are non-blocking (queue handlers).
* Emit to stdout for container aggregation and centralize via ELK/CloudWatch.


## When using `pytest`, what fixtures or plugins help test data pipelines?

* Parametrized fixtures to supply synthetic trade batches, `tmp_path` for temporary files, monkeypatching for API clients, and plugins like `pytest-asyncio` or `pytest-benchmark` to test async flows and performance regressions.


## How does `unittest.mock`'s `patch` differ from dependency injection, and when do you prefer each?

* `patch` temporarily replaces attributes on modules/classes, handy for isolating network calls.
* Dependency injection designs your code to receive collaborators (e.g., clients) explicitly, making tests cleaner and production code more flexible.
* I use DI whenever possible, reserving `patch` for legacy or unavoidable globals.


## What is the role of type checking tools like `mypy` in a regulated banking environment?

* Static type checkers catch interface mismatches before runtime, improving reliability and documentation.
* They also support gradual adoption, giving auditors confidence in critical calculations.
* Combined with CI they reduce production outages.


## Explain how pandas `merge` handles indexes vs columns and why aligning on multi-indexes matters for client statements.

* `merge` defaults to column joins, whereas aligning on indexes uses `left_index`/`right_index`.
* Multi-indexes (e.g., client, account, symbol) preserve hierarchical alignment; mis-specified indexes can duplicate or drop rows, so I ensure indexes are sorted and named before merging.


## How do you efficiently compute rolling metrics (e.g., VWAP) in pandas?

* Use `rolling(window).apply` or built-ins like `rolling().mean()` on Series/DataFrames, optionally combining with `groupby` for per-symbol windows.
* For time-based windows, resample to uniform frequency, then use `rolling('5min')`.
* Vectorized operations avoid Python loops.


## Discuss strategies to keep pandas memory footprint manageable with billions of rows.

* Read in chunks, convert dtypes (categoricals, `float32`), drop unused columns early, leverage `query` for filtering, and push as much as possible to databases or PyArrow/Polars.
* For intraday analytics I'd keep hot data in Arrow tables or Dask clusters.


## How can NumPy broadcasting simplify risk matrix calculations?

* Broadcasting automatically expands arrays along singleton dimensions, so I can combine factor matrices with position vectors without manual loops.
* By shaping arrays (e.g., `(n_positions, 1)` vs `(1, n_scenarios)`) vectorized math becomes concise and fast.


## What is `numpy.random.Generator` and why is it preferred over the legacy global RNG?

* `Generator` provides explicit RNG instances with better statistical properties (PCG64) and reproducible, thread-safe behavior.
* It avoids global state collisions when multiple risk scenarios run concurrently, allowing seeding per simulation.


## How would you serialize large position objects for inter-service messaging?

* Use `dataclasses.asdict()` plus `orjson`/`msgpack` for fast serialization, ensure only serializable fields are included, and consider schemas (Avro/JSON Schema) to validate payloads.
* Compress with zstd if needed.


## Explain the benefit of using `pathlib.Path` over `os.path` in batch jobs.

* `Path` offers object-oriented path manipulations, operator overloading for concatenation, high readability, and works uniformly across platforms.
* Methods like `.glob()` or `.read_text()` simplify file operations compared to string-based `os.path`.


## How does `subprocess.run` differ from `os.system` when invoking legacy scripts from Python?

* `subprocess.run` gives explicit control over arguments, environment, streams, timeouts, and error handling; it avoids shell injection risks if used with lists.
* `os.system` just delegates to the shell and returns an exit code.
* For regulated environments, `subprocess` is safer and more testable.


## What are `attrs` and why might you still choose dataclasses in standard libraries?

* `attrs` is a third-party library offering powerful class generation, validators, converters, and immutability features predating dataclasses.
* Dataclasses are built-in, interoperable, and sufficient for many cases; I'd use `attrs` when I need converters, validators, or slotted classes without writing boilerplate.


## Describe how to use `contextvars` in async code handling multiple client requests.

* `contextvars` store context-local state that's preserved across awaits but isolated per task, unlike thread-locals.
* I can keep request IDs or risk limits per client without passing them through every function, ensuring logging traces remain accurate.


## Why is `asyncio.gather` with `return_exceptions=True` sometimes required in market data fan-out services?

* Without it, the first exception cancels other coroutines; with `return_exceptions=True`, all tasks complete (or fail) and I can inspect individual errors.
* This prevents a single failing venue from cancelling fan-out to other venues.


## How would you guard asynchronous code against slow consumers when streaming quotes over websockets?

* Use bounded queues/backpressure: `asyncio.Queue(maxsize)` per client, drop or batch updates if queue is full, and monitor lag metrics.
* Apply `asyncio.wait_for` on send calls, and fall back to snapshots when clients can't keep up.


## What packaging considerations apply when shipping internal Python wheels to deployment pipelines?

* Build wheels via `pip wheel`/`build`, store in an internal index (Artifactory), pin dependencies, embed metadata (version, git SHA), and sign packages.
* Ensure reproducible builds via lock files and avoid direct `setup.py install`.


## Describe the role of environment isolation (virtualenv, venv, conda) in multi-project desks.

* Virtual environments isolate interpreter + dependencies per project, preventing version conflicts across desks.
* This allows me to freeze risk engines to known versions while experimenting elsewhere, and it simplifies CI/CD reproducibility.


## How do you safely handle secrets (e.g., database credentials) in Python apps?

* Never hardcode secrets; load them from secret managers (AWS Secrets Manager, HashiCorp Vault) via environment variables or short-lived tokens, inject via config files with locked-down ACLs, and avoid printing them in logs.
* Use key rotation and secure storage libraries.
