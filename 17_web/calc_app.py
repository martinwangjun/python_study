#!/usr/bin/python
# -*- coding: utf-8 -*-

def calculation(env, start_response):
    start_response(
        '200 OK',
        [('Content-Type', 'text/html')]
    )
