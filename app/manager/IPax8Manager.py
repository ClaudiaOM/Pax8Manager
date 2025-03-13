from abc import ABC, abstractmethod
from models.response import (
    ResponseModel, TokenResponse, CompanyListResponse, CompanyResponse, 
    ProductListResponse, ProductResponse, SubscriptionListResponse, 
    SubscriptionResponse
)
from models.request import SubscriptionRequest

class IPax8Manager(ABC):
    """
    Abstract base class representing the interface for Pax8Manager.
    """

    @abstractmethod
    def get_access_token(self) -> ResponseModel[TokenResponse]:
        """
        OAuth2 Authentication Method.
        :return: ResponseModel containing TokenResponse.
        """
        pass

    # Company region
    @abstractmethod
    def get_companies(self, page: int = 0, size: int = 10) -> ResponseModel[CompanyListResponse]:
        """
        Fetches a list of companies with pagination.
        :param page: Page number (default: 0).
        :param size: Page size (default: 10).
        :return: ResponseModel containing CompanyListResponse.
        """
        pass

    @abstractmethod
    def get_company(self, company_id: str) -> ResponseModel[CompanyResponse]:
        """
        Fetches details of a specific company.
        :param company_id: The ID of the company.
        :return: ResponseModel containing CompanyResponse.
        """
        pass

    # Product region
    @abstractmethod
    def get_products(self, page: int = 0, size: int = 10) -> ResponseModel[ProductListResponse]:
        """
        Fetches a list of products with pagination.
        :param page: Page number (default: 0).
        :param size: Page size (default: 10).
        :return: ResponseModel containing ProductListResponse.
        """
        pass

    @abstractmethod
    def get_product(self, product_id: str) -> ResponseModel[ProductResponse]:
        """
        Fetches details of a specific product.
        :param product_id: The ID of the product.
        :return: ResponseModel containing ProductResponse.
        """
        pass

    # Subscriptions region
    @abstractmethod
    def get_subscriptions(self, page: int = 0, size: int = 10) -> ResponseModel[SubscriptionListResponse]:
        """
        Fetches a list of subscriptions with pagination.
        :param page: Page number (default: 0).
        :param size: Page size (default: 10).
        :return: ResponseModel containing SubscriptionListResponse.
        """
        pass

    @abstractmethod
    def get_subscription_by_company(self, company_id: str) -> ResponseModel[SubscriptionListResponse]:
        """
        Fetches a list of subscriptions for a specific company.
        :param company_id: The ID of the company.
        :return: ResponseModel containing SubscriptionListResponse.
        """
        pass

    @abstractmethod
    def get_subscription(self, subscription_id: str) -> ResponseModel[SubscriptionResponse]:
        """
        Fetches details of a specific subscription.
        :param subscription_id: The ID of the subscription.
        :return: ResponseModel containing SubscriptionResponse.
        """
        pass

    @abstractmethod
    def update_subscription(self, subscription_request: SubscriptionRequest) -> ResponseModel[SubscriptionResponse]:
        """
        Updates a subscription.
        :param subscription_request: The subscription request model.
        :return: ResponseModel containing SubscriptionResponse.
        """
        pass
