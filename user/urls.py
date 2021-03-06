from django.urls import path
from .views import user_login, user_logout, user_signup , user_detail , user_infomodify , user_search, user_list, toggle_follow_realtion
from .permission_view import set_normal_user , set_normal_admin , set_super_admin

urlpatterns = [
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('signup/', user_signup, name='user-signup'),
    path('detail/<int:user_id>/' , user_detail , name = 'user-detail'),
    path('search/<str:displayname>/' , user_search , name = 'user-search' ),
    path('list/<int:page>/' , user_list , name = 'user-list' ),
    path('infomodify/' , user_infomodify , name = 'user-infomodify' ),
    path('followrelation/toggle/' , toggle_follow_realtion , name = 'user-toggle-follow-relation' ),
    path('permission/set_normal_user/' , set_normal_user , name = 'user-set-normal-user' ),
    path('permission/set_normal_admin/' , set_normal_admin , name = 'user-set-normal-admin' ),
    path('permission/set_super_admin/' , set_super_admin , name = 'user-set-super-admin' )
]