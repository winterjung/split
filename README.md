# Split

> ✂️ GitHub action to split string

## Inputs

- `msg`: String to split
- `seperator`: The delimiter to split the string. Default: `' '` (whitespace)
- `maxsplit`: Maximum number of splits. Default: `-1` (no limit)

## Outputs

- `0`, `1`, ..., `n`: Each result of a splits
- `length`: Length of the splits

## Example

```yaml
name: split example
jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - uses: jungwinter/split@v1
        id: split
        with:
          msg: '/release split v1.0.0'

      - name: release package
        if: steps.split.outputs.0 == '/release'
        uses: actions/create-release@latest
        with:
          release_name: Release ${{ steps.split.outputs.1 }}
          tag_name: ${{ steps.split.outputs.2 }}
```

---

[MIT license]


[MIT license]: LICENSE
