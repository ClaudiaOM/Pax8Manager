class SubscriptionResponse:
    """
    Represents subscription details.
    """
    def __init__(self, id, product_id, parent_subscription_id, company_id, quantity, start_date,
                 end_date, created_date, billing_start, status, price, billing_term, commitment_term):
        """
        Initializes an instance of the SubscriptionResponse class.
        :param id: The unique ID of the subscription
        :param product_id: The associated product ID
        :param parent_subscription_id: ID of the parent subscription, if applicable
        :param company_id: ID of the associated company
        :param quantity: Quantity of the subscription
        :param start_date: Start date of the subscription
        :param end_date: End date of the subscription
        :param created_date: Date when the subscription was created
        :param billing_start: Billing start date
        :param status: Status of the subscription
        :param price: Price of the subscription
        :param billing_term: Billing term (e.g., Monthly, Annual)
        :param commitment_term: An instance of CommitmentTermResponse
        """
        self.id = id
        self.product_id = product_id
        self.parent_subscription_id = parent_subscription_id
        self.company_id = company_id
        self.quantity = quantity
        self.start_date = start_date
        self.end_date = end_date
        self.created_date = created_date
        self.billing_start = billing_start
        self.status = status
        self.price = price
        self.billing_term = billing_term  # Enum value
        self.commitment_term = commitment_term  # Instance of CommitmentTermResponse

    def __repr__(self):
        return (f"SubscriptionResponse(id={self.id}, product_id={self.product_id}, "
                f"parent_subscription_id={self.parent_subscription_id}, company_id={self.company_id}, "
                f"quantity={self.quantity}, start_date={self.start_date}, end_date={self.end_date}, "
                f"created_date={self.created_date}, billing_start={self.billing_start}, "
                f"status={self.status}, price={self.price}, billing_term={self.billing_term}, "
                f"commitment_term={self.commitment_term})")



class CommitmentTermResponse:
    """
    Represents the commitment term of a subscription.
    """
    def __init__(self, id, term, end_date):
        """
        Initializes an instance of the CommitmentTermResponse class.
        :param id: Unique ID of the commitment term
        :param term: Duration of the commitment
        :param end_date: End date of the commitment
        """
        self.id = id
        self.term = term
        self.end_date = end_date

    def __repr__(self):
        return f"CommitmentTermResponse(id={self.id}, term={self.term}, end_date={self.end_date})"


class SubscriptionListResponse:
    """
    Represents a paginated list of subscriptions.
    """
    def __init__(self, content, page):
        """
        Initializes an instance of the SubscriptionListResponse class.
        :param content: List of SubscriptionResponse objects
        :param page: An instance of PageResponse
        """
        self.content = content  # List of SubscriptionResponse objects
        self.page = page  # Instance of PageResponse

    def __repr__(self):
        return f"SubscriptionListResponse(content={self.content}, page={self.page})"
