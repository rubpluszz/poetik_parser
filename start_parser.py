#!~/projects/telegram_bot_one/botworkspace/bin/python3
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from parsers import ParsersForRyhmes

class VisualForDash():

    """ A class for managing the display of graphical information."""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    colors = {
                'background': '#111111',
                'text': '#7FDBFF'
             }

    app.layout = html.Div(
                            [
                                html.Div(
                                            style={'backgroundColor': colors['background']},
                                            children=html.H1(
                                                                id='header',
                                                                children='Parser Rhyme',
                                                                style={
                                                                        'textAlign': 'center',
                                                                        'color': colors['text']
                                                                      }
                                                                )
                                        ),
                                dcc.Dropdown(
                                                options=[
                                                            {'label': 'English', 'value': 'en'},
                                                            {'label': 'Українська', 'value':'ua'},
                                                            {'label': 'Русский', 'value': 'ru'},
                                                            {'label': 'Polski', 'value': 'pl'}
                                                        ],
                                                value='en', id='my_dropbox'
                                            ),
                                html.Label(children='Введіть слово для пошуку рими до нього',id='label-input'),
                                dcc.Input(value='rhyme',id='input-box', type='text', ),
                                html.Button(children ='Пошук', id='button'),
                                html.Div(id='output-container-button',
                                            children='Введи слово  і натисни пошук'
                                        ),
                                html.Div(id='result', children='...')
                            ]
                        )
    language = 'en'

    @app.callback(dash.dependencies.Output('button', 'children'),
        [dash.dependencies.Input('my_dropbox', 'value')])
    def update_output_buton(value):#Змінює текст на кнопці'
        vdb=VisualForDash
        if vdb.language == 'en':
            return ('search')
        if vdb.language == 'ua':
            return ('пошук')
        if vdb.language == 'ru':
            return ('поиск')
        if vdb.language == 'pl':
            return ('szukaj')

    @app.callback(dash.dependencies.Output('label-input', 'children'),
        [dash.dependencies.Input('my_dropbox', 'value')])
    def update_output_input_label(value):#Змінює текст id=label-input'
        vdb=VisualForDash
        if vdb.language == 'en':
            return ('Input word and click search')
        if vdb.language == 'ua':
            return ('Введи слово  і натисни пошук')
        if vdb.language == 'ru':
            return ('Введи слово и нажми поиск')
        if vdb.language == 'pl':
            return ('Wpisz słowo i kliknij szukaj')



    @app.callback(dash.dependencies.Output('header', 'children'),
        [dash.dependencies.Input('my_dropbox', 'value')])
    def update_output_header(value):#Зміна виводу заголовку
        vdb=VisualForDash
        vdb.language=value
        if vdb.language == 'en':
            return ('Parser Rhyme')
        if vdb.language == 'ua':
            return ('Римо Парсер')
        if vdb.language == 'ru':
            return ('Парсер Рифм')
        if vdb.language == 'pl':
            return ('Parser Rym')

    @app.callback(dash.dependencies.Output('input-box', 'value'),
         [dash.dependencies.Input('my_dropbox', 'value')])
    def update_output_input(value):#Зміна початкового напису в Input в залежності від вибраної мови
        vdb=VisualForDash
        if vdb.language == 'en':
            return ('rhyme')
        if vdb.language == 'ua':
            return ('рима')
        if vdb.language == 'ru':
            return ('рифма')
        if vdb.language == 'pl':
            return ('ryma')

    @app.callback(dash.dependencies.Output('result', 'children'),
                 [dash.dependencies.Input('button', 'n_clicks')],
                 [dash.dependencies.State('input-box', 'value')])
    def update_output_result(n_clicks, value):#Запускає відповідний парсер і передає йому введене користувачем слово, повертає масив повернений парсером для виводу в result.
        vdb=VisualForDash
        print(vdb.language)
        parser = ParsersForRyhmes(value)
        if vdb.language=='ua':
            return (parser.selenium_parser_uk())
        if vdb.language=='en':
            return (parser.selenium_parser_en())
        if vdb.language=='ru':
            return (parser.selenium_parser_ru())
        if vdb.language=='pl':
            return (parser.selenium_parser_pl())


if __name__ == '__main__':
    VisualForDash.app.run_server(debug=True)
