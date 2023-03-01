import os


def test_main():
    """Dummy test to run unit tests."""
    snap_path = os.environ.get("TEST_SNAP")
    assert snap_path is not None
    assert os.path.exists(snap_path)
