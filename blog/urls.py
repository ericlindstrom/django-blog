from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    # tags
    url(r'^tags/$', TagListView.as_view(), name='tag_list'),
    url(r'^tag/(?P<slug>.*)/$', TagDetailView.as_view(), name='tag_detail'),
    # categories
    url(r'^categories/$', CategoryListView.as_view(), name='category_list'),
    url(r'^category/(?P<slug>.*)/$', CategoryDetailView.as_view(), name='category_detail'),
    # archive
    url(r'^(?P<year>\d{4})/$', EntryYearView.as_view(), name='entry_year_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', EntryMonthView.as_view(), name='entry_month_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', EntryDayView.as_view(), name='entry_day_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.*)/$', EntryDetailView.as_view(), name='entry_detail'),
)
