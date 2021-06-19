import os

from api.app.tools.make_as_scan import MakeAsScan


def test_prepare_scan():
    root_dir = os.getcwd()
    MakeAsScan(
        os.path.join(root_dir, 'tests', 'mozilla.pdf'),
        os.path.join(root_dir, 'tests', 'test.pdf')
    ).process_file()
