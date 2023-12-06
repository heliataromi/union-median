def median(arr: list[float]) -> float:
    """
        Calculate the median of a sorted list of numbers.

        Parameters
        ----------
        arr : list[float]
            A sorted list of floats from which to find the median.

        Returns
        -------
        float
            The median value of the list.
    """

    n = len(arr)

    # Check if the list has an odd number of elements
    if n % 2 != 0:
        # If so, return the middle element
        return arr[n // 2]
    else:
        # If even, return the average of the two middle elements
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


def union_median(a: list[float], b: list[float]) -> float:
    """
        Find the median of two sorted lists of equal length by the divide and conquer approach.

        Parameters
        ----------
        a : list[float]
            The first sorted list of floats.
        b : list[float]
            The second sorted list of floats.

        Returns
        -------
        float
            The median of the two sorted lists.

        Raises
        ------
        Exception
            If the two lists are not of equal length.
    """

    # Ensure both lists are of the same length
    if len(a) != len(b):
        raise Exception("Both lists must be the same length.")

    # Length of the lists
    n = len(a)

    # Base case for the median of both lists
    median_a = median(a)
    median_b = median(b)

    # Check if the lists have an odd number of elements
    if n % 2 != 0:
        # If median of `a` is greater, consider the left half of `a` and right half of `b`
        if median_a > median_b:
            a = a[:n // 2 + 1]
            b = b[n // 2:]
            return union_median(a, b)

        # If median of `b` is greater, consider the left half of `b` and right half of `a`
        else:
            a = a[n // 2:]
            b = b[:n // 2 + 1]
            return union_median(a, b)

    # Check if the lists have an even number of elements
    if n % 2 == 0:
        # Base case: Two elements in each list.
        if n == 2:
            # The median of the union of both is just the median of the sorted merged lists
            return median(sorted(a + b))

        # If median of `a` is greater, consider the left half of `a` and right half of `b`
        elif median_a > median_b:
            a = a[:n // 2 + 1]
            b = b[n // 2 - 1:]
            return union_median(a, b)

        # If median of `b` is greater, consider the left half of `b` and right half of `a`
        else:
            a = a[n // 2 - 1:]
            b = b[:n // 2 + 1]
            return union_median(a, b)
