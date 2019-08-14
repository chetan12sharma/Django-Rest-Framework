from rest_framework.pagination import LimitOffsetPagination
"""
    For Custome Pagination
"""


class LimitOffsetPaginationUpperBound(LimitOffsetPagination):
    """
        Limit the upper limit of the pagination
    """
    max_limit = 8
