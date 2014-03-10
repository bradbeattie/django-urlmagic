# django-urlmagic

The purpose of this library is to provide a consistent set of URL patterns for models.

## Pending functionality

* Singular combined add/edit and add/detail views (e.g. visit /mymodel/ to create or edit)
* Implement a view that allows related content lists (e.g. /foos/123/bars/ for all Bars related to a Foo)
* Extend singular views from MyUrlGenerator to guests (e.g. /foos/123/bar/ for a OneToOne mapping between a Foo and a Bar)
