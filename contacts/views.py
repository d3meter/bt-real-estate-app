from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,
                                                         user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing.')  # noqa: E501
                return redirect(f'/listings/{listing_id}')

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone,
                          message=message, user_id=user_id)

        contact.save()

        send_mail(
            subject='Property Listing Inquiry',
            message=f'There has been an inquiry for {listing}:\n{message}\n\nFrom {name}\n{email}\n{phone}',  # noqa: E501
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[realtor_email, settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon.')  # noqa: E501
        return redirect(f'/listings/{listing_id}')
