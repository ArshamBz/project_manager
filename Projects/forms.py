from django import forms
from .models import Project, Task, SubTask


class ProjectForm(forms.ModelForm):
    color_option = (
        ('red', 'red'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gray', 'gray'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
    )
    title = forms.CharField(max_length=256, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=color_option, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Project
        fields = (
            'title',
            'image',
            'color',
            'budget',
            'start_date',
            'end_date',
            'description',
        )


class ProjectUpdateForm(forms.ModelForm):
    color_option = (
        ('red', 'red'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gray', 'gray'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
    )
    title = forms.CharField(max_length=256, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=color_option, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Project
        fields = (
            'title',
            'image',
            'color',
            'budget',
            'start_date',
            'end_date',
            'description',
            'status'
        )


class TaskForm(forms.ModelForm):
    color_option = (
        ('black', 'black'),
        ('blue', 'blue'),
        ('gray', 'gray'),
        ('red', 'red'),
        ('green', 'green'),
        ('orange', 'orange'),
        ('pink', 'pink'),
    )
    title = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=color_option, widget=forms.Select(attrs={'class': 'form-control'}))
    descriptions = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Task
        fields = (
            'title',
            'image',
            'color',
            'budget',
            'start_date',
            'end_date',
            'descriptions',
        )


class UpdateTaskForm(forms.ModelForm):
    color_option = (
        ('black', 'black'),
        ('blue', 'blue'),
        ('gray', 'gray'),
        ('red', 'red'),
        ('green', 'green'),
        ('orange', 'orange'),
        ('pink', 'pink'),
    )
    title = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=color_option, widget=forms.Select(attrs={'class': 'form-control'}))
    descriptions = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))

    class Meta:
        model = Task
        fields = (
            'title',
            'image',
            'color',
            'budget',
            'start_date',
            'end_date',
            'descriptions',
            'status'
        )


class SubTaskForm(forms.ModelForm):
    color_option = (
        ('black', 'black'),
        ('blue', 'blue'),
        ('gray', 'gray'),
        ('red', 'red'),
        ('green', 'green'),
        ('orange', 'orange'),
        ('pink', 'pink'),
    )
    title = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=color_option, widget=forms.Select(attrs={'class': 'form-control'}))
    descriptions = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = SubTask
        fields = (
            'title',
            'image',
            'color',
            'descriptions',
            'budget',
            'start_date',
            'end_date',
        )


class UpdateSubTaskForm(forms.ModelForm):
    color_option = (
        ('black', 'black'),
        ('blue', 'blue'),
        ('gray', 'gray'),
        ('red', 'red'),
        ('green', 'green'),
        ('orange', 'orange'),
        ('pink', 'pink'),
    )
    title = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=color_option, widget=forms.Select(attrs={'class': 'form-control'}))
    descriptions = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))

    class Meta:
        model = Task
        fields = (
            'title',
            'image',
            'color',
            'budget',
            'start_date',
            'end_date',
            'descriptions',
            'status'
        )
