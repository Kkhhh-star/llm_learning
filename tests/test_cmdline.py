import sys

import pytest

from python_learning import cmdline


def test_help(mocker, capsys):
    """test help command"""
    args = ['python_learning', '-h']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        cmdline.main()

    assert ex.value.code == 0
    outerr = capsys.readouterr()
    assert '-s SOURCE' in outerr.out
    assert '-d DEST' in outerr.out

def test_only_pass_source(mocker, capsys):
    """test only pass -s """
    args = ['python_learning', '-s', 'foo']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        cmdline.main()

    assert ex.value.code == 2
    outerr = capsys.readouterr()
    assert 'the following arguments are required: -d' in outerr.err

def test_only_pass_dest(mocker, capsys):
    """test only pass -d"""
    args = ['python_learning', '-d', 'foo']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        cmdline.main()

    assert ex.value.code == 2
    outerr = capsys.readouterr()
    assert 'the following arguments are required: -s' in outerr.err

def test_main(mocker):
    """test cmdline, and everything is fine."""
    args = ['python_learning', '-s', 'foo', '-d', 'bar']
    mocker.patch.object(sys, 'argv', args)
    mock_count = mocker.patch('python_learning.cmdline.count')
    cmdline.main()
    mock_count.assert_called_once()