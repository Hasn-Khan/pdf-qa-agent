from pdf_parser import extract_text_from_pdf
from question_answering_agent import PDFQuestionAnsweringAgent
from slack_notifier import SlackNotifier, format_answers_for_slack

pdf_path = 'public/handbook.pdf'
questions = ["What is the name of the company?", "Who is the CEO of the company?", "What is their vacation policy?", "What is the termination policy?"]

pdf_text = extract_text_from_pdf(pdf_path)
qa_agent = PDFQuestionAnsweringAgent()
answers = qa_agent.answer_questions(pdf_text, questions)
slack_notifier = SlackNotifier()
slack_message = format_answers_for_slack(answers)

slack_notifier.post_message(slack_message)
