from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NoteSerializer
from .models import Note


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes = Note.objects.get(id = pk)
    serializer = NoteSerializer(notes,many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createnote(request):
    data = request.data
    
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note,many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatenote(request, pk):
    note = Note.objects.get(id =pk)
    serializer = NoteSerializer(note,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletenote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note is deleted!!")
