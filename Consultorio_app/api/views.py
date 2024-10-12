from rest_framework import viewsets
from Consultorio_app.models import Paciente, Medico, Cita, Tratamiento, Receta, Recepcion, HistorialMedico, Diagnostico, Medicamento
from Consultorio_app.api.serializers import PacienteSerializer, MedicoSerializer, CitaSerializer, TratamientoSerializer, RecetaSerializer, RecepcionSerializer, HistorialMedicoSerializer, DiagnosticoSerializer, MedicamentoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class RecepcionViewSet(viewsets.ModelViewSet):
    queryset = Recepcion.objects.all()
    serializer_class = RecepcionSerializer

class HistorialMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistorialMedicoSerializer

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer