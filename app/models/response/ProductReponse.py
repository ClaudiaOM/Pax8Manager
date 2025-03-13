class ProductResponse:
    """
    Represents details about a product.
    """
    def __init__(self, id, name, vendor_name, short_description, sku, vendor_sku, alt_vendor_sku):
        """
        Initializes an instance of the ProductResponse class.
        :param id: The unique ID of the product
        :param name: The name of the product
        :param vendor_name: The name of the vendor
        :param short_description: A short description of the product
        :param sku: The product's SKU (Stock Keeping Unit)
        :param vendor_sku: The vendor's SKU
        :param alt_vendor_sku: The Microsoft legacy subscription SKU
        """
        self.id = id
        self.name = name
        self.vendor_name = vendor_name
        self.short_description = short_description
        self.sku = sku
        self.vendor_sku = vendor_sku
        self.alt_vendor_sku = alt_vendor_sku

    def __repr__(self):
        return (f"ProductResponse(id={self.id}, name={self.name}, vendor_name={self.vendor_name}, "
                f"short_description={self.short_description}, sku={self.sku}, "
                f"vendor_sku={self.vendor_sku}, alt_vendor_sku={self.alt_vendor_sku})")


class ProductListResponse:
    """
    Represents a paginated list of products.
    """
    def __init__(self, content, page):
        """
        Initializes an instance of the ProductListResponse class.
        :param content: List of ProductResponse objects
        :param page: An instance of PageResponse with pagination details
        """
        self.content = content  # List of ProductResponse objects
        self.page = page        # An instance of PageResponse

    def __repr__(self):
        return f"ProductListResponse(content={self.content}, page={self.page})"
