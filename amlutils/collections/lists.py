import typing


def flatten_list(list_of_lists: typing.List[typing.List[typing.Any]]) -> typing.List[typing.Any]:
    return [item for sublist in list_of_lists for item in sublist]


def chunks_of_list(iterable: typing.List[typing.Any], chunk_size: int):
    length = len(iterable)
    for ndx in range(0, length, chunk_size):
        yield iterable[ndx:min(ndx + chunk_size, length)]
