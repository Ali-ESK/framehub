from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video

def is_admin(user):
    return user.is_superuser or user.is_staff

@login_required
def video_list(request):
    videos = Video.objects.order_by("-created_at")
    return render(request, "videos/list.html", {"videos": videos})

@login_required
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, "videos/detail.html", {"video": video})

@login_required
@user_passes_test(is_admin)
def upload_video(request):
    if request.method == "POST":
        title = request.POST.get("title") or request.FILES["file"].name
        f = request.FILES["file"]
        Video.objects.create(title=title, file=f, uploaded_by=request.user)
        return redirect("videos:list")
    return render(request, "videos/upload.html")
