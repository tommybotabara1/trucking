from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('database_operations/', views.database_operations, name='database_operations'),
    path('database_operations/year=<int:year>/month=<int:month>/day=<int:day>', views.database_operations_year_month, name='database_operations_year_month'),
    path('database_operations/newDBO', views.new_database_operation, name='new_database_operation'),
    path('database_operations/editDBO/<int:id>/<str:phase>', views.edit_database_operation, name='edit_database_operation'),
    path('database_operations/deleteDBO/<int:id>', views.delete_database_operation, name='delete_database_operation'),
    path('database_operations/statement_of_account', views.dbo_statement_of_account, name='dbo_statement_of_account'),
    path('database_operations/summary_of_payroll', views.dbo_summary_of_payroll, name='dbo_summary_of_payroll'),
    path('database_operations/balance_sheet', views.dbo_balance_sheet, name='dbo_balance_sheet'),
    path('database_operations/income_statement', views.dbo_income_statement, name='dbo_income_statement'),
    path('database_operations/summary', views.dbo_summary, name='dbo_summary'),


    path('tariff/', views.tariff, name='tariff'),
    path('tariff/new_tariff', views.new_tariff, name='new_tariff'),
    path('tariff/edit_tariff/<int:id>', views.edit_tariff, name='edit_tariff'),
    path('tariff/delete_tariff/<int:id>', views.delete_tariff, name='delete_tariff'),
    path('truck_budget/', views.truck_budget, name='truck_budget'),
    path('truck_budget/new_truck_budget', views.new_truck_budget, name='new_truck_budget'),
    path('truck_budget/edit_truck_budget/<int:id>', views.edit_truck_budget, name='edit_truck_budget'),
    path('truck_budget/delete_truck_budget/<int:id>', views.delete_truck_budget, name='delete_truck_budget'),
    path('statement_of_account/', views.statement_of_account, name='statement_of_account'),
    path('statement_of_account/new_statement_of_account', views.new_statement_of_account, name='new_statement_of_account'),
    path('statement_of_account/edit_statement_of_account/<int:id>', views.edit_statement_of_account, name='edit_statement_of_account'),
    path('statement_of_account/delete_statement_of_account/<int:id>', views.delete_statement_of_account, name='delete_statement_of_account'),
    path('direct_payroll/', views.direct_payroll, name='direct_payroll'),
    path('direct_payroll/new_direct_payroll', views.new_direct_payroll, name='new_direct_payroll'),
    path('direct_payroll/edit_direct_payroll/<int:id>', views.edit_direct_payroll, name='edit_direct_payroll'),
    path('direct_payroll/delete_direct_payroll/<int:id>', views.delete_direct_payroll, name='delete_direct_payroll'),
    path('breakdown/', views.breakdown, name='breakdown'),
    path('breakdown/new_breakdown', views.new_breakdown, name='new_breakdown'),
    path('breakdown/edit_breakdown/<int:id>', views.edit_breakdown, name='edit_breakdown'),
    path('breakdown/delete_breakdown/<int:id>', views.delete_breakdown, name='delete_breakdown'),
    path('canteen/', views.canteen, name='canteen'),
    path('canteen/new_canteen', views.new_canteen, name='new_canteen'),
    path('canteen/edit_canteen/<int:id>', views.edit_canteen, name='edit_canteen'),
    path('canteen/delete_canteen/<int:id>', views.delete_canteen, name='delete_canteen'),
    path('damages/', views.damages, name='damages'),
    path('damages/new_damages', views.new_damages, name='new_damages'),
    path('damages/edit_damages/<int:id>', views.edit_damages, name='edit_damages'),
    path('damages/delete_damages/<int:id>', views.delete_damages, name='delete_damages'),
    path('users/', views.users, name='users'),
    path('testing/', views.testing, name='testing'),
    path('add_new_driver/', views.add_new_driver, name='add_new_driver'),
    path('add_new_customer/', views.add_new_customer, name='add_new_customer'),
    path('add_new_client/', views.add_new_client, name='add_new_client'),
    path('add_new_helper/', views.add_new_helper, name='add_new_helper'),
    path('add_new_split_amount/', views.add_new_split_amount, name='add_new_split_amount'),
    path('get_split_amount/', views.get_split_amount, name='get_split_amount'),
    path('get_split_amount_total/', views.get_split_amount_total, name='get_split_amount_total'),
    path('delete_split_amount/', views.delete_split_amount, name='delete_split_amount'),

    path('payables/', views.payables, name='payables'),
    path('payables/new_payables', views.new_payables, name='new_payables'),
    path('payables/edit_payables/<int:id>', views.edit_payables, name='edit_payables'),
    path('payables/delete_payables/<int:id>', views.delete_payables, name='delete_payables'),

    path('liquidation/', views.liquidation, name='liquidation'),
    path('liquidation/new_liquidation', views.new_liquidation, name='new_liquidation'),
    path('liquidation/edit_liquidation/<int:id>', views.edit_liquidation, name='edit_liquidation'),
    path('liquidation/delete_liquidation/<int:id>', views.delete_liquidation, name='delete_liquidation'),

    path('cash_monitoring/', views.cash_monitoring, name='cash_monitoring'),
    path('cash_monitoring/new_cash_monitoring', views.new_cash_monitoring, name='new_cash_monitoring'),
    path('cash_monitoring/edit_cash_monitoring/<int:id>', views.edit_cash_monitoring, name='edit_cash_monitoring'),
    path('cash_monitoring/delete_cash_monitoring/<int:id>', views.delete_cash_monitoring, name='delete_cash_monitoring'),

    path('cash_on_hand/', views.cash_on_hand, name='cash_on_hand'),
    path('cash_on_hand/new_cash_on_hand', views.new_cash_on_hand, name='new_cash_on_hand'),
    path('cash_on_hand/edit_cash_on_hand/<int:id>', views.edit_cash_on_hand, name='edit_cash_on_hand'),
    path('cash_on_hand/delete_cash_on_hand/<int:id>', views.delete_cash_on_hand, name='delete_cash_on_hand'),

    path('billing_statement_or/', views.billing_statement_or, name='billing_statement_or'),
    path('billing_statement_or/new_billing_statement_or', views.new_billing_statement_or, name='new_billing_statement_or'),
    path('billing_statement_or/edit_billing_statement_or/<int:id>', views.edit_billing_statement_or, name='edit_billing_statement_or'),
    path('billing_statement_or/delete_billing_statement_or/<int:id>', views.delete_billing_statement_or, name='delete_billing_statement_or'),

    path('billing_statement_ar/', views.billing_statement_ar, name='billing_statement_ar'),
    path('billing_statement_ar/new_billing_statement_ar', views.new_billing_statement_ar, name='new_billing_statement_ar'),
    path('billing_statement_ar/edit_billing_statement_ar/<int:id>', views.edit_billing_statement_ar, name='edit_billing_statement_ar'),
    path('billing_statement_ar/delete_billing_statement_ar/<int:id>', views.delete_billing_statement_ar, name='delete_billing_statement_ar'),

    path('ajax/get_dbo/', views.get_dbo, name='get_dbo'),
    path('ajax/update_billing_date/', views.update_billing_dates, name='update_billing_dates'),
    path('ajax/get_client/', views.get_client, name='get_client'),
    path('ajax/get_customer/', views.get_customer, name='get_customer'),
    path('ajax/get_plate_number/', views.get_plate_number, name='get_plate_number'),
    path('ajax/get_way_bill_number/', views.get_way_bill_number, name='get_way_bill_number'),
    path('ajax/get_truck_type/', views.get_truck_type, name='get_truck_type'),
]
