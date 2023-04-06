from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    # List and create conversations
    path('conversations/', views.ConversationListCreate.as_view(), name='conversation-list-create'),
    # Retrieve, update, and delete a specific conversation
    path('conversations/<int:pk>/', views.ConversationDetail.as_view(), name='conversation-detail'),
    # Archive a conversation
    path('conversations/<int:pk>/archive/', views.ConversationArchive.as_view(), name='conversation-archive'),
    # End a conversation
    path('conversations/<int:pk>/end/', views.ConversationEnd.as_view(), name='conversation-end'),
    # Delete a conversation
    path('conversations/<int:pk>/delete/', views.ConversationDelete.as_view(), name='conversation-delete'),
    # List messages in a conversation
    path('conversations/<int:conversation_id>/messages/', views.MessageList.as_view(), name='message-list'),
    # Create a message in a conversation
    path('conversations/<int:conversation_id>/messages/create/', views.MessageCreate.as_view(), name='message-create'),
]
