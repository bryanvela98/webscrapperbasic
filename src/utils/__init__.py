def load_env():
    """Load environment variables from the .env file."""
    from dotenv import load_dotenv
    import os

    load_dotenv()

    return {
        "TWILIO_ACCOUNT_SID": os.getenv("TWILIO_ACCOUNT_SID"),
        "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
        "TWILIO_PHONE_NUMBER": os.getenv("TWILIO_PHONE_NUMBER"),
    }