from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Consultorio_app.api.views import PacienteViewSet, MedicoViewSet, CitaViewSet, TratamientoViewSet, RecetaViewSet, RecepcionViewSet, HistorialMedicoViewSet, DiagnosticoViewSet, MedicamentoViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'recetas', RecetaViewSet)
router.register(r'recepciones', RecepcionViewSet)
router.register(r'historiales_medicos', HistorialMedicoViewSet)
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]