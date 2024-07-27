from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_TOKEN, SLACK_CHANNEL_ID

class SlackNotifier:
  def __init__(self):
    self.client = WebClient(token=SLACK_TOKEN)
    self.channel_id = SLACK_CHANNEL_ID

  def post_message(self, message):
    try:
      response = self.client.chat_postMessage(channel=self.channel_id, text=message)
    except SlackApiError as e:
      print(f"Error posting to Slack: {e.response['error']}")

def format_answers_for_slack(answers):
  formatted_message = ""
  for question, answer in answers.items():
    formatted_message += f"*Q: {question}*\nA: {answer}\n\n"
  return formatted_message
