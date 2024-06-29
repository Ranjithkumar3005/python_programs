import phonenumbers
from phonenumbers import geocoder
from geopy.geocoders import Nominatim

def get_location_details(phone_number):
    try:
        number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(number, "en")
        geolocator = Nominatim(user_agent="phone_locator")
        location = geolocator.geocode(country, addressdetails=True)
        if location:
            address = location.raw['address']
            district = address.get('county', None)
            if district:
                return district
            else:
                return "District information not found."
        else:
            return "Location information not found."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
phone_number = "+91 9677702973"  # Replace with the phone number you want to lookup
district = get_location_details(phone_number)
print(f"The district of the phone number {phone_number} is: {district}")
