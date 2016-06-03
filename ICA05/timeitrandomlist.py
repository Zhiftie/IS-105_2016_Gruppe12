from randomlist import Search_s, Search_f
if __name__ == "__main__":
    """
    timeit test for the search slow and search_fast function
    """
    import timeit
    timer = timeit.Timer(Search_s)
    result = timer.repeat(repeat = 100, number = 100)
    print ("{:8.6f}".format(min(result)))
    timer = timeit.Timer(Search_f)
    result = timer.repeat(repeat = 100, number = 100)
    print ("{:8.6f}".format(min(result)))