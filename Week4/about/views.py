from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'author.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_title'] = 'Об авторе'
        context['author_text'] = 'Проект выполнен Дмитрием Барминовым'
        context['author_vk'] = 'https://vk.com/id202844382'
        return context


class AboutTechView(TemplateView):
    template_name = 'tech.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_title'] = 'Технологии'
        context['tech_text'] = 'В проетке был использован фреймвок Django'
        context['tech_other'] = 'Использовались приложения posts, users, about'
        return context