class PageResponse:
    """
    Represents pagination details for a response.
    """
    def __init__(self, size, total_elements, total_pages, number):
        """
        Initializes an instance of the PageResponse class.
        :param size: The size of the page
        :param total_elements: The total number of elements that can be paged over
        :param total_pages: The total number of pages based on size and total_elements
        :param number: The current page
        """
        self.size = size
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.number = number

    def __repr__(self):
        """
        Returns a string representation of the PageResponse instance.
        """
        return (f"PageResponse(size={self.size}, total_elements={self.total_elements}, "
                f"total_pages={self.total_pages}, number={self.number})")
