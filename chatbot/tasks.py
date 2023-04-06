from celery import shared_task
from celery.utils.log import get_task_logger
import openai
from django.core.exceptions import ObjectDoesNotExist

logger = get_task_logger(__name__)

from .models import Message

system_prompt = "This is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very " \
                "friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you " \
                "today?\n\n"


@shared_task
def send_gpt3_request(conversation_id, message_list):
    try:
        # Send request to GPT-3 (replace with actual GPT-3 API call)
        gpt3_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                         {"role": "system",
                          "content": system_prompt},
                         {"role": "user", "content": "Who are you?"},
                         {"role": "assistant",
                          "content": "I am the sonic powered by ChatGpt.Contact me sonic@deadlyai.com"},
                     ] + message_list
        )

    except Exception as e:
        logger.error(f"Failed to send request to GPT-3: {e}")
        return

    try:
        # Store GPT-3 response as a message
        conversation = Conversation.objects.get(pk=conversation_id)
        message = Message(conversation=conversation, content=gpt3_response, is_from_user=False)
        message.save()
    except ObjectDoesNotExist:
        logger.error(f"Conversation with id {conversation_id} does not exist")
    except Exception as e:
        logger.error(f"Failed to save GPT-3 response as a message: {e}")
