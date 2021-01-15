import os
import easypost

easypost.api_key = os.environ.get('EASYPOST_TEST_API_KEY')

tracker = easypost.Tracker.create(
	tracking_code="EZ4000000004",
	carrier="USPS"
)

print(tracker)