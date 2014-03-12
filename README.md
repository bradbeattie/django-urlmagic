# django-urlmagic

The purpose of this library is to provide a consistent set of URL patterns, names, and template sources for models.

## Pending functionality

I believe the following features may have been implemented, but need more testing.

* Extend singular views from MyUrlGenerator to guests (e.g. /foos/123/bar/ for a OneToOne mapping between a Foo and a Bar)
* Use the request's user object as a potential key into related lists (e.g. visit /my/foos/, /my/foos/123/, /my/bar/, etc)
