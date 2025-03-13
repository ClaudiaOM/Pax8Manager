class SubscriptionRequest:
    """
    Represents a subscription request.
    """
    def __init__(self, subscription_id, quantity, start_date, end_date, price, billing_term):
        """
        Initializes an instance of the SubscriptionRequest class.
        :param subscription_id: The ID of the subscription
        :param quantity: The quantity for the subscription
        :param start_date: The start date of the subscription
        :param end_date: The end date of the subscription
        :param price: The price of the subscription
        :param billing_term: The billing term (an instance of BillingTerm Enum)
        """
        self.subscription_id = subscription_id
        self.quantity = quantity
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.billing_term = billing_term 

    def __repr__(self):
        """
        Returns a string representation of the SubscriptionRequest instance.
        """
        return (f"SubscriptionRequest(subscription_id={self.subscription_id}, quantity={self.quantity}, "
                f"start_date={self.start_date}, end_date={self.end_date}, price={self.price}, "
                f"billing_term={self.billing_term})")
