import bz2
import fnmatch
import gzip
import os
import re


def gen_find(file_pattern, top_dir):
    # generate file-name-path in a directory tre
    for path, dir_list, file_list in os.walk(top_dir):
        for name in fnmatch.filter(file_list, file_pattern):
            yield os.path.join(path, name)


def gen_open(file_paths: os.path):
    for name in file_paths:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".gz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)


def gen_get_line(sources):
    for object in sources:
        for line in object:
            yield line


def gen_grep(pat, lines):
    re_compiled_pattern = re.compile(pattern=pat)
    for line in lines:
        if re_compiled_pattern.search(line):
            yield line


def capture_matching_logs(top_dir, file_patern, line_pattern):
    log_names = gen_find(file_patern, top_dir)
    file_obj = gen_open(log_names)
    log_lines = gen_get_line(file_obj)
    matching_lines = gen_grep(pat=line_pattern, lines=log_lines)
    yield matching_lines


def log_map(dictseq, name, func):
    for d in dictseq:
        d[name] = func(d[name])
        yield d


def break_up_log_lines(lines):
    log_patterns = r'(\S+) (\S+) ....'
    column_names = ('pat_1', 'pat2', ...)
    log_pat = re.compile(log_patterns)
    groups = (log_pat.match(line) for line in lines)
    tuples = (g.groups() for g in groups if g)
    log_dict = (dict(zip(column_names, t)) for t in tuples)
    log_dict_1 = log_map(log_dict, 'status', int)
    log_dict_2 = log_map(log_dict_1, 'bytes', lambda s: int(s) if s != '-' else 0)
    yield log_dict_2


# TODO: add query language setup in the sequence

if __name__ == "__main__":
    top_dir = "c:\\temp\\"
    pattern = "*obo*"
    trade_id = "sample_trade"
    line_pattern = f"*{trade_id}*"
    lines = capture_matching_logs(top_dir=top_dir, file_patern=pattern, line_pattern=line_pattern)
    log_dict_seq = break_up_log_lines(lines)
    for log_struct in log_dict_seq:
        print(log_struct)

