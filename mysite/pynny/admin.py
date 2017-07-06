from django.contrib import admin

from .models import Wallet, Budget, Transaction, BudgetCategory

class WalletAdmin(admin.ModelAdmin):
    '''Admin model for the Wallet object'''
    readonly_fields = ('created_time',)
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Wallet Information', {'fields': ['name', 'balance', 'created_time']})
    ]
    list_display = ('name', 'balance', 'user', 'created_time')
    list_filter = ['user__username']
    search_fileds = ['name', 'user__username']


class BudgetCategoryAdmin(admin.ModelAdmin):
    '''Admin model for the BudgetCategories'''
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Category Information', {'fields': ['name', 'is_income']})
    ]
    list_display = ('name', 'is_income', 'user')
    list_filter = ['user__username', 'is_income']
    search_fields = ['name', 'user__username']


class BudgetAdmin(admin.ModelAdmin):
    '''Admin model for Budgets'''
    fieldsets = [
        (None, {'fields': ['user', 'wallet']}),
        ('Budget Information', {'fields': ['category', 'goal', 'balance', 'month']})
    ]
    list_display = ('user', 'wallet', 'category', 'balance', 'goal', 'month')
    list_filter = ['user__username', 'month']
    search_fields = ['user__username', 'category__name', 'wallet__name']


class TransactionAdmin(admin.ModelAdmin):
    '''Admin model for Transactions'''
    fieldsets = [
        (None, {'fields': ['user', 'wallet', 'category']}),
        ('Transaction Information', {'fields': ['amount', 'description', 'created_time']})
    ]
    list_display = ('user', 'wallet', 'category', 'amount', 'created_time')
    list_filter = ['user__username']
    search_fields = ['user__username', 'description', 'category__name', 'wallet__name']


admin.site.register(Wallet, WalletAdmin)
admin.site.register(BudgetCategory, BudgetCategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Budget, BudgetAdmin)
