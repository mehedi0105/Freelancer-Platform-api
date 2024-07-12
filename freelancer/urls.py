from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Proposal_Veiw_set, ProposalSigleitemAPIView

router = DefaultRouter()

router.register('poposal',Proposal_Veiw_set)

urlpatterns = [
    path('', include(router.urls)),
    path('update_proposal/<int:pk>/',ProposalSigleitemAPIView.as_view(),name="update_proposal"),
]