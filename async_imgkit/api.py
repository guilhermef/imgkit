# -*- coding: utf-8 -*-
from async_imgkit.async_imgkit import AsyncIMGKit
from async_imgkit.config import Config


async def from_url(url,
             output_path,
             options=None,
             toc=None,
             cover=None,
             config=None,
             cover_first=None):
    """
    Convert URL/URLs to IMG file/files

    :param url: URL or list of URLs to be saved
    :param output_path: path to output PDF file/files. False means file will be returned as string
    :param options: (optional) dict with wkhtmltopdf global and page options, with or w/o '--'
    :param toc: (optional) dict with toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: (optional) string with url/filename with a cover html page
    :param css: style of input
    :param config: (optional) instance of imgkit.config.Config()
    :param cover_first: (optional) if True, cover always precedes TOC
    :return: True when success
    """
    rtn = await AsyncIMGKit.create(url,
                 'url',
                 options=options,
                 toc=toc, cover=cover,
                 config=config,
                 cover_first=cover_first)
    return await rtn.to_img(output_path)


async def from_file(filename,
              output_path,
              options=None,
              toc=None,
              cover=None,
              css=None,
              config=None,
              cover_first=None):
    """
    Convert HTML file/files to IMG file/files

    :param filename: path of HTML file or list with paths or file-like object
    :param output_path: path to output PDF file/files. False means file will be returned as string
    :param options: (optional) dict with wkhtmltopdf global and page options, with or w/o '--'
    :param toc: (optional) dict with toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: (optional) string with url/filename with a cover html page
    :param css: style of input
    :param config: (optional) instance of imgkit.config.Config()
    :param cover_first: (optional) if True, cover always precedes TOC
    :return: True when success
    """
    rtn = await AsyncIMGKit.create(filename,
                 'file',
                 options=options,
                 toc=toc,
                 cover=cover,
                 css=css,
                 config=config,
                 cover_first=cover_first)
    return await rtn.to_img(output_path)


async def from_string(string,
                output_path,
                options=None,
                toc=None,
                cover=None,
                css=None,
                config=None,
                cover_first=None):
    """
    Convert given string/strings to IMG file

    :param string:
    :param output_path: path to output PDF file/files. False means file will be returned as string
    :param options: (optional) dict with wkhtmltopdf global and page options, with or w/o '--'
    :param toc: (optional) dict with toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: (optional) string with url/filename with a cover html page
    :param css: style of input
    :param config: (optional) instance of imgkit.config.Config()
    :param cover_first: (optional) if True, cover always precedes TOC
    :return: True when success
    """
    rtn = await AsyncIMGKit.create(string, 'string', options=options, toc=toc, cover=cover, css=css,
                 config=config, cover_first=cover_first)
    return await rtn.to_img(output_path)


async def config(**kwargs):
    """
    Constructs and returns a :class:`Config` with given options

    :param wkhtmltopdf: path to binary
    :param meta_tag_prefix: the prefix for ``pdfkit`` specific meta tags
    """

    return await Config.create(**kwargs)
