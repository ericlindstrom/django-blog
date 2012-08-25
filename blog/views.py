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

    def get_context_data(self, *kwargs):
	context = super(IndexView, self).get_context_data(**kwargs)

	return context


index_view = IndexView.as_view()
tag_list = TagListView.as_view()
tag_detail = TagDetailView.as_view()
category_list = CategoryListView.as_view()
category_detail = CategoryDetailView.as_view()
entry_year_detail = EntryYearView.as_view()
entry_month_detail = EntryMonthView.as_view()
entry_day_detail = EntryDayView.as_view()
entry_detail = EntryDetailView.as_view()
