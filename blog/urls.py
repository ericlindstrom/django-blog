from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    # tags
    url(r'^tags/$', tag_list, name='tag_list'),
    url(r'^tag/(?P<slug>.*)/$', tag_detail, name='tag_detail'),
    # categories
    url(r'^categories/$', category_list, name='category_list'),
    url(r'^category/(?P<slug>.*)/$', category_detail, name='category_detail'),
    # archive
    url(r'^(?P<year>\d{4})/$', entry_year_detail, name='entry_year_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', entry_month_detail, name='entry_month_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', entry_day_detail, name='entry_day_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.*)/$', entry_detail, name='entry_detail'),
)
