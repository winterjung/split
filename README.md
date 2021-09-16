# Split

[![Actions Status](https://github.com/jungwinter/split/workflows/ci/badge.svg)](https://github.com/jungwinter/split/actions)

> ✂️ GitHub action to split string

## Inputs

- `msg`: String to split
- `separator`: The delimiter to split the string. Default: `' '` (whitespace)
- `maxsplit`: Maximum number of splits. Default: `-1` (no limit)

## Outputs

- `_0`, `_1`, ..., `_n`: Each result of a splits
  - According to [metadata syntax of outputs], it has `_` prefix
  - Currently, support only `100` splits
- `length`: Length of the splits

## Example

```yaml
name: split example
jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - uses: jungwinter/split@v2
        id: split
        with:
          msg: '/release split v1.0.0'

      - name: release package
        if: steps.split.outputs._0 == '/release'
        uses: actions/create-release@latest
        with:
          release_name: Release ${{ steps.split.outputs._1 }}
          tag_name: ${{ steps.split.outputs._2 }}
```

---

[MIT license]


[MIT license]: LICENSE
[metadata syntax of outputs]: https://help.github.com/en/actions/building-actions/metadata-syntax-for-github-actions#outputsoutput_id
