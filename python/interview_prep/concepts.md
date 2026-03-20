# Core Concepts and Study Sources

| Concept | Why It Matters | Primary Reference |
| --- | --- | --- |
| Python data model & descriptors | Powers attributes, iteration, context managers, and is frequently probed when building custom models. | https://docs.python.org/3/reference/datamodel.html |
| Iterators, generators, `yield from` | Enables streaming market data and memory-efficient ETL. | https://docs.python.org/3/howto/functional.html |
| Concurrency (`threading`, `multiprocessing`, `asyncio`) | Choosing the right concurrency primitive is crucial for latency-sensitive services. | https://docs.python.org/3/library/concurrency.html |
| Global Interpreter Lock & performance tuning | Understanding the GIL avoids misusing threads for CPU-bound analytics. | https://docs.python.org/3/glossary.html#term-global-interpreter-lock |
| Dataclasses vs attrs vs namedtuples | Modeling trades/positions cleanly requires the right data container. | https://docs.python.org/3/library/dataclasses.html |
| Typing (`Protocol`, `TypedDict`, `mypy`) | Static analysis improves reliability in regulated environments. | https://typing.readthedocs.io/en/latest/ |
| Context managers & `contextlib` | Guarantees resource cleanup for files, sockets, and locks. | https://docs.python.org/3/library/contextlib.html |
| Decorators (`functools`, `lru_cache`, `singledispatch`) | Common interview topic and essential for reusable analytics utilities. | https://docs.python.org/3/library/functools.html |
| Numerical precision (`decimal`, `fractions`) | Avoids rounding errors in cash/FX flows. | https://docs.python.org/3/library/decimal.html |
| Logging best practices | Critical for audit trails in banking apps. | https://docs.python.org/3/howto/logging.html |
| Testing (`pytest`, `unittest.mock`) | Demonstrates ability to build verifiable systems. | https://docs.pytest.org/en/latest/ |
| Packaging (`pyproject.toml`, wheels, virtualenv) | Needed to ship code to internal repos and prod. | https://packaging.python.org/en/latest/tutorials/packaging-projects/ |
| Pandas data pipelines | Bread-and-butter for equities analytics and reporting. | https://pandas.pydata.org/docs/ |
| NumPy broadcasting & random generators | Forms the base for vectorized risk calculations. | https://numpy.org/doc/stable/ |
| Async patterns (`asyncio.gather`, backpressure) | Ensures resilient market data fan-out services. | https://docs.python.org/3/library/asyncio-task.html |
| Serialization (`json`, `orjson`, `msgpack`) | Required for messaging between desks and services. | https://docs.python.org/3/library/json.html |
| Secrets management & config | Prevents credential leaks and satisfies compliance. | https://12factor.net/config |
| Profiling/performance (`cProfile`, `pyinstrument`) | Lets you prove optimizations with data. | https://docs.python.org/3/library/profile.html |
| SQL/DB interfaces (`sqlite3`, `SQLAlchemy`) | Many prime services workflows persist to databases. | https://docs.sqlalchemy.org/en/latest/ |
| Data validation (`pydantic`, `marshmallow`) | Keeps inbound/outbound payloads strict and testable. | https://docs.pydantic.dev/latest/ |
