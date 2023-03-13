import os
from typing import Dict, List, Optional


DEFINED_ACTION_OUTPUTS_NUMBER = 100


def set_action_output(name: str, value: str):
    # See https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/
    path = os.getenv('GITHUB_OUTPUT')
    if not path:
        print_action_error('$GITHUB_OUTPUT env is required.')
        exit(1)
    with open(path, 'a') as github_output_file:
        github_output_file.write(f'{name}={value}\n')


def print_action_error(msg: str):
    print(f'::error file={__name__}::{msg}')


def print_action_debug(msg: str):
    print(f'::debug::{msg}')


def get_action_input(
    name: str, required: bool = False, default: Optional[str] = None
) -> str:
    v = os.environ.get(f'INPUT_{name.upper()}', '')
    if v == '' and default:
        v = default
    if required and v == '':
        print_action_error(f'input required and not supplied: {name}')
        exit(1)
    return v


def split(msg: str, sep: str = ' ', maxsplit: int = -1) -> List[str]:
    results = msg.split(sep=sep, maxsplit=maxsplit)
    if len(results) > DEFINED_ACTION_OUTPUTS_NUMBER:
        results = msg.split(
            sep=sep, maxsplit=DEFINED_ACTION_OUTPUTS_NUMBER - 1
        )
    return results


def to_outputs(results: List[str]) -> Dict[str, str]:
    outputs = {
        'length': str(len(results)),
    }
    for i, result in enumerate(results):
        outputs[f'_{i}'] = result
    return outputs


def main():
    msg = get_action_input('msg', required=True)
    print_action_debug(f'msg: {msg}')
    separator = get_action_input('separator', required=False, default=' ')
    print_action_debug(f'separator: {separator}')
    maxsplit = int(get_action_input('maxsplit', required=False, default='-1'))
    print_action_debug(f'maxsplit: {maxsplit}')

    results = split(msg, separator, maxsplit)
    print_action_debug(f'results: {results}')
    outputs = to_outputs(results)
    print_action_debug(f'outputs: {outputs}')
    for k, v in outputs.items():
        print_action_debug(f'k: {k}, v: {v}')
        set_action_output(k, v)


if __name__ == '__main__':
    main()
