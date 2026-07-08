# lance-tensorflow

TensorFlow integration for Lance datasets.

This package provides a small Python adapter that exposes Lance datasets as
`tf.data.Dataset` pipelines. The core Lance format and Python bindings remain in
the `pylance` package.

## Install

```bash
pip install lance-tensorflow
```

TensorFlow support is currently targeted at Linux.

## Usage

```python
from lance_tensorflow import from_lance

ds = from_lance(
    "s3://bucket/path",
    columns=["image", "label"],
    filter="split = 'train'",
    batch_size=256,
)

for batch in ds:
    print(batch["label"])
```

If you want the `tf.data.Dataset.from_lance` convenience methods, register them
explicitly:

```python
import tensorflow as tf
import lance_tensorflow

lance_tensorflow.register_tensorflow_dataset()

ds = tf.data.Dataset.from_lance("s3://bucket/path")
```

## Development

```bash
uv sync
uv run pytest
uv run ruff format .
uv run ruff check .
```
