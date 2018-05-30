import pytest
import time
import io


def sio_aaa():
    sio = io.StringIO("12345")
    time.sleep(1)
    print("created")
    yield sio
    time.sleep(1)
    sio.close()
    print("closed")


def test1(sio_aaa):
    assert sio_aaa.getvalue() == "2345"


def test2(sio_aaa):
    assert sio_aaa.getvalue() == "3456"

# pytestで実行、fixtureがある時とない時を実行して比較する。fixtureの役割がよくわからん
# StringIOがインポートされていない？pipでインストールする必要がある？pythonのデフォルトでない？
# StringIOではなく、python3.0からStringIOではなくio
