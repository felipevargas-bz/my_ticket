from django.urls import path
from sales import views


urlpatterns = [
    path("api/event/", views.EventView.as_view(), name="events"),
    path("api/event/<int:pk>/", views.EventView.as_view(), name="event"),
    path("api/type/", views.TypeView.as_view(), name="types"),
    path("api/type/<int:pk>/", views.TypeView.as_view(), name="type"),
    path("api/ticket/", views.TicketView.as_view(), name="tickets"),
    path("api/ticket/<int:pk>/", views.TicketView.as_view(), name="ticket"),
]
