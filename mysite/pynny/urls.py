#!/usr/bin/python3
"""
File: urls.py
Author: Zachary King
Created: 2017-06-29

Defines the URLs (endpoint routing) for 
the Pynny web app.
"""

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import wallet_views, budget_views, category_views, transaction_views, main_views, savings_views, debt_views
from .views import notification_views

urlpatterns = [
    url(r'^$', main_views.index, name='index'), # /
    url(r'^dashboard/$', main_views.index, name='dashboard'),  # /dashboard/
    url(r'^login/$', auth_views.login, name='login'),  # /login/
    url(r'^logout/$', main_views.logout_view, name='logout'),  # /logout/
    url(r'^wallets/$', wallet_views.WalletsView.as_view(), name='wallets'),  # /wallets/
    url(r'^wallets/(?P<wallet_id>[0-9]+)$', wallet_views.SingleWalletView.as_view(), name='one_wallet',),  # /wallets/3
    url(r'^budgets/$', budget_views.BudgetsView.as_view(), name='budgets'), # /budgets/
    url(r'^budgets/(?P<budget_id>[0-9]+)$', budget_views.SingleBudgetView.as_view(), name='one_budget'),  # /budgets/9
    url(r'^categories/$', category_views.CategoriesView.as_view(), name='categories'),  # /categories/
    url(r'^categories/(?P<category_id>[0-9]+)$', category_views.SingleCategoryView.as_view(), name='one_category'),
    url(r'^transactions/$', transaction_views.TransactionsView.as_view(), name='transactions'),  # /transactions/
    url(r'^transactions/(?P<transaction_id>[0-9]+)$', transaction_views.SingleTransactionView.as_view(), name='one_transaction'),
    url(r'^budgets/renew/$', budget_views.RenewBudgetView.as_view(), name='renew_budgets'),  # /budgets/renew
    url(r'^savings/$', savings_views.SavingsView.as_view(), name='savings'),  # /savings/
    url(r'^savings/(?P<savings_id>[0-9]+)$', savings_views.SingleSavingView.as_view(), name='one_saving'),  # /savings/5
    url(r'^debt/$', debt_views.DebtsView.as_view(), name='debts'),
    url(r'^debt/(?P<debt_id>[0-9]})$', debt_views.SingleDebtView.as_view(), name='one_debt'),
    url(r'^notifications/dismiss/$', notification_views.dismiss_notice, name='dismiss_notice'),
    url(r'^settings/$', main_views.settings_view, name='settings'),  # /settings/
]
