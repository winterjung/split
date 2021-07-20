import pytest

from main import DEFINED_ACTION_OUTPUTS_NUMBER, split, to_outputs


class TestSplit:
    @pytest.mark.parametrize(
        'msg, sep, expected',
        [
            ('/release split v1.0.0', ' ', ['/release', 'split', 'v1.0.0']),
            ('/release split v1.0.0', ',', ['/release split v1.0.0']),
            ('/release split v1.0.0', '.', ['/release split v1', '0', '0']),
            ('/release split v1', '\'', ['/release split v1']),
            ('/release split v1', '"', ['/release split v1']),
            ('/release split v1', '/', ['', 'release split v1']),
            ('/release  split  v1', ' ', ['/release', '', 'split', '', 'v1']),
            (' /release split v1 ', ' ', ['', '/release', 'split', 'v1', '']),
        ],
    )
    def test_separator(self, msg, sep, expected):
        assert split(msg, sep=sep) == expected

    def test_empty_separator(self):
        with pytest.raises(ValueError):
            split('must fail', sep='')

    @pytest.mark.parametrize(
        'msg, maxsplit, expected',
        [
            ('/release split v1.0.0', -1, ['/release', 'split', 'v1.0.0']),
            ('/release split v1.0.0', 0, ['/release split v1.0.0']),
            ('/release split v1.0.0', 1, ['/release', 'split v1.0.0']),
        ],
    )
    def test_maxsplit(self, msg, maxsplit, expected):
        assert split(msg, maxsplit=maxsplit) == expected

    @pytest.mark.parametrize(
        'length, maxsplit, expected',
        [
            (DEFINED_ACTION_OUTPUTS_NUMBER, -1, '99'),
            (DEFINED_ACTION_OUTPUTS_NUMBER + 1, -1, '99 100'),
            (
                DEFINED_ACTION_OUTPUTS_NUMBER + 1,
                DEFINED_ACTION_OUTPUTS_NUMBER,
                '99 100',
            ),
            (
                DEFINED_ACTION_OUTPUTS_NUMBER + 1,
                DEFINED_ACTION_OUTPUTS_NUMBER + 1,
                '99 100',
            ),
        ],
    )
    def test_maxsplit_with_long_string(self, length, maxsplit, expected):
        msg = ' '.join(map(str, range(length)))
        results = split(msg, maxsplit=maxsplit)
        assert results[-1] == expected

    def test_maxsplit_is_not_numeric(self):
        with pytest.raises(TypeError):
            split('must fail', maxsplit='a')
        with pytest.raises(TypeError):
            split('must fail', maxsplit=None)


class TestToOutputs:
    def test_to_outputs(self):
        results = to_outputs(split('/release split v1'))

        expected = {
            'length': '3',
            '_0': '/release',
            '_1': 'split',
            '_2': 'v1',
        }
        assert results == expected

    def test_large_results_to_outputs(self):
        msg = ' '.join(map(str, range(DEFINED_ACTION_OUTPUTS_NUMBER + 1)))

        results = to_outputs(split(msg))

        assert results['length'] == '100'
        assert results['_99'] == '99 100'
