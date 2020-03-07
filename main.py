import os
from typing import Optional


DEFINED_ACTION_OUTPUTS_NUMBER = 100


def set_action_output(name: str, value: str):
    print(f'::set-output name={name}::{value}')


def print_action_error(msg: str):
    print(f'::error file={__name__}::{msg}')


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


def main():
    msg = get_action_input('msg', required=True)
    seperator = get_action_input('seperator', required=False, default=' ')
    maxsplit = int(get_action_input('maxsplit', required=False, default='-1'))

    results = msg.split(sep=seperator, maxsplit=maxsplit)
    if len(results) > DEFINED_ACTION_OUTPUTS_NUMBER:
        results = msg.split(sep=seperator, maxsplit=DEFINED_ACTION_OUTPUTS_NUMBER - 1)

    for i, result in enumerate(results):
        set_action_output('_' + str(i), result)
    set_action_output('length', len(results))


if __name__ == '__main__':
    main()
