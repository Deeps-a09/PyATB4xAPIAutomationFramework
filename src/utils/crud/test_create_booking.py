# API TestCase

# 1. URL -> Available in API Constants.p
# 2. headers -> Available in Utils.py
# 3. Payload -> Available in payload_manager.py
# 4. HTTP POST -> Available in api_requests_wrappers.py
# 5. verification -> Available in common_verification.p

import allure
import pytest
from src.helpers.api_requests_wrappers import post_request
from src.constants.api_contstants import APIConstants
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils
import logging


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking and Booking ID should not ")
    @allure.description("Creating booking from the payload and verify that booking id should not")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the TESTCASE - TC1")
        # 1. URL
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        LOGGER.info(response.json()["bookingid"])
        LOGGER.info("End of the TESTCASE TC1 - Positive")


    def test_create_booking_negative(self):
        @pytest.mark.negative
        @allure.title("Verify that Create Booking and Booking ID doesn't work with no payload")
        @allure.description("Creating booking with no payload")
        def test_create_booking_negative(self):
            LOGGER = logging.getLogger(__name__)
            LOGGER.info("TESTCASE - TC2")
            # 1. URL
            response = post_request(
                url=APIConstants().url_create_booking(),
                auth=None,
                headers=Utils().common_headers_json(),
                payload={},
                in_json=False
            )
            verify_http_status_code(response_data=response, expected_data=500)
            #verify_json_key_for_not_null(response.json()["bookingid"])
            LOGGER.info(response.json()["bookingid"])
            LOGGER.info("End of the TESTCASE TC2 - Negative")
