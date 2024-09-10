from django.shortcuts import render, redirect, get_object_or_404
from openai import Client

from .forms import ImageForm
from .models import Image

client = Client()


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.url = create_image(client, form.instance.animal, form.instance.artist)
            image = form.save()
            return redirect('image-details', image_id=image.id)
    else:
        form = ImageForm()

    return render(request, 'index.html', {'form': form})


def image_details(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'image.html', {'image': image})


def create_image(openai_client: Client, animal: str, artist: str) -> str:
    prompt = f'Create an image of a {animal} in the style of {artist}'
    response = openai_client.images.generate(prompt=prompt, model='dall-e-3')
    return response.data[0].url
