import multiprocessing

workers = multiprocessing.cpu_count() + 1
bind = '0.0.0.0:8000'