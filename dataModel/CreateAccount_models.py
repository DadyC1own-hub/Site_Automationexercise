from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CreateAccountRequest(BaseModel):
    name: str
    email: str
    password: str
    title: str
    birth_date: Optional[str] = None
    birth_month: Optional[str] = None
    birth_year: Optional[str] = None
    firstname: str
    lastname: str
    company: Optional[str] = None
    address1: str
    address2: Optional[str] = None
    country: str
    zipcode: str
    state: str
    city: str
    mobile_number: str

    @staticmethod
    def get_default(
            name: str = "Mr",
            email: str = "testuser@example.com",
            password: str = "password123",
            title: str = "Mr",
            birth_date: Optional[str] = "01",
            birth_month: Optional[str] = "January",
            birth_year: Optional[str] = "1990",
            firstname: str = "John",
            lastname: str = "Doe",
            company: Optional[str] = "Test Company",
            address1: str = "123 Test St",
            address2: Optional[str] = "Apt 456",
            country: str = "United States",
            zipcode: str = "12345",
            state: str = "CA",
            city: str = "Test City",
            mobile_number: str = "+1234567890"
    ) -> 'CreateAccountRequest':
        # Создаем экземпляр модели с переданными значениями
        return CreateAccountRequest(
            name=name,
            email=email,
            password=password,
            title=title,
            birth_date=birth_date,
            birth_month=birth_month,
            birth_year=birth_year,
            firstname=firstname,
            lastname=lastname,
            company=company,
            address1=address1,
            address2=address2,
            country=country,
            zipcode=zipcode,
            state=state,
            city=city,
            mobile_number=mobile_number
        )


class CreateAccountResponse(BaseModel):
    message: str
