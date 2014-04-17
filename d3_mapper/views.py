from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    return {'project': 'd3_mapper'}

@view_config(route_name='home2', renderer='templates/index_2.pt')
def my_view2(request):
    return {'project': 'd3_mapper'}

@view_config(route_name='home3', renderer='templates/logging_functions.pt')
def my_view3(request):
    return {'project': 'd3_mapper'}
