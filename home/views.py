from django.shortcuts import render

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        return render(request, 'HTML_contact.html', {
            'message': f"Thank you {name}, we received your email: {email}"
        })
    return render(request, 'HTML_contact.html')