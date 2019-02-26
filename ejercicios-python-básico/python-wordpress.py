#! /usr/bin/env python
import sys
# Librerias de python para wordpress
# pip install python-wordpress-xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media, posts
try:
    wp = Client('http://localhost/wordpress/xmlrpc.php', 'admin', '^Oy7AX(iZ4#3f3#G9q')
    #Insert en el sistema wordpress
    post = WordPressPost()
    post.title = "Demo insert post desde Python"
    post.content = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    post.post_status = 'publish'
    post.terms_names = {'post_tag': ['demo-python'],'category': ['desarrollo']}
    post.custom_fields = []
    post.custom_fields.append({'_demo':'1200'})
    wp.call(NewPost(post))
except Exception as e:
    sys.exit(e)
