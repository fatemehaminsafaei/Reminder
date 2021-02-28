# from django.core.serializers import serialize
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView
from apps.todo.forms import TaskForm, CategoryForm
from django.views.generic.base import View

from apps.todo.models import Task, Category


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories_list'


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_Task'] = Task.objects.all()[:3]
        context['done_task'] = Task.objects.get_passed_tasks()
        context['E_Category'] = Category.objects.get_empty_category()
        context['full_category'] = Category.objects.get_full_category()
        context['empty_category'] = Category.objects.get_empty_category()
        return context


class Lists(DetailView):
    model = Category
    context_object_name = 'Lists'
    template_name = 'lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryView(View):
    def get(self, request):
        form = CategoryForm(request.Post)
        return render(request, 'registeredcategory.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.Post)
        if form.is_valid():
            validated_data = form.cleaned_data
            category_obj = Category(**validated_data)
            category_obj.save()
            return redirect('saved Successfully')
        return render(request, 'registeredcategory.html', {'form': form})


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            task_obj = Task(**validated_data)
            task_obj.save()
            return redirect('ok')

    else:
        form = TaskForm()
    return render(request, 'registeredtask.html', {'form': form})


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            category_obj = Category(**validated_data)
            category_obj.save()
            return redirect('ok')
    else:
        form = CategoryForm()
    return render(request, 'registeredcategory.html', {'form': form})



def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            form.instance.author = request.user.user
            validated_data = form.cleaned_data
            task_obj = Task(**validated_data)
            task_obj.save()
            return redirect('ok')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            form.instance.author = request.user.user
            validated_data = form.cleaned_data
            category_obj = Category(**validated_data)
            category_obj.save()
            return redirect('ok')
    else:
        form = TaskForm(instance=Category)
    return render(request, 'category_edit.html', {'form': form})



class TaskListAPI(View):
    def get(self, request):
        serialized_task_list = serialize('json', Task.objects.all())
        return HttpResponse(serialized_task_list, content_type='application/json')
