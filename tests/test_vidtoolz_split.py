import pytest
import vidtoolz_split as w

from argparse import Namespace, ArgumentParser

def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(['hello.mp4', "5"])
    assert result.input == "hello.mp4"
    assert result.splitat == 5
    assert result.output is None


def test_plugin(capsys):
    w.split_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out
