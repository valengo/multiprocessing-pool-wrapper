#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: valengo
"""

from multiprocessing import Pool
from multiprocessing import freeze_support
from multiprocessing import cpu_count
from typing import Callable, Any


class MPPoolWrapper(object):
    """
    Handle tasks multiprocessing using multiprocessing.Pool

    :param list tasks: a list of tasks. Each task is defined as a tuple
    :param int cores: number of cores to be used when multiprocessing
    :param int chunksize: chunksize of tasks to be send each time for a given process

    """

    def __init__(self, tasks: list, cores: int, chunksize: int):
        self.tasks = tasks
        self._cores = cores
        self._chunksize = chunksize
        self.pool = None

    @classmethod
    def create_tasks(cls, task: Callable, data: [Any], *args, n_cores=None):
        chunks = MPPoolWrapper.create_chunks(data, n_cores=n_cores)
        tasks = [(task, chunk, *args) for chunk in chunks]
        return MPPoolWrapper(tasks, n_cores, len(chunks[0]))

    @property
    def cores(self):
        if self._cores is None:
            return cpu_count()
        return self._cores

    @property
    def chunksize(self):
        return self._chunksize

    @staticmethod
    def compute_chunksize(data_len: int, n_cores=None) -> int:
        if n_cores is None:
            n_cores = cpu_count()
        chunksize, extra = divmod(data_len, n_cores * 4)
        if extra:
            chunksize += 1
        return chunksize

    @staticmethod
    def create_chunks(data: [Any], n_cores=None) -> [Any]:
        chunksize = MPPoolWrapper.compute_chunksize(len(data), n_cores=n_cores)
        chunks = []
        for i in range(0, len(data), chunksize):
            chunks.append(data[i: i + chunksize])
        return chunks

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict

    def __setstate__(self, state):
        self.__dict__.update(state)

    @staticmethod
    def _runstar(args) -> list:
        return args[0](*args[1:len(args)])

    def run(self) -> list:
        """
        Run tasks

        :return: a list containing the resulting stuff of tasks
        """
        freeze_support()
        self.pool = Pool(self.cores)
        results = list(self.pool.imap(self._runstar, self.tasks))
        self.pool.close()
        return [r for res in results for r in res]
