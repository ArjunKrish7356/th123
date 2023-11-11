import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from google.auth import default
from google.auth.transport.requests import Request

# Try to get credentials from the environment
try:
    credentials, _ = default()
except Exception as e:
    # If not found, or if the credentials are expired, initiate the authentication flow
    credentials = None

if credentials is None or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        # If no credentials are available or they are not valid, prompt the user to authenticate
        credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])

# Now you can use the 'credentials' object for your API requests

vertexai.init(project="kinetic-octagon-404610", location="us-central1")

#setting up the chat-bison model
text_model = TextGenerationModel.from_pretrained("text-bison")
parameters = {
    "temperature": 0.5,
    "max_output_tokens": 2048,
    "top_p": 0.8,
    "top_k": 40
}
response = text_model.predict(
    """Always show forms,letters and documents with proper structure and format
    
    """,
)

print(f"Response from Model: {response.text}")