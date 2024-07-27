import openai
from config import OPENAI_API_KEY

class PDFQuestionAnsweringAgent:
  def __init__(self):
    openai.api_key = OPENAI_API_KEY

  def answer_questions(self, pdf_text, questions):
    answers = {}
    for question in questions:
      response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": f"Document: {pdf_text}"},
          {"role": "user", "content": f"Question: {question}"}
        ]
      )
      answer = response.choices[0].message['content'].strip()
      if "Data Not Available" in answer or len(answer) == 0:
        answers[question] = "Data Not Available"
      else:
        answers[question] = answer
    return answers
