import json
from datetime import datetime, timedelta
from typing import TypeVar, Generic, Dict, Any, Optional
import requests
from app.models.response import CompanyResponse
from app.models.response import ResponseModel, TokenResponse, CompanyListResponse,  ProductResponse, SubscriptionResponse, SubscriptionListResponse, ErrorResponse
from app.models.request import SubscriptionRequest
from app.settings import pax8_settings

T = TypeVar("T", bound=Any)  # Generic type for response content

class Pax8Manager:
    """
    Manages interactions with the Pax8 API.
    """

    TOKEN_URL = "/token"
    COMPANIES_URL = "/companies"
    PRODUCT_URL = "/products"

    def __init__(self, settings: pax8_settings):
        self.settings = settings
        self.token: Optional[TokenResponse] = None
        self.token_request_time: Optional[datetime] = None

    def _check_response(self, response_content: str, response_uri: str) -> ResponseModel[T]:
        """
        Parses and validates the response from the Pax8 API.
        """
        try:
            error = json.loads(response_content).get("error")
            if error:
                return ResponseModel(
                    error=ErrorResponse(**error),
                    message="Error",
                    resource=response_uri,
                    is_success=False
                )
            response_object = json.loads(response_content)
            return ResponseModel(
                content=response_object,
                message="Successful",
                resource=response_uri,
                is_success=True
            )
        except json.JSONDecodeError:
            return ResponseModel(
                error=ErrorResponse(
                    message="Invalid JSON response.",
                    type="ParseError"
                ),
                message="Error",
                resource=response_uri,
                is_success=False
            )

    def _refresh_token_if_expired(self) -> bool:
        """
        Refreshes the OAuth token if it is expired.
        """
        if self.token and self.token_request_time:
            expiration_time = self.token_request_time + timedelta(seconds=self.token.expires_in)
            if datetime.utcnow() > expiration_time:
                self.token = self.get_access_token().content
        else:
            self.token = self.get_access_token().content
        return bool(self.token)

    def get_access_token(self) -> ResponseModel[TokenResponse]:
        """
        Fetches a new OAuth access token.
        """
        url = f"{self.settings.base_url}{self.TOKEN_URL}"
        headers = {"Accept": "application/json"}
        body = {
            "audience": self.settings.audience,
            "grant_type": self.settings.grant_type,
            "client_id": self.settings.client_id,
            "client_secret": self.settings.client_secret,
        }

        response = requests.post(url, json=body, headers=headers)
        self.token_request_time = datetime.utcnow()
        return self._check_response(response.text, url)

    def get_companies(self, page: int = 0, size: int = 10) -> ResponseModel[CompanyListResponse]:
        """
        Retrieves a paginated list of companies.
        """
        if not self._refresh_token_if_expired():
            return ResponseModel(error=ErrorResponse(message="Failed to refresh token."))

        url = f"{self.settings.base_url}{self.COMPANIES_URL}?page={page}&size={size}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token.access_token}"
        }

        response = requests.get(url, headers=headers)
        return self._check_response(response.text, url)

    def get_company(self, company_id: str) -> ResponseModel[CompanyResponse]:
        """
        Retrieves details of a specific company.
        """
        if not company_id:
            return ResponseModel(
                error=ErrorResponse(
                    message="Company ID cannot be empty.",
                    type="BadRequest"
                )
            )

        if not self._refresh_token_if_expired():
            return ResponseModel(error=ErrorResponse(message="Failed to refresh token."))

        url = f"{self.settings.base_url}{self.COMPANIES_URL}/{company_id}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token.access_token}"
        }

        response = requests.get(url, headers=headers)
        return self._check_response(response.text, url)

    def get_product(self, product_id: str) -> ResponseModel[ProductResponse]:
        """
        Retrieves details of a specific product.
        """
        if not product_id:
            return ResponseModel(
                error=ErrorResponse(
                    message="Product ID cannot be empty.",
                    type="BadRequest"
                )
            )

        if not self._refresh_token_if_expired():
            return ResponseModel(error=ErrorResponse(message="Failed to refresh token."))

        url = f"{self.settings.base_url}{self.PRODUCT_URL}/{product_id}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token.access_token}"
        }

        response = requests.get(url, headers=headers)
        return self._check_response(response.text, url)

    def get_subscription(self, subscription_id: str) -> ResponseModel[SubscriptionResponse]:
        """
        Retrieves details of a specific subscription.
        """
        if not subscription_id:
            return ResponseModel(
                error=ErrorResponse(
                    message="Empty subscription ID",
                    type="400"
                ),
                is_success=False,
                message="Empty subscription ID"
            )

        self._refresh_token_if_expired()
        url = f"{self.settings.base_url}/subscriptions/{subscription_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}

        response = requests.get(url, headers=headers)
        return self._check_response(response.text, url)

    def get_subscriptions(self, page: int = 0, size: int = 10) -> ResponseModel[SubscriptionListResponse]:
        """
        Retrieves a paginated list of subscriptions.
        """
        if page < 0 or size < 0:
            return ResponseModel(
                error=ErrorResponse(
                    message="Invalid pagination parameters",
                    type="400"
                ),
                is_success=False,
                message="Invalid pagination parameters"
            )

        self._refresh_token_if_expired()
        url = f"{self.settings.base_url}/subscriptions?page={page}&size={size}"
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}

        response = requests.get(url, headers=headers)
        return self._check_response(response.text, url)

    def get_subscription_by_company(self, company_id: str) -> ResponseModel[SubscriptionListResponse]:
        """
        Retrieves a list of subscriptions for a specific company.
        """
        if not company_id:
            return ResponseModel(
                error=ErrorResponse(
                    message="Empty company ID",
                    type="400"
                ),
                is_success=False,
                message="Empty company ID"
            )

        self._refresh_token_if_expired()
        url = f"{self.settings.base_url}/subscriptions?companyId={company_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}

        response = requests.get(url, headers=headers)
        return self._check_response(response.text, url)

    def update_subscription(self, subscription: SubscriptionRequest) -> ResponseModel[SubscriptionResponse]:
        """
        Updates the subscription details.
        """
        if not subscription.subscription_id:
            return ResponseModel(
                error=ErrorResponse(
                    message="Empty subscription ID",
                    type="400"
                ),
                is_success=False,
                message="Empty subscription ID"
            )

        self._refresh_token_if_expired()
        url = f"{self.settings.base_url}/subscriptions/{subscription.subscription_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}
        body = {
            "quantity": subscription.quantity,
            "billingTerm": subscription.billing_term
        }

        response = requests.put(url, json=body, headers=headers)
        return self._check_response(response.text, url)
