from models import BlogCategory, BlogTag, BlogEntry
from django.views.generic import ListView, DetailView, DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView, ArchiveIndexView

class TagListView(ListView):
    model = BlogTag

class TagDetailView(DetailView):
    model = BlogTag

class CategoryListView(ListView):
    model = BlogCategory
    
class CategoryDetailView(DetailView):
    model = BlogCategory

class EntryYearView(YearArchiveView):
    model = BlogEntry
    date_field = 'date'

class EntryMonthView(MonthArchiveView):
    model = BlogEntry
    date_field = 'date'

class EntryDayView(DayArchiveView):
    model = BlogEntry
    date_field = 'date'

class EntryDetailView(DetailView):
    model = BlogEntry

class IndexView(ArchiveIndexView):
    date_field = 'date'
    model = BlogEntry

