# Python Web Scraping Project

This project is designed to perform web scraping using Selenium and send notifications via Twilio.

## Project Structure

```
python-web-scraping
├── src
│   ├── scraper.py
│   ├── notifier.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd python-web-scraping
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Twilio credentials:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   ```

## Usage

1. **Run the scraper**:
   You can start the scraping process by executing the `scraper.py` file:

   ```bash
   python src/scraper.py
   ```

2. **Send notifications**:
   Notifications will be sent automatically based on the scraped data using the `notifier.py` file.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License.
