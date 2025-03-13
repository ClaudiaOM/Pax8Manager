class AddressResponse:
    """
    Represents the address details of a company.
    """
    def __init__(self, street, street2, city, state_or_province, postal_code, country):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state_or_province = state_or_province
        self.postal_code = postal_code
        self.country = country

class CompanyResponse:
    """
    Represents details about a company.
    """
    def __init__(self, id, name, address, phone, website, external_id, 
                 bill_on_behalf_of_enabled, self_service_allowed, 
                 order_approval_required, status):
        self.id = id
        self.name = name
        self.address = address  # An instance of AddressResponse
        self.phone = phone
        self.website = website
        self.external_id = external_id
        self.bill_on_behalf_of_enabled = bill_on_behalf_of_enabled
        self.self_service_allowed = self_service_allowed
        self.order_approval_required = order_approval_required
        self.status = status

class CompanyListResponse:
    """
    Represents a paginated list of companies.
    """
    def __init__(self, content, page):
        self.content = content  # List of CompanyResponse objects
        self.page = page  # Page details (could define a PageResponse class if needed)
