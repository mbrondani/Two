def read(request, note_id):
    """Reads a specific note from the Database"""
    list_of_notes = Note.objects.all().order_by('-last_update_date')
    template = 'notes/base.html'
    note = Note.objects.get(id=note_id)
    noteid = note.id
    target = Note.objects.get(id=note_id)
    if target.title == '':
        target.title = 'Write title here'
    if target.content == '':
        target.content = 'Write content here'
    form = NotesForm(initial={'title': target.title, 'content': target.content})
    context = {'list_of_notes': list_of_notes, 'target': target, 'form': form, 'noteid': noteid}
    return render(request, template, context)

def update(request):
    """Updates a specific note in the Database"""
    template = 'notes/update.html'
    list_of_notes = Note.objects.all().order_by('-last_update_date')
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            noteid = form.cleaned_data['noteid']
            note = Note.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()
            return HttpResponseRedirect('/')
    else:
        form = NotesForm()
        context = {'list_of_notes': list_of_notes, 'form':form}
        return render(request, template, context)    

def delete(request, note_id):
    """Deletes a specific note from the Database"""
    list_of_notes = Note.objects.all().order_by('-last_update_date')
    template = 'notes/base.html'
    target = Note.objects.get(id=note_id)
    tempid = target.id
    target.delete()
    deleted = True
    context = {'deleted': deleted, 'tempid': tempid, 'list_of_notes': list_of_notes}
    return render(request, template, context)