from mppwrapper.wrapper import MPPoolWrapper
from multiprocessing import cpu_count


def test_create_wrapper():
    wrapper = MPPoolWrapper([], cpu_count(), 1)
    assert len(wrapper.tasks) is 0
    assert wrapper.cores is cpu_count()
    assert wrapper.chunksize is 1


def test_compute_chunksize():
    assert MPPoolWrapper.compute_chunksize(10, n_cores=1) == 3
    assert MPPoolWrapper.compute_chunksize(10, n_cores=2) == 2
    assert MPPoolWrapper.compute_chunksize(1, n_cores=2) == 1


def test_create_chunks():
    assert len(MPPoolWrapper.create_chunks(list(range(0, 10)), n_cores=1)) == 4
    assert len(MPPoolWrapper.create_chunks(list(range(0, 10)), n_cores=2)) == 5
    assert len(MPPoolWrapper.create_chunks([0], n_cores=2)) == 1


def test_chunksize_when_creating_tasks():
    assert MPPoolWrapper.create_tasks(print, list(range(0, 10)), n_cores=1).chunksize == 3
    assert MPPoolWrapper.create_tasks(print, list(range(0, 10)), n_cores=2).chunksize == 2
    assert MPPoolWrapper.create_tasks(print, [0], n_cores=2).chunksize == 1


def test_n_cores_when_creating_tasks():
    assert MPPoolWrapper.create_tasks(print, [0]).cores == cpu_count()
    assert MPPoolWrapper.create_tasks(print, [0], n_cores=2).cores == 2


def test_tasks():
    data = ['this', 'is', 'a', 'test']
    wrapper = MPPoolWrapper.create_tasks(print, data)
    for task in wrapper.tasks:
        assert task[0] == print

    assert wrapper.tasks[0][-1] == ['this']
    assert wrapper.tasks[1][-1] == ['is']
    assert wrapper.tasks[2][-1] == ['a']
    assert wrapper.tasks[3][-1] == ['test']
