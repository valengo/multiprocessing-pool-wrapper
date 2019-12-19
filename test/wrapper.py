from mppwrapper.wrapper import MPPoolWrapper
from multiprocessing import cpu_count


def test_create_wrapper():
    wrapper = MPPoolWrapper([])
    assert len(wrapper.tasks) is 0
    assert wrapper.cores is cpu_count()
    assert wrapper.chunksize is 1
