from enum import Enum

class BillingTerm(Enum):
    """
    Enum representing billing terms.
    """
    Monthly = "Monthly"
    Annual = "Annual"
    Year2 = "2-Year"
    Year3 = "3-Year"
    OneTime = "1-Time"
    Trial = "Trial"
