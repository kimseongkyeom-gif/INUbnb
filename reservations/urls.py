from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "create/<int:room>/<int:year>-<int:month>-<int:day>",
        views.create,
        name="create",
    ),
    path("<int:pk>/", views.ReservationDetailView.as_view(), name="detail"),
    path("<int:pk>/<str:verb>/", views.edit_reservation, name="edit"),
    path("user/<int:pk>", views.see_reservations, name="see-reservations",),
    path("delete/<int:pk>", views.del_reservations, name="del-reservations",),
]
